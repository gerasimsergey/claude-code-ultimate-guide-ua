---
title: "Документація посібника"
description: "Індекс усіх основних файлів документації для опанування Claude Code"
tags: [guide, reference]
---

# Документація посібника

Основна документація для опанування Claude Code, організована за темами.

---

## Початок роботи

| Файл | Опис | Час |
|------|-------------|------|
| [**learning-path/**](./learning-path/README.md) | **Структурований навчальний шлях із 7 модулів** для початківців: Встановлення, Основний цикл, Пам'ять, Агенти, Скіли, Хуки, Просунуті патерни | 8-11 годин |
| [learning-path/01-installation.md](./learning-path/01-installation.md) | Модуль 01: Встановлення Claude Code та перевірка працездатності | 15 хв |
| [learning-path/02-core-loop.md](./learning-path/02-core-loop.md) | Модуль 02: Розуміння циклу взаємодії та контексту | 45 хв |
| [learning-path/03-memory.md](./learning-path/03-memory.md) | Модуль 03: Створення CLAUDE.md та налаштування пам'яті | 1 год |
| [learning-path/04-agents.md](./learning-path/04-agents.md) | Модуль 04: Створення спеціалізованих агентів | 1.5 год |
| [learning-path/05-skills.md](./learning-path/05-skills.md) | Модуль 05: Побудова багаторазових скілів | 1.5 год |
| [learning-path/06-hooks.md](./learning-path/06-hooks.md) | Модуль 06: Створення хуків автоматизації | 1 год |
| [learning-path/07-advanced.md](./learning-path/07-advanced.md) | Модуль 07: Багатоагентна оркестрація | 2-3 год |

---

## Основна довідка

| Файл | Опис | Час |
|------|-------------|------|
| [ultimate-guide.md](./ultimate-guide.md) | Повна довідка, що охоплює всі функції Claude Code | ~3 години |
| [cheatsheet.md](./cheatsheet.md) | Шпаргалка на 1 сторінку для друку | 5 хв |
| [core/architecture.md](./core/architecture.md) | Як Claude Code працює всередині (master loop, інструменти, контекст) | 25 хв |
| [core/methodologies.md](./core/methodologies.md) | Довідник із 15 методологій розробки (TDD, SDD, BDD тощо) | 20 хв |
| [core/visual-reference.md](./core/visual-reference.md) | Візуальна шпаргалка — ASCII діаграми для ключових концепцій | 5 хв |
| [core/claude-code-releases.md](./core/claude-code-releases.md) | Офіційна історія релізів (стисло) | 10 хв |
| [core/known-issues.md](./core/known-issues.md) | **Трекер критичних багів**: питання безпеки, споживання токенів, перевірені звіти спільноти | 15 хв |
| [core/context-engineering.md](./core/context-engineering.md) | **Інженерія контексту**: бюджет токенів, модульна архітектура, збірка команд, пайплайн ACE, вимірювання якості | 25 хв |
| [core/glossary.md](./core/glossary.md) | **Глосарій**: алфавітний покажчик термінів Claude Code, патернів спільноти та концепцій AI-інженерії | 10 хв |
| [diagrams/](./diagrams/) | **Серія візуальних діаграм**: 41 інтерактивна діаграма Mermaid для вибору моделі, життєвого циклу агента, безпеки, багатоагентних патернів | 15 хв |

---

## Безпека

| Файл | Опис | Час |
|------|-------------|------|
| [security/security-hardening.md](./security/security-hardening.md) | Загрози безпеці, перевірка MCP, захист від ін'єкцій | 25 хв |
| [security/sandbox-isolation.md](./security/sandbox-isolation.md) | Пісочниці Docker, хмарні альтернативи, воркфлоу безпечної автономії | 10 хв |
| [security/sandbox-native.md](./security/sandbox-native.md) | Нативна пісочниця Claude Code: конфігурація та модель безпеки | 10 хв |
| [security/production-safety.md](./security/production-safety.md) | Безпека у продакшені: захисні бар'єри, гейти перевірки, стратегії відкату | 15 хв |
| [security/data-privacy.md](./security/data-privacy.md) | Посібник із зберігання та конфіденційності даних | 10 хв |
| [security/enterprise-governance.md](./security/enterprise-governance.md) | **Управління на рівні організації**: статути використання, воркфлоу затвердження MCP, рівні захисту (Starter/Standard/Strict/Regulated), комплаєнс | 25 хв |

---

## Екосистема

| Файл | Опис | Час |
|------|-------------|------|
| [ecosystem/ai-ecosystem.md](./ecosystem/ai-ecosystem.md) | Додаткові AI-інструменти (Perplexity, Gemini, Kimi, NotebookLM, TTS) | 30 хв |
| [ecosystem/mcp-servers-ecosystem.md](./ecosystem/mcp-servers-ecosystem.md) | **Спільнота MCP серверів**: 8 перевірених серверів (Playwright, Semgrep, Kubernetes тощо) з продакшен-конфігами | 25 хв |
| [ecosystem/third-party-tools.md](./ecosystem/third-party-tools.md) | **Інструменти спільноти**: GUI, TUI, менеджери конфігів, трекери токенів, альтернативні інтерфейси | 15 хв |
| [ecosystem/context-engineering-tools.md](./ecosystem/context-engineering-tools.md) | **Оптимізація контексту та токенів**: стиснення виводу (RTK, Headroom), стиснення промптів (LLMLingua), AI-гейтвеї (Edgee, Portkey), RAG, LLMOps | 20 хв |
| [ecosystem/remarkable-ai.md](./ecosystem/remarkable-ai.md) | Видатні патерни використання AI та техніки для досвідчених користувачів | 10 хв |

---

## Ролі та Впровадження

| Файл | Опис | Час |
|------|-------------|------|
| [roles/ai-roles.md](./roles/ai-roles.md) | Картування AI ролей: коли використовувати Claude Code vs Claude Desktop vs API | 10 хв |
| [roles/adoption-approaches.md](./roles/adoption-approaches.md) | Стратегії впровадження для команд | 15 хв |
| [roles/learning-with-ai.md](./roles/learning-with-ai.md) | Посібник для Junior-розробників про використання AI без втрати навичок | 15 хв |
| [roles/agent-evaluation.md](./roles/agent-evaluation.md) | **Метрики якості агентів**: Вимірювання ефективності кастомних агентів за допомогою хуків, тестів та циклів фідбеку | 20 хв |

---

## Операції (Operations)

| Файл | Опис | Час |
|------|-------------|------|
| [ops/devops-sre.md](./ops/devops-sre.md) | FIRE фреймворк для діагностики інфраструктури та реагування на інциденти | 30 хв |
| [ops/observability.md](./ops/observability.md) | Моніторинг сесій та відстеження витрат | 15 хв |
| [ops/ai-traceability.md](./ops/ai-traceability.md) | Атрибуція AI, політики розкриття, git-ai, комплаєнс | 20 хв |
| [ops/team-metrics.md](./ops/team-metrics.md) | **Метрики команд для AI-доповненої інженерії**: DORA, SPACE, DX Core 4, AI-специфічні сигнали, за розміром команди (5–25 осіб) | 20 хв |

---

## Воркфлоу (Workflows)

Практичні посібники для ефективних патернів розробки:

| Файл | Опис |
|------|-------------|
| [workflows/tdd-with-claude.md](./workflows/tdd-with-claude.md) | Розробка через тестування (TDD) з Claude |
| [workflows/spec-first.md](./workflows/spec-first.md) | Розробка на основі специфікацій (SDD) |
| [workflows/plan-driven.md](./workflows/plan-driven.md) | Ефективне використання режиму /plan |
| [workflows/iterative-refinement.md](./workflows/iterative-refinement.md) | Цикли ітеративного вдосконалення |
| [workflows/tts-setup.md](./workflows/tts-setup.md) | Додавання озвучення тексту до Claude Code (18 хв) |
| [workflows/task-management.md](./workflows/task-management.md) | Відстеження завдань у кількох сесіях, міграція TodoWrite |
| [workflows/agent-teams.md](./workflows/agent-teams.md) | Оркестрація багатоагентних команд для складних завдань |
| [workflows/agent-teams-quick-start.md](./workflows/agent-teams-quick-start.md) | Швидкий старт для патернів команд агентів |
| [workflows/dual-instance-planning.md](./workflows/dual-instance-planning.md) | Планування з двома інстансами: Opus планує, Sonnet виконує |
| [workflows/event-driven-agents.md](./workflows/event-driven-agents.md) | Патерни координації агентів на основі подій |
| [workflows/plan-pipeline.md](./workflows/plan-pipeline.md) | Наскрізний пайплайн планування: запуск, валідація, виконання |
| [workflows/design-to-code.md](./workflows/design-to-code.md) | Конвертація Figma/вайрфреймів у робочий код |
| [workflows/exploration-workflow.md](./workflows/exploration-workflow.md) | Систематичне дослідження незнайомих кодобаз |
| [workflows/pdf-generation.md](./workflows/pdf-generation.md) | Генерація професійних PDF за допомогою Quarto/Typst |
| [workflows/search-tools-mastery.md](./workflows/search-tools-mastery.md) | Опанування комбінованих воркфлоу rg, grepai, Serena, ast-grep |
| [workflows/skeleton-projects.md](./workflows/skeleton-projects.md) | Використання перевірених репо як основи для нових проектів |
| [workflows/talk-pipeline.md](./workflows/talk-pipeline.md) | 6-стадійна підготовка виступу: від чернетки до слайдів |
| [workflows/team-ai-instructions.md](./workflows/team-ai-instructions.md) | Масштабування CLAUDE.md у командах з кількома розробниками |

---

## Документація Cowork

Для офісних працівників, які використовують Claude Cowork (агентний десктоп):

| Ресурс | Опис |
|----------|-------------|
| **[Cowork Hub](https://github.com/FlorianBruniaux/claude-cowork-guide/blob/main/README.md)** | Повна документація Cowork |
| [Початок роботи](https://github.com/FlorianBruniaux/claude-cowork-guide/blob/main/guide/01-getting-started.md) | Налаштування та перший воркфлоу |
| [Можливості](https://github.com/FlorianBruniaux/claude-cowork-guide/blob/main/guide/02-capabilities.md) | Що Cowork може/не може робити |
| [Посібник з безпеки](https://github.com/FlorianBruniaux/claude-cowork-guide/blob/main/guide/03-security.md) | Практики безпечного використання |
| [Бібліотека промптів](https://github.com/FlorianBruniaux/claude-cowork-guide/tree/main/prompts) | 50+ готових до використання промптів |
| [Шпаргалка](https://github.com/FlorianBruniaux/claude-cowork-guide/blob/main/reference/cheatsheet.md) | Швидка довідка на 1 сторінку |

---

## Рекомендований порядок читання

1. **Нові користувачі**: Почніть з розділу Quick Start у `ultimate-guide.md`
2. **Щоденна довідка**: Роздрукуйте `cheatsheet.md`
3. **Тімліди**: Прочитайте `roles/adoption-approaches.md` щодо стратегій впровадження
4. **Фокус на безпеці**: `security/security-hardening.md`, потім `security/sandbox-isolation.md`
5. **Глибока архітектура**: `core/architecture.md`, потім `diagrams/`

---

*Назад до [головного README](../README.md)*

---
**Локалізація**: [Serhii (MacPlus Software)](https://macplus-software.com)
*Остання синхронізація: Травень 2026*
