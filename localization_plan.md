# План локалізації репозиторію Claude Code Ultimate Guide

Працюємо за **Протоколом чистої локалізації (Antigravity Protocol)**.
Мета: 100% лінгвістичне дзеркалювання англійського оригіналу в українську мову (`.uk.md`).

## 👥 Команда та відповідальні:
- **Sergey (User)**: Нагляд, фінальна перевірка, координація PR.
- **Antigravity (AI)**: Виконання перекладу, забезпечення структурного паритету, технічний контроль.

## 🔄 Статус виконання:

## Фаза 6: Аудит та верифікація (В ПРОЦЕСІ)
> ⏸️ **УВАГА: Файл `guide/ultimate-guide.uk.md` поки що не чіпаємо і не змінюємо!**
- [x] Аудит структурної цілісності таблиць та блоків коду
- [x] Стандартизація атрибуції локалізації (Serhii / MacPlus Software) — **Завершено**
- [ ] Валідація внутрішніх посилань (анкорів)
- [ ] Порівняльна перевірка обсягу тексту (рядки vs байти)
- [ ] **Порівняльна перевірка рядків (Line Count Audit)**: Оригінал має 25 744 рядки, локалізований файл — ~14 300. Необхідно виявити причину розбіжності:
    - Чи це результат злиття порожніх рядків?
    - Чи були пропущені блоки коду або тексту під час перекладу "частинами"?
    - Використати ШІ-модель для посторінкового порівняння структури (Structural Parity Check).
- [ ] **Перевірка перехресних посилань**: Переконатися, що всі якорі (`#anchor`) працюють у межах одного великого файлу.
- [ ] **Валідація Markdown-блоків**: Пошук незакритих кодових блоків або зламаних таблиць.

### 1. Головні документи (Root)
- [x] README.md (1/1) — *Antigravity*
- [x] CONTRIBUTING.md (1/1) — *Antigravity*
- [x] SECURITY.md (1/1) — *Antigravity*
- [x] CLAUDE.md (1/1) — *Antigravity*


### 2. Основний посібник (guide/)
- [x] guide/ultimate-guide.md (1/1) — *Antigravity* (Зібрано 32 частини, потребує аудиту рядків)
- [x] guide/cheatsheet.md (1/1) — *Antigravity*
- [x] guide/README.md (1/1) — *Antigravity*
- [x] guide/cowork.md (1/1) — *Antigravity*

### 3. Розділ Core (guide/core/)
- [x] guide/core/architecture.md (1/1) — *Antigravity*
- [x] guide/core/claude-code-releases.md (1/1) — *Antigravity*
- [x] guide/core/context-engineering.md (1/1) — *Antigravity*
- [x] guide/core/methodologies.md (1/1) — *Antigravity*
- [x] guide/core/settings-reference.md (1/1) — *Antigravity*
- [x] guide/core/glossary.md (1/1) — *Antigravity*
- [x] guide/core/known-issues.md (1/1) — *Antigravity*
- [x] guide/core/skill-design-patterns.md (1/1) — *Antigravity*
- [x] guide/core/visual-reference.md (1/1) — *Antigravity*
- [x] guide/core/credits.md (1/1) — *Antigravity*

### 4. Операційний розділ (guide/ops/)
- [x] guide/ops/devops-sre.md (1/1) — *Antigravity*
- [x] guide/ops/observability.md (1/1) — *Antigravity*
- [x] guide/ops/ai-traceability.md (1/1) — *Antigravity*
- [x] guide/ops/team-metrics.md (1/1) — *Antigravity*

### 5. Безпека (guide/security/)
- [x] guide/security/security-hardening.md (1/1) — *Antigravity*
- [x] guide/security/production-safety.md (1/1) — *Antigravity*
- [x] guide/security/data-privacy.md (1/1) — *Antigravity*
- [x] guide/security/enterprise-governance.md (1/1) — *Antigravity*
- [x] guide/security/sandbox-isolation.md (1/1) — *Antigravity*
- [x] guide/security/sandbox-native.md (1/1) — *Antigravity*

### 6. Ролі та Воркфлоу (guide/roles/ та guide/workflows/)
- [x] guide/roles/ai-roles.md (1/1) — *Antigravity*
- [x] guide/roles/adoption-approaches.md (1/1) — *Antigravity*
- [x] guide/roles/learning-with-ai.md (1/1) — *Antigravity*
- [x] guide/roles/agent-evaluation.md (1/1) — *Antigravity*
- [x] guide/workflows/README.md (1/1) — *Antigravity*
- [x] guide/workflows/agent-teams.md (1/1) — *Antigravity*
- [x] guide/workflows/tdd-with-claude.md (1/1) — *Antigravity*
- [x] guide/workflows/plan-driven.md (1/1) — *Antigravity*
- [x] guide/workflows/spec-first.md (1/1) — *Antigravity*
- [x] guide/workflows/search-tools-mastery.md (1/1) — *Antigravity*
- [x] guide/workflows/exploration-workflow.md (1/1) — *Antigravity*
- [x] guide/workflows/iterative-refinement.md (1/1) — *Antigravity*
- [x] guide/workflows/skeleton-projects.md (1/1) — *Antigravity*
- [x] guide/workflows/team-ai-instructions.md (1/1) — *Antigravity*
- [x] guide/workflows/changelog-fragments.md (1/1) — *Antigravity*
- [x] guide/workflows/rpi.md (1/1) — *Antigravity*
- [x] guide/workflows/github-actions.md (1/1) — *Antigravity*
- [x] guide/workflows/gstack-workflow.md (1/1) — *Antigravity*
- [x] guide/workflows/design-to-code.md (1/1) — *Antigravity*
- [x] guide/workflows/og-image-generation.md (1/1) — *Antigravity*
- [x] guide/workflows/pdf-generation.md (1/1) — *Antigravity*
- [x] guide/workflows/talk-pipeline.md (1/1) — *Antigravity*
- [x] guide/workflows/tts-setup.md (1/1) — *Antigravity*
- [x] guide/workflows/agent-teams-quick-start.md (1/1) — *Antigravity*
- [x] guide/workflows/dual-instance-planning.md (1/1) — *Antigravity*
- [x] guide/workflows/event-driven-agents.md (1/1) — *Antigravity*
- [x] guide/workflows/plan-pipeline.md (1/1) — *Antigravity*
- [x] guide/workflows/task-management.md (1/1) — *Antigravity*
- [x] guide/workflows/code-review.md (1/1) — *Antigravity*
### Розділ 6: Екосистема (Ecosystem) — ЗАВЕРШЕНО
- [x] guide/ecosystem/ai-ecosystem.md (1/1) — *Antigravity*
- [x] guide/ecosystem/context-engineering-tools.md (1/1) — *Antigravity*
- [x] guide/ecosystem/mcp-servers-ecosystem.md (1/1) — *Antigravity*
- [x] guide/ecosystem/mcp-vs-cli.md (1/1) — *Antigravity*
- [x] guide/ecosystem/remarkable-ai.md (1/1) — *Antigravity*
- [x] guide/ecosystem/third-party-tools.md (1/1) — *Antigravity*
- [x] guide/learning-path/README.md (1/1) — *Antigravity*
- [x] guide/learning-path/01-installation.md (1/1) — *Antigravity*
- [x] guide/learning-path/02-core-loop.md (1/1) — *Antigravity*
- [x] guide/learning-path/03-memory.md (1/1) — *Antigravity*
- [x] guide/learning-path/04-agents.md (1/1) — *Antigravity*
- [x] guide/learning-path/05-skills.md (1/1) — *Antigravity*
- [x] guide/learning-path/06-hooks.md (1/1) — *Antigravity*
- [x] guide/learning-path/07-advanced.md (1/1) — *Antigravity*

---

## 🚀 Завдання на інтеграцію (Maintenance & Integration)
- [ ] **Підготовка Pull Request**: Після завершення перекладу кореневих документів та основного посібника, сформувати запит на включення (PR) в оригінальний репозиторій [FlorianBruniaux/claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide).
- [ ] **Налаштування автоматизації**: Адаптувати `scripts/translate-guide.py` для підтримки української мови як стандартної цілі.

## 🛠️ Технічні вимоги
- **Переклад**: Прямий, професійний, без регіональних адаптацій.
- **Паритет**: 100% відповідність структурі оригіналу.
- **Формат файлів**: `filename.uk.md` у тій же директорії, що й оригінал.
- **Код**: Блоки коду та технічні ідентифікатори залишаються англійською мовою.
- **Брендинг**: Кожен файл `.uk.md` має завершуватися футером:
  ```markdown
  ---
  **Локалізація**: [Serhii (MacPlus Software)](https://macplus-software.com)
  *Остання синхронізація: Травень 2026*
  ```

