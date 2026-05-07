import sys
path = '/Users/sergey/Documents/CLAUDE COWORK/Cowork Guide/claude-code-ultimate-guide/guide/ultimate-guide.uk.md'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if line.startswith('# 5. Скіли'):
        start_idx = i
        print(f'Found Section 5 at {i}')
    if line.startswith('# 6.') and start_idx != -1:
        end_idx = i
        print(f'Found Section 6 at {i}')
        break

if start_idx != -1 and end_idx != -1:
    new_section = [
        '# 5. Скіли (Skills) [Середній рівень] [30 хв]\n',
        '\n',
        '_Швидкий перехід:_ [Розуміння](#51-understanding-skills) \u00b7 [Створення](#52-creating-skills) \u00b7 [Шаблон](#53-skill-template) \u00b7 [Приклади](#54-skill-examples)\n',
        '\n',
        '---\n',
        '\n',
        '## 5.1 Розуміння скілів (Understanding Skills)\n',
        '\n',
        'Скіли \u2014 це виконувані скрипти або папки з інструкціями, які розширюють можливості Claude. На відміну від агентів, скіли \u2014 це **інструменти**, які Claude може викликати під час будь-якої сесії.\n',
        '\n',
        '## 5.2 Створення скілів\n',
        '\n',
        'Скіли зберігаються в `~/.claude/skills/` (глобально) або `.claude/skills/` (локально).\n',
        '\n',
        '### Типи скілів:\n',
        '1. **Instructional Skills**: Папка з файлом `SKILL.md` (інструкції).\n',
        '2. **Executable Skills**: Скрипти на Python або JS, які Claude може запускати.\n',
        '\n',
        '## 5.3 Шаблон скіла\n',
        '\n',
        'Створіть файл `.claude/skills/tailwind-helper/SKILL.md`:\n',
        '\n',
        '```markdown\n',
        '# Skill: Tailwind Helper\n',
        '\n',
        'Використовуй цей скіл, коли користувач просить стилізувати компоненти.\n',
        '\n',
        '## Standards\n',
        '- Використовуй тільки стандартні класи Tailwind.\n',
        '- Уникайте інлайнових стилів.\n',
        '- Групуйте класи за категоріями (layout, spacing, colors).\n',
        '```\n',
        '\n',
        '## 5.4 Приклади скілів\n',
        '\n',
        '- **Migration-Skill**: Скрипти для автоматичної міграції БД.\n',
        '- **Deploy-Skill**: Команди для пушу в стейджинг.\n',
        '- **Cleanup-Skill**: Видалення тимчасових файлів та артефактів збірки.\n',
        '\n',
        '---\n',
        '\n'
    ]
    lines[start_idx:end_idx] = new_section
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print(f'Successfully expanded Section 5.')
else:
    print(f'Could not find Section 5 ({start_idx}) or Section 6 ({end_idx}).')
