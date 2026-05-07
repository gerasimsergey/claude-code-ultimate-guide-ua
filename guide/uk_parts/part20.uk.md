```bash
# Запуск Claude Code для валідації повідомлення коміту
COMMIT_MSG=$(cat "$1")
claude -p "Is this commit message good? '$COMMIT_MSG'. Reply YES or NO with reason."
```

**Хук Pre-push**:

```bash
#!/bin/bash
# .git/hooks/pre-push

# Перевірка безпеки перед пушем
claude -p "Scan staged files for secrets and security issues. Exit 1 if found."
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    echo "Виявлено проблеми з безпекою. Пуш заблоковано."
    exit 1
fi
```

### Інтеграція з GitHub Actions

```yaml
# .github/workflows/claude-review.yml
name: Claude Code Review

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p "Review the changes in this PR. \
            Focus on security, performance, and code quality. \
            Output as markdown." --bare
```

> **Прапорець `--bare` для CI-скриптів (v2.1.81+)**: додавайте `--bare` до будь-якого виклику `claude -p`, щоб отримати детерміноване, герметичне середовище виконання. Це вимикає хуки, LSP, синхронізацію плагінів та сканування директорій навичок — гарантуючи, що локальні конфіги розробника ніколи не потраплять у CI. Потребує `ANTHROPIC_API_KEY` (без OAuth). Також вимикає автоматичну пам'ять.

#### Налагодження невдалих запусків CI

Коли GitHub Actions видає помилку, використовуйте `gh` CLI для дослідження, не виходячи з термінала:

```bash
# Список останніх запусків воркфлоу
gh run list --limit 10

# Перегляд деталей конкретного запуску
gh run view <run-id>

# Перегляд логів для невдалого запуску
gh run view <run-id> --log-failed

# Аналіз помилок через Claude
gh run view $FAILED_RUN --log-failed | claude -p "Analyze this CI failure and suggest fixes"
```

---

### Патерн Verify Gate

Перед створенням PR переконайтеся, що всі локальні перевірки пройдено. Це економить цикли CI та час рев'юерів.

**Патерн**:
```
Build ✓ → Lint ✓ → Test ✓ → Type-check ✓ → ТІЛЬКИ ТОДІ створюємо PR
```

**Реалізація як команди** (`.claude/commands/complete-task.md`):

```markdown
# Завершити завдання

Запустіть повну перевірку (verify gate) перед створенням PR:
1. **Build**: `pnpm build`
2. **Lint**: `pnpm lint` (нуль помилок)
3. **Test**: `pnpm test` (усі тести пройдені)
4. **Type-check**: `pnpm typecheck`

Якщо БУДЬ-ЯКИЙ крок не вдається:
- Зупиніться негайно
- Повідомте, що і чому зламалося
- Запропонуйте виправлення
- НЕ переходьте до створення PR

Якщо ВСІ кроки пройдені:
- Створіть PR через `gh pr create`
- Чекайте на CI: `gh pr checks --watch`
- Якщо CI впаде, отримайте фідбек та виправте автоматично
```

---

### Генерація Release Notes

Автоматизуйте створення нотаток до релізу та чейнджлогу за допомогою Claude Code.

**Чому варто це автоматизувати?**
- Єдиний формат для всіх релізів.
- Вилучення технічних деталей безпосередньо з комітів.
- Переклад технічних змін на мову, зрозумілу користувачу.
- Економія 30-60 хвилин на кожному релізі.

#### Підхід 1: На основі команд

Створіть `.claude/commands/release-notes.md`:
1. **Отримати коміти** з моменту останнього тегу.
2. **Проаналізувати деталі**: повідомлення, змінені файли, номери PR.
3. **Категоризувати**: ✨ Features, 🐛 Bug Fixes, ⚡ Performance, 🔒 Security, 📝 Documentation, 🔧 Maintenance, ⚠️ Breaking Changes.
4. **Згенерувати три версії**:
   - **A. Формат CHANGELOG.md** (технічний, для розробників).
   - **B. GitHub Release Notes** (баланс технічного та контексту).
   - **C. Анонс для користувачів** (нетехнічний, акцент на перевагах).

#### Підхід 2: Автоматизація в CI/CD
Додайте воркфлоу, який при пуші нового тегу (`v*`) автоматично генерує нотатки через Claude, створює GitHub Release через `gh release create` та оновлює `CHANGELOG.md` у репозиторії.

---

### Changelog Fragments: Патерн примусового виконання для кожного PR

Альтернатива генерації з комітів — фіксація контексту *під час розробки*. Кожен PR створює свій YAML-файл у `changelog/fragments/`, які автоматично збираються під час релізу.

**Проблема комітів**: через три тижні після фіксу ніхто не пам'ятає, на що саме він вплинув.
**Рішення**:
- **Шар 1 (CLAUDE.md)**: правило, за яким Claude автоматично створює фрагмент при підготовці PR.
- **Шар 2 (Хук UserPromptSubmit)**: підказує розробнику створити фрагмент, якщо він забув.
- **Шар 3 (CI Gate)**: блокує PR без фрагмента або якщо додано міграції БД, але не позначено `migration: true`.

**Збірка при релізі**: `pnpm changelog:assemble --version 1.8.0`. Збирає всі фрагменти, групує за типами, вставляє в `CHANGELOG.md` та архівує використані фрагменти.

---

### Автоматизація розгортання (Deployment)

Claude Code може автоматизувати деплой на Vercel, GCP тощо, використовуючи збережені облікові дані.

**Обов'язкові обмеження (Guardrails)**:
- **Staging-first**: завжди спочатку на стейджинг.
- **Підтвердження людиною**: Claude зупиняється перед прапорцем `--prod` і просить підтвердження.
- **Smoke test**: перевірка HTTP 200 на ключових ендпоінтах після деплою.
- **Готовність до відкату**: збереження попереднього ID деплою.

---

## 9.4 Інтеграція з IDE

- **VS Code**: розширення "Claude Code" (Ctrl+Shift+P → Start Session).
- **JetBrains**: плагін для IntelliJ, WebStorm, PyCharm.
- **Xcode (лютий 2026)**: нативна підтримка Claude Agent SDK в Xcode 26.3 RC+.

### Інтеграція з терміналом

**macOS/Linux (Bash/Zsh)**:
```bash
alias cc='claude'
alias ccp='claude --plan'
alias cce='claude --execute'

cq() { claude -p "$*"; } # Швидке запитання: cq "як працює цей regex?"
```

**Windows (PowerShell)**:
Додайте функції `cc`, `ccp`, `cce` та `cq` до вашого `$PROFILE`.
```powershell
function cq {
    param([Parameter(ValueFromRemainingArguments)]$question)
    claude -p ($question -join ' ')
}
```

---

## 9.5 Швидкі цикли зворотного зв'язку

Швидкий фідбек прискорює навчання та ловить помилки на ранніх стадіях.

**Піраміда зворотного зв'язку**:
1. **Миттєво (IDE)**: TypeCheck, Lint.
2. **Секунди (Локально)**: Юніт-тести.
3. **Хвилини (CI/CD)**: Повний конвеєр перевірок.
4. **Години/Дні**: Тести після розгортання.

**Інтеграція з Claude Code**:
Використовуйте хуки `PostToolUse` (наприклад, після `Edit` або `Write`), щоб автоматично запускати швидку перевірку типів (`tsc --noEmit`) для зміненого файлу.
