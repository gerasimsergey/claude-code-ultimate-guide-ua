---
title: "Довідник налаштувань Claude Code"
description: "Повний довідник конфігурацій settings.json та змінних оточення для Claude Code v2.1.81+"
tags: [reference, configuration, environment-variables, settings, ukrainian]
---

# Довідник налаштувань Claude Code

> Повний довідник для конфігурації `settings.json` та змінних оточення. Охоплює всі підтверджені налаштування станом на Claude Code v2.1.81.

**Джерела:** [Офіційна документація](https://code.claude.com/docs/en/settings) · [JSON Схема](https://json.schemastore.org/claude-code-settings.json)

**Легенда:**
- Без значка = підтверджено в офіційній документації
- `📋 Тільки схема` = присутнє в JSON-схемі, але не на офіційній сторінці — все одно працює
- `⚠️ Неперевірено` = не підтверджено в офіційних джерелах

---

## Області видимості та пріоритетність

Claude Code використовує чотири рівні налаштувань, які застосовуються від найвищого до найнижчого пріоритету:

| Пріоритет | Область | Розташування | Спільне? | Призначення |
|----------|-------|----------|---------|---------|
| 1 | **Managed** | Сервер, MDM-профіль або `managed-settings.json` | Так (від IT) | Політики організації, неможливо змінити |
| 2 | **Командний рядок** | Прапорці `--` при запуску | Ні | Тимчасові налаштування сесії |
| 3 | **Local** | `.claude/settings.local.json` | Ні (gitignored) | Персональні налаштування для проекту |
| 4 | **Project** | `.claude/settings.json` | Так (у Git) | Спільні налаштування команди |
| 5 | **User** | `~/.claude/settings.json` | Ні | Глобальні особисті налаштування |

**Об'єднання масивів:** Такі налаштування як `permissions.allow`, `sandbox.filesystem.allowWrite` та `allowedHttpHookUrls` об'єднуються з усіх рівнів і дедуплікуються, а не замінюються.

**Пріоритет заборони:** Правила `permissions.deny` завжди мають перевагу над дозволами на будь-якому рівні.

---

## Ключі налаштувань

### Основна конфігурація

#### `$schema`
**Тип:** string | **Область:** всі | **Типово:** немає
URL JSON-схеми для валідації в IDE та автодоповнення. Рекомендується додати `"https://json.schemastore.org/claude-code-settings.json"`.

#### `model`
**Тип:** string | **Область:** всі | **Типово:** `"default"`
Перевизначення моделі для всіх сесій. Приймає аліаси (`"sonnet"`, `"opus"`, `"haiku"`) або повні ID.

#### `language`
**Тип:** string | **Область:** всі | **Типово:** `"english"`
Бажана мова відповідей Claude та мова голосового диктування. Наприклад: `"ukrainian"`, `"japanese"`.

#### `cleanupPeriodDays`
**Тип:** number | **Область:** всі | **Типово:** `30`
Кількість днів, після яких неактивні сесії видаляються. `0` вимикає збереження історії сесій.

#### `autoUpdatesChannel`
**Тип:** string | **Область:** всі | **Типово:** `"latest"`
Канал оновлень: `"latest"` (найновіші) або `"stable"` (стабільні, зазвичай з відставанням на тиждень).

#### `includeGitInstructions`
**Тип:** boolean | **Область:** всі | **Типово:** `true`
Чи включати вбудовані інструкції для комітів та PR у системний промпт.

#### `companyAnnouncements`
**Тип:** array of strings | **Область:** всі
Оголошення, що відображаються користувачам при запуску.

#### `defaultShell`
**Тип:** string | **Область:** всі | **Типово:** `"bash"`
Оболонка за замовчуванням для команд `!`. Можна встановити `"powershell"` для Windows.

---

### Плани та Пам'ять

#### `plansDirectory`
**Тип:** string | **Область:** всі | **Типово:** `"~/.claude/plans"`
Директорія для виводів команди `/plan`. Шлях відносно кореня проекту.

#### `autoMemoryEnabled`
**Тип:** boolean | **Область:** всі | **Типово:** `true`
Увімкнути/вимкнути функцію автоматичної пам'яті (збереження контексту між сесіями).

---

### Дозволи (Permissions)

#### `permissions.allow` / `permissions.ask` / `permissions.deny`
**Тип:** array of strings
Списки інструментів та операцій, які дозволені (без запиту), потребують підтвердження (ask) або заборонені (deny).

**Синтаксис правил:**
| Інструмент | Патерн | Приклад |
|------|---------|---------|
| `Bash` | Команда з вайлдкардами | `Bash(npm run *)` |
| `Read` | Шлях до файлу | `Read(.env)` |
| `Edit` | Шлях до файлу | `Edit(src/**)` |
| `WebFetch` | Хост | `WebFetch(domain:google.com)` |

---

### Пісочниця (Sandbox)

Налаштування ізоляції Bash-команд. Доступно на macOS, Linux та WSL2.

#### `sandbox.enabled`
**Тип:** boolean | **Типово:** `false`
Увімкнути пісочницю для ізоляції команд від файлової системи та мережі.

#### `sandbox.autoAllowBashIfSandboxed`
**Тип:** boolean | **Типово:** `true`
Автоматично дозволяти Bash-команди, якщо вони виконуються в пісочниці.

#### `sandbox.network.allowedDomains`
**Тип:** array of strings
Домени, до яких дозволено доступ з пісочниці (наприклад, `*.npmjs.org`).

---

### Атрибуція (Attribution)

#### `attribution.commit` / `attribution.pr`
**Тип:** string
Текст, що додається до повідомлень комітів або описів PR. Встановіть порожній рядок `""`, щоб вимкнути підпис "Generated with Claude Code".

---

### Дисплей та UX

#### `outputStyle`
**Тип:** string | **Типово:** `"Default"`
Стиль спілкування Claude:
- `"Default"` — лаконічний, орієнтований на швидкість.
- `"Explanatory"` — додає пояснення щодо вибору архітектури та рішень.
- `"Learning"` — режим парного програмування, Claude залишає `TODO(human)` для вас.

#### `respectGitignore`
**Тип:** boolean | **Типово:** `true`
Чи повинен вибір файлів через `@` враховувати правила `.gitignore`.

---

## Змінні оточення

Встановлюються у вашому терміналі або в ключі `env` у `settings.json`.

| Змінна | Опис |
|----------|-------------|
| `ANTHROPIC_API_KEY` | API ключ для прямого доступу |
| `ANTHROPIC_MODEL` | Модель для використання (sonnet, opus, haiku) |
| `CLAUDE_CODE_EFFORT_LEVEL` | Рівень зусиль міркування: `low`, `medium`, `high` |
| `CLAUDE_CODE_SIMPLE` | Увімкнути мінімалістичний інтерфейс |
| `DISABLE_TELEMETRY` | Вимкнути відправку телеметрії (`1`) |
| `HTTP_PROXY` / `HTTPS_PROXY` | Налаштування проксі |

---

## Повний приклад конфігурації

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "model": "sonnet",
  "language": "ukrainian",
  "cleanupPeriodDays": 30,
  "autoUpdatesChannel": "stable",
  "effortLevel": "medium",
  "permissions": {
    "allow": [
      "Edit(*)",
      "Bash(npm run *)",
      "Bash(git *)"
    ],
    "deny": [
      "Read(.env)"
    ],
    "defaultMode": "acceptEdits"
  },
  "sandbox": {
    "enabled": true,
    "excludedCommands": ["git"]
  },
  "attribution": {
    "commit": "Сгенеровано за допомогою Claude Code",
    "pr": ""
  }
}
```

---

*Довідник оновлюється разом із новими релізами Claude Code. Для отримання детальної інформації про кожен параметр звертайтеся до `/config` у терміналі.*

---

**Локалізація**: [Serhii (MacPlus Software)](https://macplus-software.com) | **Остання синхронізація**: Травень 2026
