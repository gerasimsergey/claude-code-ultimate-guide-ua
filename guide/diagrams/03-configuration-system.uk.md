---
title: "Claude Code — Діаграми системи конфігурації"
description: "Пріоритетність конфігурацій, скіли vs команди vs агенти, життєвий цикл агента, пайплайн хуків"
tags: [configuration, hooks, agents, skills, commands, ukrainian]
---

# Система конфігурації

Як Claude Code завантажує налаштування, вирішує конфлікти та організовує розширюваність.

---

### Пріоритетність конфігурацій (5 рівнів)

Claude Code вирішує конфлікти налаштувань через сувору ієрархію пріоритетів. Вищі рівні перезаписують нижчі.

```mermaid
flowchart TD
    A["1️⃣ CLI Прапорці<br/>--model, --dangerously-skip-permissions<br/>--max-turns, --system-prompt"] --> B["2️⃣ Змінні оточення<br/>ANTHROPIC_API_KEY<br/>CLAUDE_MODEL, CLAUDE_CONFIG"]
    B --> C["3️⃣ Конфігурація проекту<br/>.claude/settings.json<br/>.claude/settings.local.json"]
    C --> D["4️⃣ Глобальна конфігурація<br/>~/.claude/settings.json<br/>~/.claude/CLAUDE.md"]
    D --> E["5️⃣ Вбудовані значення за замовчуванням<br/>Зашиті в бінарний файл Claude Code"]

    A1["Найвищий пріоритет<br/>Перезаписує все<br/>Для: автоматизації, CI/CD"] --> A
    E1["Найнижчий пріоритет<br/>Резервні значення<br/>Базова поведінка"] --> E

    style A fill:#E87E2F,color:#fff
    style B fill:#6DB3F2,color:#fff
    style C fill:#6DB3F2,color:#fff
    style D fill:#F5E6D3,color:#333
    style E fill:#B8B8B8,color:#333

    click A href "../ultimate-guide.uk.md#34-правила-пріоритетності" "CLI Прапорці — найвищий пріоритет"
    click B href "../ultimate-guide.uk.md#33-налаштування-та-дозволи" "Змінні оточення"
    click C href "../ultimate-guide.uk.md#33-налаштування-та-дозволи" "Конфігурація проекту"
    click D href "../ultimate-guide.uk.md#31-файли-пам'яті-claudemd" "Глобальна конфігурація"
```

<details>
<summary>ASCII версія</summary>

```
ПРІОРИТЕТ (від найвищого до найнижчого)
═══════════════════════════
1. CLI Прапорці         ← --model, --system-prompt
2. Змінні оточення      ← ANTHROPIC_API_KEY
3. Проект .claude/      ← settings.json, settings.local.json
4. Глобальна ~/.claude/ ← settings.json, CLAUDE.md
5. Вбудовані значення   ← зашиті в код
```

</details>

---

### Скіли vs Команди vs Агенти — коли що використовувати

Три механізми розширення з різними цілями та компромісами.

```mermaid
flowchart LR
    subgraph SKILLS["📦 Скіли (.claude/skills/)"]
        S1[Пакет можливостей<br/>з ресурсами]
        S2[Виклик через /skillname]
        S3[Переносні між проектами]
        S4["Для: багаторазових<br/>функцій між проектами"]
    end

    subgraph COMMANDS["⚡ Команди (.claude/commands/)"]
        C1[Простий шаблон<br/>або скрипт]
        C2[Команда для проекту]
        C3[Тільки для цього проекту]
        C4["Для: автоматизації проекту,<br/>швидких клавіш"]
    end

    subgraph AGENTS["🤖 Агенти (.claude/agents/)"]
        A1[Повністю автономний агент]
        A2[Власні інструменти та CLAUDE.md]
        A3[Запуск через інструмент Task]
        A4["Для: складних<br/>делегованих завдань"]
    end

    Q{Що ви<br/>будуєте?} --> |Багаторазова функція| SKILLS
    Q --> |Швидкий шлях проекту| COMMANDS
    Q --> |Складне підзавдання| AGENTS

    style S1 fill:#6DB3F2,color:#fff
    style S4 fill:#7BC47F,color:#333
    style C1 fill:#F5E6D3,color:#333
    style C4 fill:#7BC47F,color:#333
    style A1 fill:#E87E2F,color:#fff
    style A4 fill:#7BC47F,color:#333
    style Q fill:#E87E2F,color:#fff

    click S1 href "../ultimate-guide.uk.md#51-розуміння-скілів" "Скіли: пакет можливостей"
    click C1 href "../ultimate-guide.uk.md#62-створення-кастомних-команд" "Команди: простий шаблон"
    click A1 href "../ultimate-guide.uk.md#41-що-таке-агенти" "Агенти: автономність"
```

<details>
<summary>ASCII версія</summary>

```
                    Скіли               Команди            Агенти
Розташування:  .claude/skills/     .claude/commands/  .claude/agents/
Тригер:        /skillname          /commandname       Інструмент Task
Масштаб:       Міжпроекти          Цей проект         Будь-який контекст
Складність:    Середня (пакет)     Низька (шаблон)    Висока (автономія)
Коли:          Багат. функції      Швидкі команди     Складні завдання
```

</details>

---

### Життєвий цикл агента та ізоляція контексту

Субагенти працюють у повній ізоляції від батьківського процесу. Вони отримують копію контексту, але не ділять стан.

```mermaid
sequenceDiagram
    participant P as Батьківський Claude
    participant T as Інструмент Task
    participant S as Субагент
    participant FS as Файлова система

    P->>T: Task(промпт, дозволені_інструменти)
    T->>S: Створення нового екземпляра Claude
    Note over S: Отримує: промпт + дозволи<br/>НЕ отримує: історію батька

    S->>FS: Читання файлів (якщо дозволено)
    S->>FS: Редагування файлів (якщо дозволено)
    S->>S: Незалежне міркування

    Note over S,FS: Повністю ізольоване виконання
    Note over S: Немає доступу до стану батька

    S->>T: Повертає: тільки текстовий результат
    T->>P: Рядок результату
    P->>P: Продовжує з результатом

    Note over P,T: Батько бачить тільки фінальний текст<br/>Побічні ефекти не передаються назад
```

---

### Пайплайн подій Хуків (Hooks)

Хуки дозволяють запускати ваш код у ключові моменти життєвого циклу Claude Code — для сканування безпеки, логування або сповіщень.

```mermaid
flowchart TD
    INIT([Початок сесії]) -.->|v2.1.69+| INST{InstructionsLoaded Hook}
    INST -.-> A

    A([Повідомлення користувача]) --> UPS{UserPromptSubmit Hook}
    UPS -->|Exit 0: продовжити| B{PreToolUse Hook}
    UPS -->|Exit 2: фідбек| A
    B -->|Exit 0: дозволити| C[Інструмент виконується]
    B -->|Exit 1: блок| D([Блокування<br/>Claude зупиняється])
    C --> E{PostToolUse Hook}
    E --> F[Наступний інструмент або відповідь]
    F --> G{Ще виклики?}
    G -->|Так| B
    G -->|Ні| H([Кінець сесії])
    H --> I{Stop / SessionEnd Hook}
    I --> J([Завершено])

    K{PreCompact Hook} -.->|Перед /compact| L[/compact запускається]
    L --> M{PostCompact Hook}

    style INST fill:#6DB3F2,color:#fff
    style UPS fill:#6DB3F2,color:#fff
    style B fill:#E87E2F,color:#fff
    style D fill:#E85D5D,color:#fff
    style E fill:#E87E2F,color:#fff
    style I fill:#E87E2F,color:#fff
    style K fill:#6DB3F2,color:#fff
    style M fill:#6DB3F2,color:#fff
    style C fill:#7BC47F,color:#333
    style J fill:#7BC47F,color:#333

    click INIT href "../ultimate-guide.uk.md#71-система-подій" "Початок сесії"
    click B href "../ultimate-guide.uk.md#71-система-подій" "PreToolUse Hook"
    click C href "../core/architecture.uk.md#2-арсенал-інструментів" "Інструмент виконується"
    click D href "../ultimate-guide.uk.md#71-система-подій" "Інструмент заблоковано"
```

<details>
<summary>ASCII версія</summary>

```
Початок сесії
     │ (InstructionsLoaded Hook)
Повідомлення
     │
 UserPromptSubmit ──exit 2──► фідбек Claude (цикл)
     │ exit 0
 PreToolUse ──exit 1──► ЗАБЛОКОВАНО
     │ exit 0
     ▼
Інструмент виконується
     │
PostToolUse
     │
Ще інструменти? ──так──► PreToolUse (цикл)
     │ ні
Кінець сесії
     │
 Stop / SessionEnd Hook
     │
 Завершено
```

</details>

---

**Локалізація**: [Serhii (MacPlus Software)](https://macplus-software.com)
*Остання синхронізація: Травень 2026*
