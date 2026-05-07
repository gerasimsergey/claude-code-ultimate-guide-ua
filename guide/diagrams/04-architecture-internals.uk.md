---
title: "Claude Code — Діаграми внутрішньої архітектури"
description: "Головний цикл, категорії інструментів, збірка системного промпту, ізоляція субагентів"
tags: [architecture, internals, master-loop, tools, ukrainian]
---

# Внутрішня архітектура

Що відбувається "під капотом" під час роботи Claude Code.

---

### Головний цикл (The Master Loop)

Ядро виконання Claude Code складається з двох вкладених циклів: **внутрішній цикл агента**, який продовжує викликати API, поки повертаються виклики інструментів, та **зовнішній цикл діалогу**, який починає новий хід, коли користувач відповідає.

```mermaid
flowchart TD
    A([Ввід користувача]) --> B(Збірка системного промпту<br/>+ контекст + інструменти)
    B --> C

    subgraph AGENT_LOOP["Цикл агента — повторюється до кінця викликів інструментів"]
        C{{Виклик Claude API}} --> D{Відповідь містить<br/>виклики інструментів?}
        D -->|Так| E(Паралельне виконання інструментів<br/>Glob, Grep, Bash...)
        E --> F(Додавання результатів<br/>до діалогу)
        F --> C
    end

    D -->|Ні| H(Вилучення текстової відповіді)
    H --> I([Показ користувачеві])
    I --> J{Користувач надсилає<br/>наступне повідомлення?}
    J -->|Так| B
    J -->|Ні| K([Кінець сесії])

    style A fill:#F5E6D3,color:#333
    style C fill:#E87E2F,color:#fff
    style D fill:#E87E2F,color:#fff
    style E fill:#6DB3F2,color:#fff
    style F fill:#6DB3F2,color:#fff
    style I fill:#7BC47F,color:#333
    style J fill:#E87E2F,color:#fff
    style K fill:#B8B8B8,color:#333

    click B href "../core/architecture.uk.md#1-головний-цикл" "Збірка системного промпту"
    click C href "../core/architecture.uk.md#1-головний-цикл" "Виклик Claude API"
    click E href "../core/architecture.uk.md#2-арсенал-інструментів" "Виконання інструментів"
```

<details>
<summary>ASCII версія</summary>

```
Ввід користувача
     │
Збірка промпту (система + контекст + інструменти)
     │
 ┌── Цикл агента ─────────────────────┐
  │ Claude API ◄────────────────────┐  │
  │      │                          │  │
  │ Виклики інструментів?           │  │
  │  ├─ Так → Виконати інструменти ─┘  │
  │  └─ Ні  → вихід з циклу            │
  └────────────────────────────────────┘
                │
         Показ відповіді
                │
         Наступне повід.? ──► Так → збірка промпту → цикл
                └─ Ні → Кінець сесії
```

</details>

---

### Категорії інструментів та їх вибір

Claude Code має 6 категорій інструментів, кожна з яких оптимізована для різних операцій.

```mermaid
flowchart TD
    ROOT["Інструменти Claude Code"] --> READ
    ROOT --> WRITE
    ROOT --> EXECUTE
    ROOT --> WEB
    ROOT --> WORKFLOW
    ROOT --> CONTROL

    subgraph READ["📖 Читання"]
        R1[Glob<br/>Пошук файлів за паттерном]
        R2[Grep<br/>Пошук вмісту файлів]
        R3[Read<br/>Читання вмісту файлу]
        R4[LS<br/>Список файлів у папці]
    end

    subgraph WRITE["✏️ Запис"]
        W1[Write<br/>Створення нового файлу]
        W2[Edit<br/>Редагування існуючого файлу]
        W3[MultiEdit<br/>Пакетне редагування]
    end

    subgraph EXECUTE["⚙️ Виконання"]
        E1[Bash<br/>Shell команди]
        E2[Task<br/>Запуск субагента]
    end

    subgraph WEB["🌐 Веб"]
        WB1[WebSearch<br/>Пошук у вебі]
        WB2[WebFetch<br/>Отримання вмісту URL]
    end

    subgraph WORKFLOW["📋 Робочі процеси"]
        WF1[TodoWrite<br/>Управління списком завдань]
        WF2[NotebookEdit<br/>Jupyter блокноти]
    end

    subgraph CONTROL["🎛️ Управління"]
        CF1[EnterPlanMode / ExitPlanMode<br/>Режим планування]
        CF2[EnterWorktree / ExitWorktree<br/>Навігація по worktree]
        CF3[AskUserQuestion<br/>Запитання до людини]
    end

    style ROOT fill:#E87E2F,color:#fff
    style R1 fill:#6DB3F2,color:#fff
    style E1 fill:#E85D5D,color:#fff
    style E2 fill:#E87E2F,color:#fff
    style WB1 fill:#7BC47F,color:#333

    click ROOT href "../core/architecture.uk.md#2-арсенал-інструментів" "Інструменти Claude Code"
```

<details>
<summary>ASCII версія</summary>

```
ЧИТАННЯ:  Glob, Grep, Read, LS
ЗАПИС:    Write, Edit, MultiEdit
ВИКОНАННЯ: Bash (shell), Task (субагент) ← найпотужніші/ризиковані
ВЕБ:      WebSearch, WebFetch
ПРОЦЕСИ:  TodoWrite, NotebookEdit
УПРАВЛІННЯ: Режими Plan, Worktree, AskUserQuestion
```

</details>

---

### Збірка системного промпту

Перед кожним викликом API Claude Code збирає системний промпт із декількох джерел.

```mermaid
sequenceDiagram
    participant CC as Claude Code
    participant G as Глобальний CLAUDE.md
    participant P as Проектний CLAUDE.md
    participant T as Реєстр інструментів
    participant A as Claude API

    Note over CC: СТАТИЧНА зона (кешується глобально)
    CC->>CC: 1. Базові інструкції + правила безпеки
    CC->>G: 2. Читання ~/.claude/CLAUDE.md
    G->>CC: Глобальні преференції
    CC->>P: 3. Читання проектного CLAUDE.md
    P->>CC: Конвенції проекту
    CC->>T: 4. Отримання списку інструментів
    T->>CC: Схеми інструментів (Glob, Grep, Bash...)
    Note over CC: ── РОЗДІЛЬНИЙ МАРКЕР ──────────────────────────
    Note over CC: ДИНАМІЧНА зона (кешується для сесії)
    CC->>CC: 5. Додавання робочої папки + git info
    CC->>CC: 6. Можливості MCP серверів (не кешується)
    CC->>CC: 7. Пам'ять (MEMORY.md), мова, вказівки
    CC->>A: Системний промпт (зібраний)<br/>+ повідомлення користувача
    Note over A: Один великий виклик із<br/>усім вбудованим контекстом
```

---

### Ізоляція контексту субагентів

Субагенти повністю ізольовані від батьківського процесу — вони не можуть читати історію діалогу батька або змінювати його стан.

```mermaid
sequenceDiagram
    participant P as Батьківський Claude
    participant T as Інструмент Task
    participant S as Субагент
    participant EXT as Зовнішні сервіси

    Note over P: Має повну історію діалогу
    P->>T: Task(промпт="зроби X", інструменти=[Read,Write,Bash])
    Note over T: Створює новий екземпляр Claude
    T->>S: spawn(тільки промпт + дозволи на інструменти)
    Note over S: НЕ отримує:<br/>- Діалог батька<br/>- Результати інструментів батька<br/>- Стан батька

    S->>EXT: читання файлів, bash, web (якщо дозволено)
    EXT->>S: Результати

    Note over S: Незалежне міркування<br/>з обмеженим контекстом

    S->>T: повертає "завдання виконано: деталі..."
    Note over T: Тільки текст передається назад
    T->>P: Рядок результату
    Note over P: Батько отримує тільки текст<br/>Немає спільного стану
```

---

**Локалізація**: [Serhii (MacPlus Software)](https://macplus-software.com)
*Остання синхронізація: Травень 2026*
