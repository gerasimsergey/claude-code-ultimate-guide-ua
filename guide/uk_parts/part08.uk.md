ln -s ~/.claude/skills ./skills

# 3. Скопіюйте шаблон налаштувань (без секретів)
cp ~/.claude/settings.json ./settings.template.json
# Вручну замініть секрети на плейсхолдери ${VAR_NAME}

# 4. .gitignore для секретів
cat > .gitignore << EOF
# Ніколи не комітьте ці файли
.env
settings.json           # Містить розкриті секрети
mcp.json               # Містить API-ключі
*.local.json

# Історія сесій (велика, особиста)
projects/
EOF

# 5. Зробіть коміт та пуш у приватний репозиторій
git add .
git commit -m "Initial Claude Code global config backup"
git remote add origin git@github.com:yourusername/claude-config-private.git
git push -u origin main
```

**Чому симлінки?**
- Зміни в `~/.claude/agents/` миттєво відображаються в Git-репозиторії
- Не потрібно синхронізувати вручну
- Працює на macOS/Linux (на Windows: використовуйте junction points)

#### Стратегії резервного копіювання

| Стратегія | Плюси | Мінуси | Кейс використання |
|----------|------|------|----------|
| **Git remote (приватний)** | Повна історія версій, гілки | Потребує знання Git | Розробники, досвідчені користувачі |
| **Cloud sync (Dropbox/iCloud)** | Автоматично, між пристроями | Немає історії версій, конфлікти синхронізації | Одноосібні користувачі, просте налаштування |
| **Cron скрипт бекапу** | Автоматизовано, з мітками часу | Немає синхронізації між машинами | Тільки для відновлення після збоїв |
| **Сторонні інструменти** | `claudebot backup --config` | Залежність від зовнішнього інструменту | Швидке налаштування |

**Приклад: Автоматизований бекап за допомогою cron**:

```bash
# ~/claude-config-backup/backup.sh
#!/bin/bash
BACKUP_DIR=~/claude-backups
DATE=$(date +%Y-%m-%d_%H-%M-%S)

# Створення бекапу з міткою часу
mkdir -p "$BACKUP_DIR"
tar -czf "$BACKUP_DIR/claude-config-$DATE.tar.gz" \
    ~/.claude/agents \
    ~/.claude/commands \
    ~/.claude/hooks \
    ~/.claude/skills \
    ~/.claude/settings.json

# Зберігати тільки за останні 30 днів
find "$BACKUP_DIR" -name "claude-config-*.tar.gz" -mtime +30 -delete

echo "Backup created: $BACKUP_DIR/claude-config-$DATE.tar.gz"
```

Планування через cron:
```bash
# Щоденний бекап о 2 годині ночі
crontab -e
0 2 * * * ~/claude-config-backup/backup.sh >> ~/claude-backups/backup.log 2>&1
```

#### Синхронізація між кількома машинами

**Сценарій**: Ноутбук + десктоп, потрібен однаковий досвід роботи з Claude Code.

**Варіант 1: Git + симлінки**

```bash
# Машина 1 (налаштування)
cd ~/claude-config-backup
git add agents/ commands/ hooks/ skills/
git commit -m "Add latest configs"
git push

# Машина 2 (синхронізація)
cd ~/claude-config-backup
git pull
# Симлінки автоматично синхронізують директорії ~/.claude/
```

**Варіант 2: Симлінки на хмарне сховище**

```bash
# Обидві машини
# 1. Перемістіть ~/.claude/ у Dropbox
mv ~/.claude ~/Dropbox/claude-config

# 2. Створіть симлінк назад
ln -s ~/Dropbox/claude-config ~/.claude

# Зміни синхронізуються автоматично через Dropbox
```

**Варіант 3: Гібридний (Git для агентів/хуків, хмара для конфігів MCP)**

```bash
# Git для коду (агенти, хуки, скіли)
~/claude-config-backup/  → Git репозиторій

# Хмара для даних (налаштування, MCP, сесії)
~/Dropbox/claude-mcp/    → settings.json, mcp.json (зашифровані секрети)
ln -s ~/Dropbox/claude-mcp/settings.json ~/.claude/settings.json
```

#### Міркування щодо безпеки

**Ніколи не комітьте це в Git**:
- API-ключі, токени, паролі
- Файли `.env` із секретами
- `mcp.json` із розкритими обліковими даними
- Історію сесій (може містити конфіденційний код)

**Завжди комітьте це**:
- Файли шаблонів із плейсхолдерами `${VAR_NAME}`
- `.gitignore`, щоб запобігти витоку секретів
- Публічні агенти/хуки/скіли (якщо їх безпечно поширювати)

**Найкращі практики**:
1. Використовуйте `settings.template.json` з плейсхолдерами → Генеруйте `settings.json` через скрипт
2. Запускайте [pre-commit hook](../../examples/hooks/bash/pre-commit-secrets.sh) для виявлення секретів
3. Для секретів MCP див. [Розділ 8.3.1 Керування секретами MCP](#831-mcp-secrets-management)

#### Відновлення після збоїв

**Відновлення з Git-бекапу**:

```bash
# З Git-бекапу
cd ~/claude-config-backup
git clone git@github.com:yourusername/claude-config-private.git
cd claude-config-private

# Перестворіть симлінки
ln -sf ~/.claude/agents ./agents
ln -sf ~/.claude/commands ./commands
# ... і так далі

# Відновіть налаштування (заповніть секрети вручну або через .env)
cp settings.template.json ~/.claude/settings.json
# Відредагуйте та замініть ${VAR_NAME} на реальні значення
```

**Відновлення з архіву tarball**:
```bash
cd ~/claude-backups
# Знайдіть останній бекап
ls -lt claude-config-*.tar.gz | head -1

# Розархівуйте
tar -xzf claude-config-YYYY-MM-DD_HH-MM-SS.tar.gz -C ~/
```

#### Рішення спільноти

- **[brianlovin/claude-config](https://github.com/brianlovin/claude-config)**: Публічний репозиторій зі скриптом `sync.sh` для бекапу та відновлення
- **Підхід Martin Ratinaud**: Git репо + симлінки + `sync-mcp.sh` для секретів (перевірено на 504 сесіях)
- **Шаблон скрипта**: Див. [sync-claude-config.sh](../../examples/scripts/sync-claude-config.sh) для повної автоматизації

**GitHub Issue**: [#16204 - Proactive migration guidance for backup/restore workflows](https://github.com/anthropics/claude-code/issues/16204)

## 3.3 Налаштування та дозволи

### settings.json (Конфігурація команди)

Цей файл налаштовує хуки, дозволи, змінні оточення та інше. Файл `.claude/settings.json` на рівні проекту комітиться в репозиторій (спільний для команди). Доступні ключі включають: `hooks`, `env`, `allowedTools`, `autoApproveTools`, `dangerouslyAllowedPatterns`, `teammates`, `teammateMode`, `apiKeyHelper`, `spinnerVerbs`, `spinnerTipsOverride`, `plansDirectory`, `enableAllProjectMcpServers`.

**Приклад хуків** (найпоширеніше використання в `.claude/settings.json`):

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash|Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/security-check.sh",
            "timeout": 5000
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/auto-format.sh"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/git-context.sh"
          }
        ]
      }
    ]
  }
}
```

### settings.local.json (Особисті дозволи)

Особисті перевизначення дозволів (ігноруються Git):

```json
{
  "permissions": {
    "allow": [
      "Bash(git *)",
      "Bash(pnpm *)",
      "Bash(npm test)",
      "Edit",
      "Write",
      "WebSearch"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Bash(sudo *)"
    ],
    "ask": [
      "Bash(npm publish)",
      "Bash(git push --force)"
    ]
  }
}
```

### Налаштування персоналізації терміналу

Два параметри дозволяють налаштувати текст, який чергується в терміналі, поки агент працює ("Аналіз…", "Фокуси…", тощо).

**`spinnerVerbs`** — замінює або доповнює слова дій, що відображаються в спінері:

```json
{
  "spinnerVerbs": {
    "mode": "replace",
    "verbs": ["Хакінг…", "Заклинання…", "Глибокі роздуми…", "Заварювання кави…"]
  }
}
```

Використовуйте `"mode": "add"`, щоб доповнити стандартний список замість його заміни.

**`spinnerTipsOverride`** — налаштовує поради, що показуються в спінері. Використовуйте `excludeDefault: true`, щоб видалити всі вбудовані поради:

```json
{
  "spinnerTipsOverride": {
    "tips": ["Спробуй /compact, коли контекст заповнений", "Використовуй --print для CI-пайплайнів"],
    "excludeDefault": true
  }
}
```

Ці параметри вказуються в `~/.claude/settings.json` (особисті, не комітяться) або `.claude/settings.json` (спільні для команди). Нульова функціональна цінність — чиста персоналізація UX.

Повний приклад із 80+ порадами з посібника та кастомними дієсловами: [`examples/config/settings-personalization.json`](../examples/config/settings-personalization.json)

### Патерни дозволів

| Патерн | Відповідність |
|---------|---------|
| `Bash(git *)` | Будь-яка команда git |
| `Bash(pnpm *)` | Будь-яка команда pnpm |
| `Edit` | Усі редагування файлів |
| `Write` | Усі записи файлів |
| `WebSearch` | Можливість пошуку в мережі |
| `mcp__serena__*` | Усі інструменти Serena MCP |
| `mcp__github__create_issue` | Конкретний інструмент MCP (формат: `mcp__<сервер>__<інструмент>`) |
| `Read(file_path:*.env*)` | Читання файлів за маскою шляху (кваліфікований формат) |
| `Edit(file_path:*.pem)` | Редагування за маскою шляху (кваліфікований формат) |
| `Write(file_path:*.key)` | Запис за маскою шляху (кваліфікований формат) |

**Кваліфікований формат заборони (Tool-qualified deny)** — обмежте доступ до файлів за патерном шляху, а не лише за назвою інструмента:

```json
{
  "permissions": {
    "deny": [
      "Bash(command:*rm -rf*)",
      "Bash(command:*terraform destroy*)",
      "Read(file_path:*.env*)",
      "Read(file_path:*.pem)",
      "Read(file_path:*credentials*)",
      "Edit(file_path:*.env*)",
      "Edit(file_path:*.key)",
      "Write(file_path:*.env*)",
      "Write(file_path:*.key)"
    ]
  }
}
```

Префікс `file_path:` перевіряється на відповідність повному шляху, переданому в Read/Edit/Write. Використовуйте glob-патерни (`*`, `**`). Це набагато точніше, ніж проста форма рядка (наприклад, `".env"`), яка відповідає лише точному імені файлу.

> **Глибокий захист**: `permissions.deny` має відоме обмеження — фонова індексація може розкрити вміст файлів через системні нагадування ще до застосування перевірок дозволів ([GitHub #4160](https://github.com/anthropics/claude-code/issues/4160)). Зберігайте секрети поза директорією проекту для гарантованого захисту.

### Поведінка дозволів

| Категорія | Поведінка |
|----------|----------|
| `allow` | Автосхвалення без запиту |
| `deny` | Повне блокування |
| `ask` | Запит на підтвердження |
| (default) | Використання стандартного режиму дозволів |

### Конфігурація allowedTools / autoApproveTools

Для детального контролю в `~/.claude/settings.json` або `.claude/settings.json` доступні два формати.

**`autoApproveTools`** (формат масиву, простіший) автоматично схвалює перелічені інструменти без запитів.
**`allowedTools`** (формат об'єкта зі значеннями `true`/`false`) забезпечує точний контроль, включаючи явні заборони.

Приклад використання `autoApproveTools` у `~/.claude/settings.json`:

```json
{
  "allowedTools": [
    "Read",
    "Grep",
    "Glob",
    "WebFetch",
    "TodoRead",
    "TodoWrite",
    "Task",
    "Bash(git status *)",
    "Bash(git diff *)",
    "Bash(git log *)",
    "Bash(pnpm typecheck *)",
    "Bash(pnpm lint *)",
    "Bash(pnpm test *)"
  ]
}
```

**Логіка патернів**:
| Патерн | Значення | Приклад |
|---------|---------|---------|
| `Read` | Усі читання | Будь-який файл |
| `Bash(git status *)` | Конкретна команда | `git status` дозволено |
| `Bash(pnpm *)` | Префікс команди | `pnpm test`, `pnpm build` |
| `Edit` | Усі редагування | ⚠️ Небезпечно |

**Прогресивні рівні дозволів**:

**Рівень 1 - Початківець (дуже обмежений)**:
```json
{
  "autoApproveTools": ["Read", "Grep", "Glob"]
}
```

**Рівень 2 - Середній**:
```json
{
  "autoApproveTools": [
    "Read", "Grep", "Glob",
    "Bash(git *)", "Bash(pnpm *)"
  ]
}
```

**Рівень 3 - Просунутий**:
```json
{
  "autoApproveTools": [
    "Read", "Grep", "Glob", "WebFetch",
    "Edit", "Write",
    "Bash(git *)", "Bash(pnpm *)", "Bash(npm *)"
  ]
}
```

⚠️ **Ніколи не використовуйте `--dangerously-skip-permissions`**

Жахливі історії з r/ClaudeAI включають:
- `rm -rf node_modules` з подальшим `rm -rf .` (помилка шляху)
- Ненавмисний `git push --force` у main
- `DROP TABLE users` у погано згенерованій міграції
- Видалення файлів `.env` з обліковими даними

**Завжди надавайте перевагу точковим дозволам у `allowedTools` замість повного вимкнення перевірок.**

> **Безпечна альтернатива**: Для автономного виконання запускайте Claude Code всередині [Docker Sandboxes](sandbox-isolation.md) або подібного ізольованого середовища. Пісочниця стає межею безпеки, що робить використання `--dangerously-skip-permissions` безпечним. Див. [Посібник з ізоляції в пісочниці](sandbox-isolation.md) щодо налаштування та альтернатив.

### Динамічна пам'ять (Перемикання профілів)

**Концепція**: Тимчасово змінюйте CLAUDE.md для специфічних завдань, потім відновлюйте.

**Техніка 1: Git Stash**
```bash
# Перед зміною
git stash push -m "CLAUDE.md original" CLAUDE.md

# Claude змінює CLAUDE.md для конкретного завдання
# ... робота ...

# Після завдання
git stash pop
```

**Техніка 2: Бібліотека профілів**
```
~/.claude/profiles/
├── default.md          # Загальна конфігурація
├── security-audit.md   # Для аудитів безпеки
├── refactoring.md      # Для великих рефакторингів
├── documentation.md    # Для написання документації
└── debugging.md        # Для дебаг-сесій
```

**Скрипт перемикання профілів**:
```bash
#!/bin/bash
# ~/.local/bin/claude-profile

PROFILE=$1
cp ~/.claude/profiles/${PROFILE}.md ./CLAUDE.md
echo "Switched to profile: $PROFILE"
```

Використання:
```bash
claude-profile security-audit
claude  # Запускається з профілем безпеки
```

**Техніка 3: Паралельні інстанси**
```bash
# Термінал 1: Основний проект
cd ~/projects/myapp
claude  # Завантажує CLAUDE.md проекту myapp

# Термінал 2: Worktree для ізольованої фічі
cd ~/projects/myapp-feature-x
# Інший CLAUDE.md, ізольований контекст
claude
```

## 3.4 Правила пріоритетності

При виникненні конфліктів у файлах пам'яті або налаштуваннях, Claude Code використовує таку пріоритетність:

### Пріоритетність налаштувань

```
Найвищий пріоритет
       │
       ▼
┌──────────────────────────────────┐
│  settings.local.json             │  Особисті перевизначення
└──────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────┐
│  settings.json                   │  Налаштування проекту
└──────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────┐
│  ~/.claude/settings.json         │  Глобальні стандарти
└──────────────────────────────────┘
       │
       ▼
Найнижчий пріоритет
```

### Пріоритетність CLAUDE.md

```
Найвищий пріоритет
       │
       ▼
┌──────────────────────────────────┐
│  .claude/CLAUDE.md               │  Локальна (особиста)
└──────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────┐
│  /project/CLAUDE.md              │  Проектна (командна)
└──────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────┐
│  ~/.claude/CLAUDE.md             │  Глобальна (особиста)
└──────────────────────────────────┘
       │
       ▼
Найнижчий пріоритет
```

### Автоматичне завантаження правил

Файли в `.claude/rules/` завантажуються та об'єднуються автоматично:

```
.claude/rules/
├── code-conventions.md    ──┐
├── git-workflow.md        ──┼──→  Усі завантажуються на початку сесії
└── architecture.md        ──┘
```

### Порівняння завантаження пам'яті

Розуміння того, коли завантажується кожен метод пам'яті, є критичним для оптимізації токенів:

| Метод | Коли завантажується | Вартість у токенах | Кейс використання |
|--------|-------------|------------|----------|
| `CLAUDE.md` | Початок сесії | Завжди | Основний контекст проекту |
| `.claude/rules/*.md` | Початок сесії (УСІ файли) | Завжди | Конвенції, що діють завжди |
| `@шлях/до/файлу.md` | За запитом (при посиланні) | Тільки при використанні | Опціональний/умовний контекст |
| `.claude/commands/*.md` | Тільки при виклику | Тільки при виклику | Шаблони воркфлоу |
| `.claude/skills/*.md` | Тільки при виклику | Тільки при виклику | Модулі доменних знань |

**Ключовий інсайт**: Папка `.claude/rules/` НЕ працює "за запитом". Кожен файл `.md` у цій директорії завантажується на початку сесії, споживаючи токени. Резервуйте її для конвенцій, що актуальні завжди, а не для рідко використовуваних настанов. Скіли (skills) завантажуються тільки при виклику і можуть не спрацьовувати надійно — одне оцінювання показало, що агенти викликали скіли лише у 56% випадків ([Gao, 2026](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)). Ніколи не покладайтеся на скіли для критичних інструкцій; використовуйте замість них CLAUDE.md або правила.

> **Див. також**: [Оцінка вартості токенів](#token-saving-techniques) для приблизної вартості залежно від розміру файлу. Для єдиного довідника "який механізм для чого?" див. [§2.7 Посібник з прийняття рішень щодо конфігурації](#27-configuration-decision-guide).

### Правила для конкретних шляхів (грудень 2025)

Починаючи з грудня 2025 року, правила можуть бути спрямовані на конкретні шляхи до файлів за допомогою YAML frontmatter:

```markdown
---
globs: src/api/**/*.ts, lib/handlers/**/*.ts
---

# Конвенції API ендпоінтів

Ці правила застосовуються тільки при роботі з файлами API:

- Усі ендпоінти повинні мати OpenAPI документацію
- Використовуй zod для валідації запитів/відповідей
- Включай middleware для обмеження частоти запитів (rate limiting)
```

> **Попередження — синтаксис масиву `paths:` не працює.** Документоване поле `paths:` із YAML-масивом зламане через внутрішню помилку парсера CSV (`_9A()` отримує JS Array і ітерує символи рядкового представлення замість реальних патернів). Рядки в лапках під `paths:` мають ту саму проблему, зберігаючи лапки в паттерні glob. Це підтверджено у GitHub issue #17204 та 8 дублікатах звітів. Вихід — використовувати `globs:` з паттернами через кому без лапок. Жодних лапок, жодних YAML-масивів.

Це дозволяє впроваджувати прогресивне завантаження контексту: правила з'являються тільки тоді, коли Claude працює з відповідними файлами. Реальний приклад: компанія Avo перевела 600-рядковий CLAUDE.md на ~15 файлів з обмеженням за шляхами, повідомивши про більш точні відповіді та легше обслуговування різних доменів. ([Björn Jóhannsson](https://www.linkedin.com/posts/bj%C3%B6rn-j%C3%B3hannsson-72435083_your-claudemd-is-eating-your-context-window-activity-7431750526729338881-ODSs))

**Як працює відповідність (matching)**:
- Патерни використовують синтаксис glob (як у `.gitignore`)
- Кілька правил можуть відповідати одному файлу (завантажуються всі)
- Правила без frontmatter `globs:` завантажуються завжди

---

## 3.5 Конфігурація команди в масштабі

---

### 📌 Розділ 3.5 TL;DR (60 секунд)

**Проблема**: Файли інструкцій ШІ (CLAUDE.md, .cursorrules, AGENTS.md) фрагментуються між розробниками, інструментами та ОС — кожен девелопер отримує трохи іншу версію, і ніхто не знає, яка з них "правильна".

**Рішення**: Збірка модулів на основі профілів — виділіть багаторазові модулі, визначте профілі для кожного розробника в YAML, автоматично збирайте фінальний файл інструкцій.

**Виміряний результат**: Зменшення контексту токенів на 59% (з ~8,400 до ~3,450 токенів на зібраний файл). Виміряно в команді з 5 розробників, стек TypeScript/Node.js.

**Використовуйте, коли**: Команди від 3+ розробників використовують кілька інструментів ШІ (Claude Code, Cursor, Windsurf тощо)

**Пропустіть, якщо**: Один розробник або однорідна команда (один інструмент, одна ОС, однакові правила для всіх).

---

### Проблема фрагментації N×M×P

Коли ваша команда використовує інструменти кодування ШІ, файли інструкцій розмножуються швидко:

```
Розробники (N)  ×  Інструменти (M)  ×  ОС (P)     =  Фрагменти
─────────────     ───────────      ─────────     ──────────
5 розробників      3 інструменти    2 ОС          30 потенційних конфігів
                  (Claude Code,    (macOS,
                   Cursor,          Linux)
                   Windsurf)
```

На практиці це спричиняє реальні розбіжності:

- Аліса додає правила TypeScript strict-mode у свій CLAUDE.md. Боб їх ніколи не отримує.
- Керол налаштовує шляхи для macOS. Дейв на Linux копіює файл і отримує биті шляхи.
- Хтось оновлює розділ git-воркфлоу в одному файлі. Інші 4 файли залишаються застарілими.

Через 3 місяці у жодних двох розробників немає однакових інструкцій — і ніхто не знає, яка версія є "вірною".

### Рішення: Збірка модулів на основі профілів

Замість того, щоб підтримувати N окремих монолітних файлів, ви підтримуєте:
- **Модулі**: Невеликі тематичні файли інструкцій (багаторазові для всіх розробників)
- **Профілі**: Один YAML-файл на розробника, де вказано, які модулі йому потрібні
- **Скелет (Skeleton)**: Шаблон із плейсхолдерами, що заповнюється під час збірки
- **Збирач (Assembler)**: Скрипт, який читає профіль і видає фінальний файл

```
profiles/
├── alice.yaml      ──┐
├── bob.yaml        ──┤  Профілі розробників
└── carol.yaml      ──┘
        │
        ▼
modules/
├── core-standards.md    ──┐
├── typescript-rules.md  ──┤  Спільні модулі
├── git-workflow.md      ──┤
└── macos-paths.md       ──┘
        │
        ▼
skeleton/
└── claude.md            ─── Шаблон із {{PLACEHOLDERS}}
        │
        ▼
sync-ai-instructions.ts  ─── Скрипт-збирач
        │
        ▼
output/
├── alice/CLAUDE.md      ──┐
├── bob/CLAUDE.md        ──┤  Зібрано для кожного розробника
└── carol/CLAUDE.md      ──┘
```

**Одне оновлення модуля автоматично поширюється на всіх розробників.**

### Профіль YAML

Кожен розробник має профіль, що описує його оточення та модулі для включення:

```yaml
# profiles/alice.yaml
name: "Alice"
os: "macos"
tools:
  - claude-code
  - cursor
communication_style: "verbose"  # або "concise"
modules:
  core:
    - core-standards
    - git-workflow
    - typescript-rules
  conditional:
    - macos-paths        # включається, якщо os: macos
    - cursor-rules       # включається, якщо cursor в інструментах
preferences:
  language: "english"
  token_budget: "medium"  # low | medium | high
```

### Шаблон скелета (Skeleton)

Скелет — це Markdown-шаблон із плейсхолдерами. Збирач заповнює їх:

```markdown
# Інструкції ШІ - {{DEVELOPER_NAME}}
# Згенеровано: {{GENERATED_DATE}} | ОС: {{OS}} | Інструмент: {{TOOL}}
# НЕ РЕДАГУВАТИ - Автозгенеровано з профілю. Редагуйте профілі + модулі.

## Контекст проекту
{{MODULE:core-standards}}

## Git Воркфлоу
{{MODULE:git-workflow}}

{{#if typescript}}
## Правила TypeScript
{{MODULE:typescript-rules}}
{{/if}}

## Оточення
{{MODULE:{{OS}}-paths}}
```

Заголовок `НЕ РЕДАГУВАТИ` дуже важливий — він запобігає локальним змінам розробників, які будуть стерті при наступній збірці.

### Скрипт-збирач

Спрощений збирач на TypeScript (~30 рядків основної логіки):

```typescript
// sync-ai-instructions.ts (спрощено)
import { readFileSync, writeFileSync } from 'fs'
import { parse } from 'yaml'

interface Profile {
  name: string
  os: 'macos' | 'linux' | 'windows'
  tools: string[]
  modules: { core: string[]; conditional: string[] }
}

function assembleInstructions(profilePath: string, skeletonPath: string): string {
  const profile = parse(readFileSync(profilePath, 'utf-8')) as Profile
  let output = readFileSync(skeletonPath, 'utf-8')

  // Заміна плейсхолдерів
  output = output.replace('{{DEVELOPER_NAME}}', profile.name)
  output = output.replace('{{OS}}', profile.os)
  output = output.replace('{{GENERATED_DATE}}', new Date().toISOString())

  // Ін'єкція модулів
  const allModules = [
    ...profile.modules.core,
    ...profile.modules.conditional.filter(m => isApplicable(m, profile))
  ]

  for (const moduleName of allModules) {
    const content = readFileSync(`modules/${moduleName}.md`, 'utf-8')
    output = output.replace(`{{MODULE:${moduleName}}}`, content)
  }

  return output
}

function isApplicable(module: string, profile: Profile): boolean {
  if (module.endsWith('-paths')) return module.startsWith(profile.os)
  if (module === 'cursor-rules') return profile.tools.includes('cursor')
  return true
}

// Запуск для всіх профілів
const profiles = ['alice', 'bob', 'carol']
for (const dev of profiles) {
  const result = assembleInstructions(`profiles/${dev}.yaml`, 'skeleton/claude.md')
  writeFileSync(`output/${dev}/CLAUDE.md`, result)
  console.log(`Generated CLAUDE.md for ${dev}`)
}
```

Ви можете написати це на Python або bash — логіка та сама: прочитати профіль, завантажити модулі, замінити плейсхолдери, записати результат.

### Виміряні результати

Перевірено в команді з 5 розробників, стек TypeScript/Node.js (Метод Aristote):

| Метрика | Монолітний | На основі профілів | Зміна |
|--------|-----------|---------------|--------|
| Сер. розмір CLAUDE.md | 380 рядків | 185 рядків | -51% |
| Оціночна вартість токенів | ~8,400 токенів | ~3,450 токенів | **-59%** |
| Файлів для підтримки | 1 спільний файл | 12 модулів + 5 профілів | +16 файлів |
| Поширення оновлень | Ручний копіпаст | Автоматично (1 модуль → всі) | Автоматизовано |
| Виявлення розбіжностей | Немає | Щоденна перевірка CI | Автоматизовано |

Оцінка токенів базується на середньому значенні ~22 токени на рядок. Зменшення на 59% відбувається завдяки тому, що кожен розробник завантажує тільки ті модулі, які йому дійсно потрібні, замість повного монолітного файлу з розділами, нерелевантними для його налаштувань.

### Виявлення розбіжностей через CI

Додайте щоденну перевірку, щоб виявити, коли зібраний результат відрізняється від того, що згенерували б профілі:

```yaml
# .github/workflows/ai-instructions-sync.yml
name: Check AI Instructions Sync
on:
  schedule:
    - cron: '0 8 * * *'  # Щодня о 8 ранку
  push:
    paths: ['profiles/**', 'modules/**', 'skeleton/**']

jobs:
  check-sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npx ts-node sync-ai-instructions.ts --dry-run --check
      - name: Fail if drift detected
        run: |
          git diff --exit-code output/ || \
            (echo "AI instructions out of sync. Run sync-ai-instructions.ts" && exit 1)
```

Це виявляє два сценарії:
1. Хтось відредагував модуль, але забув перезапустити збирач
2. Хтось вручну відредагував вихідний файл замість модуля

### Посібник із реплікації у 5 кроків

1. **Аудит**: Випишіть усе, що є у вашому поточному CLAUDE.md. Позначте кожен рядок як `universal` (стосується всіх), `conditional` (залежить від інструмента/ОС/ролі) або `personal` (тільки один розробник).

2. **Вилучення**: Перемістіть кожну категорію в окремий файл у `modules/`. Один файл на тему (наприклад, `git-workflow.md`, `typescript-rules.md`, `macos-paths.md`).

3. **Профілі**: Створіть один YAML-файл на розробника, вказавши, які модулі йому потрібні залежно від його інструментів, ОС та ролі.

4. **Скрипт**: Напишіть збирач, який читає профілі, вставляє модулі в скелет і записує результат. Почніть з простого — приклад вище готовий до роботи в невеликих командах.
**Локалізація**: [Serhii (MacPlus Software)](https://macplus-software.com)
*Остання синхронізація: Травень 2026*
