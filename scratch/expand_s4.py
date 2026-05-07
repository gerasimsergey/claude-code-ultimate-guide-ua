import sys
path = '/Users/sergey/Documents/CLAUDE COWORK/Cowork Guide/claude-code-ultimate-guide/guide/ultimate-guide.uk.md'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if line.startswith('## 4.1 Що таке агенти'):
        start_idx = i
        print(f'Found Section 4 point at {i}')
    if line.startswith('# 5.') and start_idx != -1:
        end_idx = i
        print(f'Found Section 5 at {i}')
        break

if start_idx != -1 and end_idx != -1:
    new_section = [
        '# 4. Агенти (Agents)\n',
        '\n',
        '_Швидкий перехід:_ [Що таке агенти](#41-what-are-agents) \u00b7 [Створення](#42-creating-custom-agents) \u00b7 [Шаблон](#43-agent-template) \u00b7 [Кращі практики](#44-best-practices) \u00b7 [Пам\'ять](#45-agent-memory) \u00b7 [Приклади](#46-agent-examples)\n',
        '\n',
        '---\n',
        '\n',
        '## 4.1 Що таке агенти (What Are Agents)\n',
        '\n',
        'Агенти в Claude Code \u2014 це спеціалізовані конфігурації Claude, які мають власні інструкції, набір інструментів та пам\'ять. Вони дозволяють перетворити Claude з загального помічника на вузькопрофільного експерта.\n',
        '\n',
        '## 4.2 Створення кастомних агентів\n',
        '\n',
        'Агенти визначаються у папці `.claude/agents/`. Кожен файл `.md` у цій папці стає новим агентом.\n',
        '\n',
        '**Як викликати агента:**\n',
        '```bash\n',
        'claude --agent <agent-name>\n',
        '```\n',
        '\n',
        '## 4.3 Шаблон агента\n',
        '\n',
        'Створіть файл `.claude/agents/reviewer.md`:\n',
        '\n',
        '```markdown\n',
        '# Agent: Code Reviewer\n',
        '\n',
        '## Role\n',
        'Ти \u2014 експерт з якості коду. Твоя мета \u2014 шукати баги та пропонувати покращення продуктивності.\n',
        '\n',
        '## Instructions\n',
        '- Завжди перевіряй обробку помилок.\n',
        '- Звертай увагу на зайві ререндери в React.\n',
        '- Будь лаконічним у своїх коментарях.\n',
        '\n',
        '## Tools\n',
        '- Дозволено: `read_file`, `ls`, `grep`.\n',
        '- Заборонено: `run_command` (тільки перегляд, без змін).\n',
        '```\n',
        '\n',
        '## 4.4 Кращі практики\n',
        '\n',
        '- **Вузька спеціалізація**: Один агент для тестів, інший для документації.\n',
        '- **Обмеження інструментів**: Не давайте агенту зайвих дозволів.\n',
        '- **Чіткі інструкції**: Використовуйте списки для кроків.\n',
        '\n',
        '## 4.5 Пам\'ять агента\n',
        '\n',
        'Агенти можуть мати свій власний файл пам\'яті, схожий на `CLAUDE.md`, але специфічний для їхньої ролі. Він завантажується автоматично при виклику агента.\n',
        '\n',
        '## 4.6 Приклади агентів\n',
        '\n',
        '1. **QA-Agent**: Автоматично пише Unit-тести для нових функцій.\n',
        '2. **Docs-Agent**: Оновлює `README.md` та JSDoc коментарі.\n',
        '3. **Security-Agent**: Сканує код на наявність вразливостей.\n',
        '\n',
        '## 4.7 Просунуті патерни агентів\n',
        '\n',
        '- **Agent Teams**: Виклик одного агента іншим (оркестрація).\n',
        '- **Conditional Agents**: Агенти, що активуються залежно від мови програмування.\n',
        '\n',
        '---\n',
        '\n'
    ]
    lines[start_idx:end_idx] = new_section
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print(f'Successfully expanded Section 4.')
else:
    print(f'Could not find Section 4 point ({start_idx}) or Section 5 ({end_idx}).')
