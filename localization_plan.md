# План локалізації репозиторію Claude Code Ultimate Guide

Працюємо за **Протоколом чистої локалізації (Antigravity Protocol)**.
Мета: 100% лінгвістичне дзеркалювання англійського оригіналу в українську мову (`.uk.md`).

## 👥 Команда та відповідальні:
- **Sergey (User)**: Нагляд, фінальна перевірка, координація PR.
- **Antigravity (AI)**: Виконання перекладу, забезпечення структурного паритету, технічний контроль.

## 🔄 Статус виконання:

### [В ПРОЦЕСІ] Фаза 6: Аудит та Верифікація (Post-Localization Audit)
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
- [ ] guide/cheatsheet.md (0/1) — *Antigravity*
- [ ] guide/README.md (0/1) — *Antigravity*
- [ ] guide/cowork.md (0/1) — *Antigravity*

### 3. Розділ Core (guide/core/)
- [ ] guide/core/architecture.md (0/1)
- [ ] guide/core/claude-code-releases.md (0/1)
- [ ] guide/core/context-engineering.md (0/1)
- [ ] guide/core/methodologies.md (0/1)
- [ ] guide/core/settings-reference.md (0/1)
- [ ] guide/core/glossary.md (0/1)
- [ ] guide/core/known-issues.md (0/1)
- [ ] guide/core/skill-design-patterns.md (0/1)
- [ ] guide/core/visual-reference.md (0/1)
- [ ] guide/core/credits.md (0/1)

### 4. Операційний розділ (guide/ops/)
- [ ] guide/ops/devops-sre.md (0/1)
- [ ] guide/ops/observability.md (0/1)
- [ ] guide/ops/ai-traceability.md (0/1)
- [ ] guide/ops/team-metrics.md (0/1)

### 5. Безпека (guide/security/)
- [ ] guide/security/security-hardening.md (0/1)
- [ ] guide/security/production-safety.md (0/1)
- [ ] guide/security/data-privacy.md (0/1)
- [ ] guide/security/enterprise-governance.md (0/1)
- [ ] guide/security/sandbox-isolation.md (0/1)
- [ ] guide/security/sandbox-native.md (0/1)

### 6. Ролі та Воркфлоу (guide/roles/ та guide/workflows/)
- [ ] guide/roles/ai-roles.md (0/1)
- [ ] guide/roles/adoption-approaches.md (0/1)
- [ ] guide/roles/learning-with-ai.md (0/1)
- [ ] guide/roles/agent-evaluation.md (0/1)
- [ ] guide/workflows/agent-teams.md (0/1)
- [ ] guide/workflows/tdd-with-claude.md (0/1)
- [ ] guide/workflows/plan-driven.md (0/1)
- [ ] guide/workflows/spec-first.md (0/1)
- [ ] guide/workflows/README.md (0/1)
- [ ] *...інші воркфлоу будуть додані після завершення основних розділів*

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

