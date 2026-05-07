}

exit 0
```

#### Шаблон W3: Збагачувач контексту (Batch-файл)

Створіть `.claude/hooks/git-context.cmd`:

```batch
@echo off
setlocal enabledelayedexpansion

for /f "tokens=*" %%i in ('git branch --show-current 2^>nul') do set BRANCH=%%i
if "%BRANCH%"=="" set BRANCH=not a git repo

for /f "tokens=*" %%i in ('git log -1 --format^="%%h %%s" 2^>nul') do set LAST_COMMIT=%%i
if "%LAST_COMMIT%"=="" set LAST_COMMIT=no commits

echo {"hookSpecificOutput":{"additionalContext":"[Git] Branch: %BRANCH% | Last: %LAST_COMMIT%"}}
exit /b 0
```

#### Шаблон W4: Сповіщення (Windows)

Створіть `.claude/hooks/notification.ps1`:

```powershell
# notification.ps1
# Показує спливаючі сповіщення Windows та відтворює звуки

$inputJson = [Console]::In.ReadToEnd() | ConvertFrom-Json
$title = $inputJson.title
$message = $inputJson.message

# Визначення звуку на основі вмісту
if ($title -match "error" -or $message -match "failed") {
    [System.Media.SystemSounds]::Hand.Play()
} elseif ($title -match "complete" -or $message -match "success") {
    [System.Media.SystemSounds]::Asterisk.Play()
} else {
    [System.Media.SystemSounds]::Beep.Play()
}

# Опціонально: Показувати Windows Toast Notification (потребує модуля BurntToast)
# Install-Module -Name BurntToast
# New-BurntToastNotification -Text $title, $body

exit 0
```

#### Windows settings.json для хуків

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash|Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "powershell -ExecutionPolicy Bypass -File .claude/hooks/security-check.ps1",
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
            "command": "powershell -ExecutionPolicy Bypass -File .claude/hooks/auto-format.ps1",
            "timeout": 10000
          }
        ]
      }
    ]
  }
}
```

## 7.4 Хуки безпеки (Security Hooks)

Хуки безпеки мають критичне значення для захисту вашої системи.

> **Просунуті патерни**: Для комплексного захисту, включаючи виявлення Unicode-ін'єкцій, верифікацію цілісності MCP-конфігів та пом'якшення CVE-ризиків, див. [Посібник із посилення безпеки](./security/security-hardening.md).

> **Claude Code Security (research preview)**: Anthropic пропонує спеціалізований сканер вразливостей кодобази, який відстежує потоки даних між файлами, внутрішньо перевіряє знахідки перед їх висвітленням (змагальна валідація) та генерує пропозиції виправлень. Окремо від Агента-аудитора безпеки вище — доступ тільки за списком очікування. Див. [Посібник із посилення безпеки → Claude Code як сканер безпеки](./security/security-hardening.md#claude-code-as-security-scanner-research-preview).
>
> **Валідовано масштабом**: У березні 2026 року в партнерстві з Mozilla, Claude Opus 4.6 просканував ~6000 файлів C++ у JS-рушії Firefox за два тижні, виявивши 22 підтверджені вразливості (14 високої критичності) — це приблизно одна п'ята частина всіх висококритичних CVE Firefox, виправлених у 2025 році. Це демонструє практичну глибину моделі для виробничих завдань безпеки, що виходить далеко за межі поверхневого лінтингу.

### Рекомендовані правила безпеки

```bash
#!/bin/bash
# .claude/hooks/comprehensive-security.sh

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // ""')

# === КРИТИЧНІ БЛОКУВАННЯ (Exit 2) ===

# Руйнування файлової системи
[[ "$COMMAND" =~ rm.*-rf.*[/~] ]] && { echo "BLOCKED: Рекурсивне видалення root/home" >&2; exit 2; }

# Дискові операції
[[ "$COMMAND" =~ ">/dev/sd" ]] && { echo "BLOCKED: Прямий запис на диск" >&2; exit 2; }
[[ "$COMMAND" =~ "dd if=" ]] && { echo "BLOCKED: Команда dd" >&2; exit 2; }

# Force-операції Git на захищених гілках
[[ "$COMMAND" =~ "git push".*"-f".*"(main|master)" ]] && { echo "BLOCKED: Force push у main" >&2; exit 2; }
[[ "$COMMAND" =~ "git push --force".*"(main|master)" ]] && { echo "BLOCKED: Force push у main" >&2; exit 2; }

# Публікація пакетів
[[ "$COMMAND" =~ "npm publish" ]] && { echo "BLOCKED: npm publish" >&2; exit 2; }

# Привілейовані операції
[[ "$COMMAND" =~ ^sudo ]] && { echo "BLOCKED: Команда sudo" >&2; exit 2; }

# === ПОПЕРЕДЖЕННЯ (Exit 0, але логувати) ===

[[ "$COMMAND" =~ "rm -rf" ]] && echo "WARNING: Виявлено рекурсивне видалення" >&2

exit 0
```

### Тестування хуків безпеки

Перед розгортанням протестуйте ваші хуки:

```bash
# Тест заблокованої команди
echo '{"tool_name":"Bash","tool_input":{"command":"rm -rf /"}}' | .claude/hooks/security-blocker.sh
echo "Код виходу: $?"  # Має бути 2

# Тест безпечної команди
echo '{"tool_name":"Bash","tool_input":{"command":"git status"}}' | .claude/hooks/security-blocker.sh
echo "Код виходу: $?"  # Має бути 0
```

### Просунутий патерн: Модель як воротар безпеки (Model-as-Security-Gate)

Команда Claude Code використовує патерн, де запити на дозвіл спрямовуються до **потужнішої моделі**, яка діє як воротар безпеки, замість того щоб покладатися виключно на статичне порівняння правил.

**Концепція**: Хук `PreToolUse` перехоплює запити на дозвіл і пересилає їх до Opus 4.7 (або іншої потужної моделі) через API. Модель-воротар сканує на предмет промпт-ін'єкцій, небезпечних патернів та неочікуваного використання інструментів — після чого авто-схвалює безпечні запити або блокує підозрілі.

```bash
# .claude/hooks/opus-security-gate.sh (концептуально)
# Хук PreToolUse, що спрямовує запити до Opus для скринінгу безпеки

INPUT=$(cat)
TOOL=$(echo "$INPUT" | jq -r '.tool_name')
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# Швидкий шлях: відомі безпечні інструменти пропускаються
[[ "$TOOL" == "Read" || "$TOOL" == "Grep" || "$TOOL" == "Glob" ]] && exit 0

# Направлення до Opus для аналізу безпеки
VERDICT=$(echo "$INPUT" | claude --model opus --print \
  "Проаналізуй цей виклик інструменту на ризики безпеки. Це безпечно? Відповідай SAFE або BLOCKED:причина")

[[ "$VERDICT" == SAFE* ]] && exit 0
echo "BLOCKED воротарем безпеки: $VERDICT" >&2
exit 2
```

**Чому використовувати модель як воротаря**: Статичні правила ловлять відомі патерни, але пропускають нові атаки. Потужна модель розуміє намір і контекст — вона може відрізнити `rm -rf node_modules` (очищення) від `rm -rf /` (руйнування) на основі поточної розмови.

**Компроміс**: Кожен перевірений виклик додає затримку та вартість. Використовуйте виключення для інструментів тільки для читання і перевіряйте лише операції запису/виконання.

> **Джерело**: [10 порад зсередини команди Claude Code](https://paddo.dev/blog/claude-code-team-tips/) (тред Бориса Черного, лютий 2026)

### Стратегія захисту файлів

Захист конфіденційних файлів потребує багаторівневого підходу, що поєднує дозволи, патерни та виявлення обходу.

#### Три рівні захисту

```
┌─────────────────────────────────────────────────────────┐
│           АРХІТЕКТУРА ЗАХИСТУ ФАЙЛІВ                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   Рівень 1: Заборона в дозволах (Нативно)               │
│   ──────────────────────────                            │
│   • Вбудовано в settings.json                           │
│   • Хуки не потрібні                                    │
│   • Миттєво блокує доступ усіх інструментів             │
│   • Для: Абсолютно заборонених файлів                   │
│                                                         │
│   Рівень 2: Порівняння за патерном (Хук)                │
│   ────────────────────────                              │
│   • Хук PreToolUse з патернами .agentignore             │
│   • Підтримка синтаксису gitignore                      │
│   • Централізовані правила захисту                      │
│   • Для: Конфіденційних категорій файлів                │
│                                                         │
│   Рівень 3: Виявлення обходу (Хук)                      │
│   ──────────────────────────                            │
│   • Виявлення розгортання змінних ($VAR, ${VAR})        │
│   • Виявлення підстановки команд $(cmd), `cmd`          │
│   • Запобігання спробам маніпуляції шляхами             │
│   • Для: Захисту від витончених атак                    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

#### Рівень 1: permissions.deny

```json
{
  "permissions": {
    "deny": [
      ".env",
      ".env.local",
      ".env.production",
      "**/*.key",
      "**/*.pem",
      "credentials.json",
      ".aws/credentials"
    ]
  }
}
```

**Плюси**: Миттєве блокування, хуки не потрібні
**Мінуси**: Немає кастомної логіки, неможливо логувати спроби

#### Рівень 2: Файл патернів .agentignore

Створіть `.agentignore` (або `.aiignore`) у корені проекту:

```gitignore
# Credentials
.env*
*.key
*.pem
*.p12
credentials.json
secrets.yaml

# Config
config/secrets/
.aws/credentials
.ssh/id_*

# Артефакти збірки (якщо генеровані з секретів)
dist/.env
build/config/production.json
```

**Уніфікований хук** (Див: `examples/hooks/bash/file-guard.sh`):

```bash
# .claude/hooks/file-guard.sh
# Читає .agentignore та блокує відповідні файли
# Також виявляє спроби обходу через bash
```

**Плюси**: Звичний синтаксис gitignore, централізовані правила, контроль версій
**Мінуси**: Потребує реалізації хука

#### Рівень 3: Виявлення обходу

Витончені атаки можуть намагатися обійти захист через розгортання змінних:

```bash
# Спроби атак
FILE="sensitive.key"
cat $FILE              # Обхід через розгортання змінної

HOME_DIR=$HOME
cat $HOME_DIR/.env     # Обхід через підстановку змінної

cat $(echo ".env")     # Обхід через підстановку команди
```

Хук `file-guard.sh` виявляє ці патерни:

```bash
# Логіка виявлення
detect_bypass() {
    local file="$1"

    # Розгортання змінних
    [[ "$file" =~ \$\{?[A-Za-z_][A-Za-z0-9_]*\}? ]] && return 0

    # Підстановка команд
    [[ "$file" =~ \$\( || "$file" =~ \` ]] && return 0

    return 1
}
```

#### Повний приклад захисту

**1. Налаштуйте settings.json**:

```json
{
  "permissions": {
    "deny": [".env", "*.key", "*.pem"]
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Read|Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/file-guard.sh",
            "timeout": 2000
          }
        ]
      }
    ]
  }
}
```

**2. Створіть .agentignore**:

```gitignore
.env*
config/secrets/
**/*.key
**/*.pem
credentials.json
```

**3. Скопіюйте шаблон хука**:

```bash
cp examples/hooks/bash/file-guard.sh .claude/hooks/
chmod +x .claude/hooks/file-guard.sh
```

#### Тестування захисту

```bash
# Тест прямого доступу
echo '{"tool_name":"Read","tool_input":{"file_path":".env"}}' | \
  .claude/hooks/file-guard.sh
# Має вийти з кодом 1 і показати "File access blocked"

# Тест спроби обходу
echo '{"tool_name":"Read","tool_input":{"file_path":"$HOME/.env"}}' | \
  .claude/hooks/file-guard.sh
# Має вийти з кодом 1 і показати "Variable expansion detected"
```

> **Перехресне посилання**: Для повного посилення безпеки, включаючи пом'якшення CVE та цілісність MCP-конфігів, див. [Посібник із посилення безпеки](./security/security-hardening.md).

## 7.5 Приклади хуків

### Розумна диспетчеризація хуків (Smart Hook Dispatching)

Замість конфігурації десятків окремих хуків використовуйте **єдиний диспетчер**, який інтелектуально спрямовує події на основі типу файлу, інструменту та контексту.

**Проблема**: У міру зростання колекції хуків `settings.json` стає громіздким через повторювані матчери та накладання конфігурацій.

**Рішення**: Одна точка входу, яка делегує роботу спеціалізованим обробникам.

```bash
#!/bin/bash
# .claude/hooks/dispatch.sh
# Єдина точка входу для всіх хуків PostToolUse
# Спрямовує до спеціалізованих обробників на основі типу файлу та інструменту

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name')
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.command // ""')
EVENT=$(echo "$INPUT" | jq -r '.hook_event_name // "unknown"')

HOOKS_DIR="$(dirname "$0")/handlers"

# Маршрутизація за розширенням файлу
case "$FILE_PATH" in
    *.ts|*.tsx)
        [[ -x "$HOOKS_DIR/typescript.sh" ]] && echo "$INPUT" | "$HOOKS_DIR/typescript.sh"
        ;;
    *.py)
        [[ -x "$HOOKS_DIR/python.sh" ]] && echo "$INPUT" | "$HOOKS_DIR/python.sh"
        ;;
    *.rs)
        [[ -x "$HOOKS_DIR/rust.sh" ]] && echo "$INPUT" | "$HOOKS_DIR/rust.sh"
        ;;
    *.sql|*.prisma)
        [[ -x "$HOOKS_DIR/database.sh" ]] && echo "$INPUT" | "$HOOKS_DIR/database.sh"
        ;;
esac

# Маршрутизація за інструментом (запускається завжди, незалежно від типу файлу)
case "$TOOL_NAME" in
    Bash)
        [[ -x "$HOOKS_DIR/security.sh" ]] && echo "$INPUT" | "$HOOKS_DIR/security.sh"
        ;;
    Write)
        [[ -x "$HOOKS_DIR/new-file.sh" ]] && echo "$INPUT" | "$HOOKS_DIR/new-file.sh"
        ;;
esac

exit 0
```

**Конфігурація** (мінімальний `settings.json`):

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|Write|Bash",
      "hooks": [{
        "type": "command",
        "command": ".claude/hooks/dispatch.sh"
      }]
    }]
  }
}
```

**Структура директорії обробників**:

```
.claude/hooks/
├── dispatch.sh              # Єдина точка входу
└── handlers/
    ├── typescript.sh         # ESLint + tsc для .ts/.tsx
    ├── python.sh             # Ruff + mypy для .py
    ├── rust.sh               # cargo clippy для .rs
    ├── database.sh           # Валідація схеми для .sql/.prisma
    ├── security.sh           # Блокування небезпечних bash-команд
    └── new-file.sh           # Перевірка конвенцій іменування при Write
```

**Переваги перед індивідуальними хуками**:
- **Один матчер** у settings.json (замість N)
- **Легке розширення**: просто додайте новий обробник у `handlers/`, конфіг змінювати не потрібно
- **Обізнаність про мову**: різна вадідація для різних типів файлів
- **Композиційність**: хуки за типом файлу та за інструментом запускаються одночасно, коли це доречно
- **Зручність дебагу**: `echo "$INPUT" | .claude/hooks/dispatch.sh` тестує весь ланцюжок

### Приклад 1: Логер активності (Activity Logger)

```bash
#!/bin/bash
# .claude/hooks/activity-logger.sh
# Логує використання всіх інструментів у файл JSONL

INPUT=$(cat)
LOG_DIR="$HOME/.claude/logs"
LOG_FILE="$LOG_DIR/activity-$(date +%Y-%m-%d).jsonl"

# Створення директорії логів
mkdir -p "$LOG_DIR"

# Очищення старих логів (зберігати 7 днів)
find "$LOG_DIR" -name "activity-*.jsonl" -mtime +7 -delete

# Витяг інформації про інструмент
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name')
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id')

# Створення запису логу
LOG_ENTRY=$(jq -n \
  --arg timestamp "$TIMESTAMP" \
  --arg tool "$TOOL_NAME" \
  --arg session "$SESSION_ID" \
  '{timestamp: $timestamp, tool: $tool, session: $session}')

# Додавання до логу
echo "$LOG_ENTRY" >> "$LOG_FILE"

exit 0
```

### Приклад 2: Ворота лінтингу (Linting Gate)

```bash
#!/bin/bash
# .claude/hooks/lint-gate.sh
# Запускає лінтер після зміни коду

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name')

# Перевірка тільки після Edit/Write
if [[ "$TOOL_NAME" != "Edit" && "$TOOL_NAME" != "Write" ]]; then
    exit 0
fi

FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // ""')

# Лінтинг тільки для TypeScript/JavaScript
if [[ ! "$FILE_PATH" =~ \.(ts|tsx|js|jsx)$ ]]; then
    exit 0
fi

# Запуск ESLint
LINT_OUTPUT=$(npx eslint "$FILE_PATH" 2>&1)
LINT_EXIT=$?

if [[ $LINT_EXIT -ne 0 ]]; then
    cat << EOF
{
  "systemMessage": "Виявлено помилки лінтингу в $FILE_PATH:\n$LINT_OUTPUT"
}
EOF
fi

exit 0
```

### Патерн "Конвеєр валідації" (Validation Pipeline Pattern)

З'єднайте кілька хуків валідації в ланцюжок, щоб ловити проблеми відразу після зміни коду. Цей патерн гарантує якість коду без ручного втручання.

#### Патерн

```
Edit/Write → TypeCheck → Lint → Tests → Повідомити Claude
    ↓            ↓         ↓       ↓
  file.ts    tsc check  eslint  jest file.test.ts
```

**Переваги**:
- Ловіть помилки негайно (до наступної дії Claude)
- Немає потреби вручну запускати `npm run typecheck && npm run lint && npm test`
- Швидка петля фідбеку → швидша ітерація
- Запобігає каскадним помилкам (Claude отримує сигнал про якість завчасно)

#### Конфігурація трирівневого конвеєра

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/typecheck-on-save.sh",
            "timeout": 5000
          },
          {
            "type": "command",
            "command": ".claude/hooks/lint-gate.sh",
            "timeout": 5000
          },
          {
            "type": "command",
            "command": ".claude/hooks/test-on-change.sh",
            "timeout": 10000
          }
        ]
      }
    ]
  }
}
```

**Порядок хуків має значення**: спочатку запускайте швидкі перевірки (typecheck ~1с), потім повільніші (тести ~3-5с).

#### Етап 1: Перевірка типів

Див: `examples/hooks/bash/typecheck-on-save.sh`

```bash
# Запускає tsc на файлах TypeScript після редагування
# Повідомляє тільки про помилки (не попередження)
# Таймаут: 5с (має бути швидким)
```

**Що він ловить**:
- Невідповідність типів
- Відсутні імпорти
- Неправильний доступ до властивостей
- Порушення обмежень generic-типів

#### Етап 2: Лінтинг

Вже описано в прикладі 2 вище (lint-gate.sh).

**Що він ловить**:
- Порушення стилю коду
- Невикористані змінні
- Відсутні крапки з комою
- Проблеми з порядком імпортів

#### Етап 3: Виконання тестів

Див: `examples/hooks/bash/test-on-change.sh`

```bash
# Виявляє відповідний файл тесту та запускає його
# Підтримка: Jest (.test.ts), Pytest (_test.py), Go (_test.go)
# Запускається тільки якщо файл тесту існує
```

**Логіка виявлення файлу тесту**:

| Вихідний файл | Патерни файлу тесту |
|-------------|-------------------|
| `auth.ts` | `auth.test.ts`, `__tests__/auth.test.ts` |
| `utils.py` | `utils_test.py`, `test_utils.py` |
| `main.go` | `main_test.go` |

#### Розумне виконання: Пропуск, якщо не релевантно

Всі три хуки перевіряють умови перед запуском:

```bash
# Тільки для Edit/Write
[[ "$TOOL_NAME" != "Edit" && "$TOOL_NAME" != "Write" ]] && exit 0

# Тільки для специфічних типів файлів
[[ ! "$FILE_PATH" =~ \.(ts|tsx|js|jsx)$ ]] && exit 0

# Тільки якщо існує конфіг
[[ ! -f "tsconfig.json" ]] && exit 0
```

Це запобігає марному виконанню при редагуванні README, зміні конфігів або не-кодових файлів.

#### Міркування щодо продуктивності

| Розмір проекту | Час конвеєра | Прийнятно? |
|--------------|---------------|-------------|
| Малий (<100 файлів) | ~1-2с на правку | ✅ Так |
| Середній (100-1000 файлів) | ~2-5с на правку | ✅ Так (з інкрементальністю) |
| Великий (1000+ файлів) | ~5-10с на правку | ⚠️ Розгляньте async або пропуск тестів |

**Стратегії оптимізації**:
1. Використовуйте `async: true` для лінтингу/форматування (косметичні перевірки)
2. Залишайте typecheck синхронним (помилки мають блокувати)
3. Пропускайте повний набір тестів, запускайте тільки тести зміненого файлу
4. Використовуйте інкрементальну компіляцію (`tsc --incremental`)

#### Приклад виводу (випадок помилки)

```
Користувач: Виправ логіку автентифікації
Claude: [Редагує auth.ts]

⚠ Помилки TypeScript у src/auth.ts:

src/auth.ts:45:12 - error TS2345: Argument of type 'string' is not assignable to parameter of type 'number'.

45   userId: user.id.toString(),
              ~~~~~~~~~~~~~~~~~~~

⚠ Тести провалені в src/__tests__/auth.test.ts:

FAIL src/__tests__/auth.test.ts
  ● Authentication › should validate user token
    Expected token to be valid

Виправ реалізацію або онови тести.
```

Claude бачить ці повідомлення миттєво і може ітерувати без ручного запуску тестів.

---

### Приклад 3: Хук підсумку сесії (Session Summary Hook)

**Подія**: `Stop`

Відображення вичерпної статистики сесії після завершення роботи Claude Code, натхненне функцією підсумку сесії в Gemini CLI.

#### Проблема

Після довгої сесії Claude Code ви можете запитати себе:
- Скільки часу я витратив?
- Скільки API-запитів зробив Claude?
- Якими інструментами я користувався найчастіше?
- Скільки коштувала ця сесія?

Без відстеження сесій ця інформація похована у файлах JSONL, які важко парсити вручну.

#### Рішення

Хук Stop, який автоматично виводить відформатований підсумок з:
- Метаданими сесії (ID, автозгенерована назва, гілка git)
- Розподілом тривалості (загальний час vs активний час Claude)
- Статистикою використання інструментів з кількістю успіхів/помилок
- Використанням моделей (запити, вхідні/вихідні токени, статистика кешу)
- Оціночною вартістю (через ccusage або вбудовану таблицю цін)

#### Реалізація

**Файл**: `examples/hooks/bash/session-summary.sh`

**Вимоги**:
- `jq` (необхідно для парсингу JSON)
- `ccusage` (опціонально, для точного розрахунку вартості)
- bash 3.2+ (сумісно з macOS)

**Встановлення плагіна (рекомендовано)**:

```bash
claude plugin marketplace add FlorianBruniaux/claude-code-plugins
claude plugin install session-summary@florian-claude-tools
```

Хуки автоматично підключаються до `SessionStart` (базовий рівень RTK) та `SessionEnd` (відображення підсумку). Ручна конфігурація не потрібна.

**Ручна конфігурація** (альтернатива):

```json
{
  "hooks": {
    "SessionEnd": [{
      "hooks": [{
        "type": "command",
        "command": "~/.claude/hooks/session-summary.sh"
      }]
    }]
  }
}
```

**Змінні оточення**:

| Змінна | За замовчуванням | Опис |
|----------|---------|-------------|
| `NO_COLOR` | - | Вимкнути кольори ANSI |
| `SESSION_SUMMARY_LOG` | `~/.claude/logs` | Перевизначити директорію логів |
| `SESSION_SUMMARY_SKIP` | `0` | Встановіть `1`, щоб вимкнути підсумок |

#### Приклад виводу

```
═══ Підсумок сесії ═══════════════════
ID:       abc-123-def-456
Назва:    Security hardening v3.26
Гілка:    main
Тривалість: Загальна 1г 34хв | Активна 14хв 24с

Виклики інструментів: 47 (OK 45 / ERR 2)
  Read: 12  Bash: 10  Edit: 8  Write: 6
  Grep: 5   Glob: 4   WebSearch: 2

Використання моделей   Запити    Вхідні    Вихідні
claude-sonnet-4-5     42   493.9K     2.5K
claude-haiku-4-5       5    12.4K       46

Кеш: 1.2M прочитано / 45.3K створено
Оціночна вартість: $0.74
═══════════════════════════════════════
```

#### Джерела даних

Хук витягує дані з двох місць:

**1. Файл JSONL сесії** (`~/.claude/projects/{encoded-path}/{session-id}.jsonl`):
- Кількість API-запитів
- Використання токенів на модель
- Виклики інструментів (витягнуті з повідомлень асистента)
- Помилки інструментів (з tool_result з is_error: true)
- Тривалість ходів (системні повідомлення з subtype: turn_duration)
- Загальний час (від першої до останньої мітки часу)

**2. Індекс сесій** (`~/.claude/projects/{encoded-path}/sessions-index.json`):
- Резюме сесії (автозгенероване Claude)
- Гілка Git
- Кількість повідомлень

#### Файл логу

Підсумки сесій також записуються у `~/.claude/logs/session-summaries.jsonl` для історичного аналізу:

```json
{
  "timestamp": "2026-02-13T10:30:00Z",
  "session_id": "abc-123-def",
  "session_name": "Security hardening v3.26",
  "git_branch": "main",
  "project": "/path/to/project",
  "duration_wall_ms": 5640000,
  "duration_active_ms": 864000,
  "api_requests": 47,
  "tool_calls": {"Read": 12, "Bash": 10, "Edit": 8},
  "tool_errors": 2,
  "models": {
    "claude-sonnet-4-5-20250929": {
      "requests": 42,
      "input": 493985,
      "output": 2505,
      "cache_read": 1200000,
