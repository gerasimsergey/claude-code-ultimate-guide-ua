**Плюси**: Простота, кросплатформеність, легкий онбординг.
**Мінуси**: Відкритий текст на диску (тільки права доступу до файлу), вимагає дисципліни.

**Налаштування**:

```bash
# 1. Створіть файл .env (у корені проекту або ~/.claude/)
cat > ~/.claude/.env << EOF
GITHUB_TOKEN=ghp_your_token_here
OPENAI_API_KEY=sk-your-key-here
DATABASE_URL=postgresql://user:pass@localhost/db
EOF

# 2. Налаштуйте права доступу (тільки для Unix)
chmod 600 ~/.claude/.env

# 3. Додайте до .gitignore
echo ".env" >> ~/.claude/.gitignore
```

**Конфігурація MCP зі змінними .env**:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@github/mcp-server"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "${DATABASE_URL}"
      }
    }
  }
}
```

**Завантаження .env перед запуском Claude Code**:

```bash
# Варіант 1: Оболонка-обгортка
# ~/bin/claude-with-env
#!/bin/bash
export $(cat ~/.claude/.env | xargs)
claude "$@"

# Варіант 2: direnv (автоматично для директорії)
# Встановлення: https://direnv.net/
echo 'dotenv ~/.claude/.env' > ~/.config/direnv/direnvrc
direnv allow ~/.claude
```

**Шаблонний підхід для команд**:

```bash
# Комітьте шаблон (без секретів)
cat > ~/.claude/mcp-config.template.json << EOF
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@github/mcp-server"],
      "env": {
        "GITHUB_TOKEN": "\${GITHUB_TOKEN}"
      }
    }
  }
}
EOF

# Генерація реального конфігу з шаблону + .env
envsubst < ~/.claude/mcp-config.template.json > ~/.claude.json

# .gitignore
.claude.json  # Згенерований файл, містить розкриті секрети
.env          # Ніколи не комітити
```

**Дивіться також**: [sync-claude-config.sh](../../examples/scripts/sync-claude-config.sh) для автоматизованої підстановки шаблонів.

---

#### Підхід 3: Секретні сховища (Enterprise)

**Найкраще для**: Великих компаній, комплаєнсу (SOC 2, HIPAA), централізованого управління секретами.

**Плюси**: Централізація, аудит, автоматична ротація, тонке управління доступом.
**Мінуси**: Складне налаштування, потребує інфраструктури, прив'язка до вендора.

**HashiCorp Vault**:

```bash
# Зберегти секрет у Vault
vault kv put secret/claude/github token=ghp_your_token_here

# Отримати у скрипті-обгортці
# ~/.claude/scripts/mcp-github-vault.sh
#!/bin/bash
export GITHUB_TOKEN=$(vault kv get -field=token secret/claude/github)
npx @github/mcp-server

# ~/.claude.json (або .mcp.json)
{
  "mcpServers": {
    "github": {
      "command": "~/.claude/scripts/mcp-github-vault.sh",
      "args": []
    }
  }
}
```

**AWS Secrets Manager**:

```bash
# Зберегти секрет
aws secretsmanager create-secret \
  --name claude/github-token \
  --secret-string "ghp_your_token_here"

# Отримати в обгортці
export GITHUB_TOKEN=$(aws secretsmanager get-secret-value \
  --secret-id claude/github-token \
  --query SecretString \
  --output text)
npx @github/mcp-server
```

**1Password CLI** (зручно для команд):

```bash
# Створити елемент у 1Password (через GUI або CLI)
op item create --category=password \
  --title="Claude MCP GitHub Token" \
  token=ghp_your_token_here

# Отримати в обгортці
export GITHUB_TOKEN=$(op read "op://Private/Claude MCP GitHub Token/token")
npx @github/mcp-server
```

---

#### Воркфлоу ротації секретів

**Проблема**: API-ключі застарівають або компрометуються. Ротація секретів на багатьох MCP-серверах вручну — це шлях до помилок.

**Рішення**: Централізований файл `.env` зі скриптом ротації.

```bash
# ~/.claude/rotate-secret.sh
#!/bin/bash
SECRET_NAME=$1
NEW_VALUE=$2

# 1. Оновити файл .env
sed -i.bak "s|^${SECRET_NAME}=.*|${SECRET_NAME}=${NEW_VALUE}|" ~/.claude/.env

# 2. Перегенерувати конфіг із шаблону
envsubst < ~/.claude/mcp-config.template.json > ~/.claude.json

# 3. Перезапустити MCP-сервери (якщо запущені)
pkill -f "mcp-server" || true

echo "✅ Ротовано $SECRET_NAME"
echo "⚠️ Перезапустіть Claude Code, щоб застосувати зміни"
```

**Автоматична ротація з Vault** (просунуто):

```bash
# vault-rotate.sh
#!/bin/bash
# Отримання свіжих секретів із Vault, оновлення .env, перезапуск Claude
vault kv get -format=json secret/claude | jq -r '.data.data | to_entries[] | "\(.key)=\(.value)"' > ~/.claude/.env
envsubst < ~/.claude/mcp-config.template.json > ~/.claude.json

echo "✅ Секрети ротовано з Vault"
```

---

#### Виявлення секретів перед комітом (Pre-Commit)

**Проблема**: Розробники випадково комітять секрети в Git попри `.gitignore` (наприклад, через `git add -f .env`).

**Рішення**: [Pre-commit hook](../../examples/hooks/bash/pre-commit-secrets.sh) для блокування комітів із секретами.

```bash
# Встановити хук
cp examples/hooks/bash/pre-commit-secrets.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

# Тест (має завершитися помилкою)
echo "GITHUB_TOKEN=ghp_test" > test.txt
git add test.txt
git commit -m "Test"
# ❌ Заблоковано: Виявлено секрет у test.txt
```

**Патерни виявлення**: OpenAI keys (`sk-...`), GitHub tokens (`ghp_...`), AWS keys (`AKIA...`), загальні API-ключі.

---

#### Чек-лист перевірки

Перед запуском MCP-серверів із секретами:

| Перевірка | Команда | Критерій успіху |
|-------|---------|---------------|
| **.env не в Git** | `git ls-files | grep .env` | Порожній вивід |
| **Права доступу** | `ls -l ~/.claude/.env` | `-rw-------` (600) |
| **Шаблон у Git** | `git ls-files | grep template` | `mcp.json.template` наявний |
| **Pre-commit хук** | `cat .git/hooks/pre-commit` | Скрипт виявлення наявний |
| **Секрети розкриті** | `claude mcp list` | Усі сервери запускаються без помилок |

---

#### Підсумок найкращих практик

- **Використовуйте системну зв'язку ключів (OS keychain)**, де це можливо.
- **Ніколи не комітьте .env у Git**. Один витік = повна компрометація.
- **Комітьте шаблон .env.example** для швидкого онбордингу команди.
- **Використовуйте `${VAR}` у конфігу MCP**, щоб відокремити налаштування від секретів.
- **Ротуйте секрети щоквартально**, щоб обмежити радіус ураження старих витоків.
- **Використовуйте принцип найменших привілеїв**: користувачі БД тільки для читання, токени API з обмеженою сферою дії.

---

## 8.4 Посібник із вибору сервера

### Дерево рішень

```
Що вам потрібно?
│
├─ Знаєте точний патерн/текст?
│  └─ Використовуйте нативний Grep або rg (~20мс)
│
├─ Глибоке розуміння коду?
│  └─ Використовуйте Serena
│
├─ Дослідження коду за наміром / семантикою?
│  └─ Використовуйте grepai (~500мс)
│
├─ Відстеження "хто кого викликає"? (граф викликів)
│  └─ Використовуйте grepai
│
├─ Документація бібліотек?
│  └─ Використовуйте Context7
│
├─ Складні міркування?
│  └─ Використовуйте Sequential Thinking
│
├─ Запити до бази даних?
│  └─ Використовуйте Postgres
│
├─ Тестування в браузері?
│  └─ Використовуйте Playwright
│
└─ Загальне завдання?
   └─ Використовуйте вбудовані інструменти
```

### Порівняння серверів

| Потреба | Найкращий інструмент | Чому |
|------|-----------|-----|
| "Знайди точний рядок 'validateUser'" | Нативний Grep / rg | Швидкий точний збіг (~20мс) |
| "Знайди всі використання цієї функції" | Serena | Семантичний аналіз символів |
| "Запам'ятай це для наступної сесії" | Serena | Персистентна пам'ять |
| "Знайди код, що обробляє платежі" | grepai / mgrep | Семантичний пошук за наміром |
| "Хто викликає цю функцію?" | grepai | Аналіз графа викликів |
| "Як працює React useEffect?" | Context7 | Офіційна документація |
| "Чому це не працює?" | Sequential | Структурований дебаг |
| "Тестуй флоу логіну" | Playwright | Автоматизація браузера |

### Випадок із практики: Mergify (Cross-System Investigator)

**Контекст**: Mergify (платформа автоматизації CI/CD) потребувала сортування тікетів підтримки у 5 різних системах — ручний процес займав 15 хвилин на тікет.

**Архітектура**: Claude Code як оркестратор + 5 кастомних MCP-серверів як адаптери систем: Datadog, Sentry, PostgreSQL, Linear, GitHub.

**Результати** (листопад 2025):
- Час сортування: ~15 хв → <5 хв (скорочення на ⅔).
- Точність першого проходу: 75% (25% потребують перевірки людиною).

**Ключовий висновок**: Цей патерн — Claude Code як операційний оркестратор — підходить будь-якій команді підтримки, що працює з багатьма розрізненими системами. Це відрізняється від "Claude як інструмент розробки": тут він працює у **виробничому воркфлоу**.

---

## 8.5 Система плагінів

Claude Code включає повноцінну **систему плагінів**, яка дозволяє розширювати функціональність за допомогою спільноти або власних розробок.

### Що таке плагіни?

Плагіни — це запаковані розширення, які можуть додавати:
- Кастомних агентів зі спеціалізованою поведінкою.
- Нові навички (skills) для багаторазових воркфлоу.
- Попередньо налаштовані команди.
- Інструментарій для конкретних доменів.

Сприймайте плагіни як **дистрибутивні пакети**, що об'єднують агентів, навички та конфігурацію в модулі, які легко встановити.

### Команди плагінів

| Команда | Призначення | Приклад |
|---------|---------|---------|
| `claude plugin` | Список встановлених плагінів | Показує всі плагіни та їх статус |
| `claude plugin install <name>` | Встановити з маркетплейсу | `claude plugin install security-audit` |
| `claude plugin enable <name>` | Увімкнути плагін | `claude plugin enable security-audit` |
| `claude plugin disable <name>` | Вимкнути без видалення | `claude plugin disable linter` |
| `claude plugin uninstall <name>` | Повне видалення | `claude plugin uninstall security-audit` |
| `claude plugin update [name]` | Оновити до останньої версії | `claude plugin update security-audit` |
| `claude plugin validate <path>` | Перевірити маніфест плагіна | `claude plugin validate ./my-plugin` |

> **`${CLAUDE_PLUGIN_DATA}` — Персистентне сховище (v2.1.78+)**: Плагіни можуть зберігати стан, що виживає після оновлень, використовуючи змінну `${CLAUDE_PLUGIN_DATA}`. Використовуйте її для кешу, налаштувань користувача або будь-яких даних, необхідних між сесіями.

### Управління маркетплейсами

Маркетплейси — це репозиторії, з яких можна встановлювати плагіни.

```bash
# Додати маркетплейс
claude plugin marketplace add https://github.com/claudecode/plugins
claude plugin marketplace add gh:myorg/claude-plugins  # GitHub shorthand

# Оновити каталог
claude plugin marketplace update [name]
```

### Нативна підтримка LSP (v2.0.74+)

З грудня 2025 року Claude Code нативно інтегрується з серверами Language Server Protocol. Замість того, щоб ходити по коду через текстовий пошук (grep), Claude підключається до LSP-сервера вашого проекту і розуміє символи, типи та перехресні посилання — так само як IDE.

**Чому це важливо**: Пошук усіх місць виклику функції скорочується з ~45 секунд до ~50мс. Claude також отримує автоматичну діагностику — помилки з'являються в реальному часі без кроку збірки.

**Активація**:
```bash
ENABLE_LSP_TOOL=1 claude
```

**Сервери для мов**:
- TypeScript: `tsserver`.
- Python: `pylsp` (`pip install python-lsp-server`).
- Rust: `rust-analyzer`.
- Swift: `sourcekit-lsp`.

#### Конфігурація таймаутів (`.lsp.json`)
Визначає, як довго Claude чекає на ініціалізацію сервера перед тим, як вважати його неактивним. Корисно для повільних оточень (Docker, CI).

---

### Плагін vs MCP-сервер

- **Плагін** = "Як Claude думає" (нові воркфлоу, спеціалізовані агенти). Наприклад, агент-аудитор безпеки.
- **MCP-сервер** = "Що Claude може робити" (нові інструменти, зовнішні системи). Наприклад, доступ до PostgreSQL або автоматизація браузера.

---

### Маркетплейси спільноти

- **[wshobson/agents](https://github.com/wshobson/agents)**: 67 плагінів, 99 агентів, 107 навичок. Виробничі воркфлоу, DevOps, безпека.
- **[claude-plugins.dev](https://claude-plugins.dev)**: Понад 11,000 плагінів, проіндексованих для легкого пошуку.

### Популярні плагіни (січень 2026):
1. **Context7** (~72k встановлень): Пошук документації бібліотек.
2. **Ralph Wiggum** (~57k встановлень): Автоматизація рев'ю коду.
3. **Figma MCP** (~18k встановлень): Дизайн у код.

### Плагіни з цього посібника:
Усі 181 шаблон із директорії `examples/` доступні як плагіни:
```bash
claude plugin marketplace add FlorianBruniaux/claude-code-plugins
```
Серед них: `security-suite`, `devops-pipeline`, `code-quality`, `session-tools`.

---

#### Vitals — Детекція здоров'я кодобази

**Проблема**: ШІ пише код швидше, ніж команди встигають його підтримувати. Аналіз GitClear показує, що частка рефакторингу впала з 25% до <10% (2021–2025).
**Рішення**: Vitals розраховує `git churn × structural complexity × coupling centrality`, щоб визначити "гарячі точки" — файли, які з найбільшою ймовірністю викличуть проблеми наступними.

```bash
/plugin marketplace add chopratejas/vitals
/plugin install vitals@vitals
/vitals:scan src/ --top 5
```
