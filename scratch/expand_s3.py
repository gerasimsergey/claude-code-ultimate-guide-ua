import sys
path = '/Users/sergey/Documents/CLAUDE COWORK/Cowork Guide/claude-code-ultimate-guide/guide/ultimate-guide.uk.md'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if line.startswith('# 3. Пам\'ять та налаштування'):
        start_idx = i
        print(f'Found Section 3 at {i}')
    if line.startswith('## 4.') and start_idx != -1:
        end_idx = i
        print(f'Found Section 4 at {i}')
        break

if start_idx != -1 and end_idx != -1:
    new_section = [
        '_Швидкий перехід:_ [CLAUDE.md](#31-memory-files-claudemd) \u00b7 [Папка .claude](#32-the-claude-folder-structure) \u00b7 [Налаштування](#33-settings--permissions) \u00b7 [Правила пріоритетності](#34-precedence-rules) \u00b7 [Командна робота](#35-team-configuration-at-scale)\n',
        '\n',
        '---\n',
        '\n',
        '## 3.1 Файли пам\'яті (CLAUDE.md)\n',
        '\n',
        'Файл `CLAUDE.md` \u2014 це **зовнішня пам\'ять** вашого проекту. Він повідомляє Claude про ваші вподобання, не перевантажуючи кожен промпт.\n',
        '\n',
        '### Що має бути в CLAUDE.md:\n',
        '- **Команди збірки та тестів**: Наприклад, `npm run build`, `pytest`.\n',
        '- **Стандарти коду**: \"Використовуй тільки функціональні компоненти\", \"Крапки з комою обов\'язкові\".\n',
        '- **Архітектурні особливості**: \"Ми використовуємо Redux для стейту\", \"API знаходиться в /api/v1\".\n',
        '- **Термінологія**: Як називати певні сутності в проекті.\n',
        '\n',
        '### Приклад CLAUDE.md:\n',
        '```markdown\n',
        '# Проект: Awesome App\n',
        '\n',
        '## Команди\n',
        '- Збірка: `npm run build`\n',
        '- Тести: `npm test`\n',
        '- Лінтер: `npm run lint`\n',
        '\n',
        '## Стандарти\n',
        '- TypeScript, суворий режим.\n',
        '- Компоненти в `src/components`, хуки в `src/hooks`.\n',
        '- Використовуй Tailwind CSS для стилізації.\n',
        '```\n',
        '\n',
        '## 3.2 Структура папки .claude/\n',
        '\n',
        'Папка `.claude/` створюється автоматично і містить локальні дані сесії.\n',
        '\n',
        '- **`history.json`**: Історія ваших повідомлень (локально).\n',
        '- **`settings.json`**: Налаштування, специфічні для проекту.\n',
        '- **`mcp.json`**: Конфігурація MCP серверів для цього проекту.\n',
        '\n',
        '> **💡 Порада**: Додайте `.claude/` у свій `.gitignore`, щоб не ділитися історією сесій з іншими, але закомітьте `.claude/mcp.json`, якщо хочете поділитися налаштуваннями MCP серверів з командою.\n',
        '\n',
        '## 3.3 Налаштування та дозволи\n',
        '\n',
        'Ви можете змінити глобальні налаштування за допомогою команди:\n',
        '```bash\n',
        'claude config set <key> <value>\n',
        '```\n',
        '\n',
        '### Основні ключі:\n',
        '- `model`: Модель за замовчуванням.\n',
        '- `theme`: Тема терміналу.\n',
        '- `auto_apply_diff`: Чи застосовувати зміни автоматично (рекомендується `false`).\n',
        '\n',
        '## 3.4 Правила пріоритетності\n',
        '\n',
        'Коли Claude отримує інструкції, він слідує такій ієрархії (від найвищого до найнижчого пріоритету):\n',
        '1. **Ваш поточний промпт** (те, що ви написали щойно).\n',
        '2. **CLAUDE.md** у корені проекту.\n',
        '3. **Файли пам\'яті агента** (якщо використовується кастомний агент).\n',
        '4. **Глобальні налаштування** (`~/.claude/settings.json`).\n',
        '\n',
        '## 3.5 Конфігурація команди в масштабі\n',
        '\n',
        'Для великих команд рекомендується:\n',
        '- Створити спільний `CLAUDE.md` і закомітити його.\n',
        '- Використовувати `.claudeignore` для ігнорування папок, які не потребують індексації (наприклад, `dist/`, `build/`, `logs/`).\n',
        '- Налаштувати спільні MCP сервери в `.mcp.json`.\n',
        '\n',
        '---\n',
        '\n'
    ]
    lines[start_idx:end_idx] = ['# 3. Пам\'ять та налаштування (Memory & Settings)\n', '\n'] + new_section
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print(f'Successfully expanded Section 3.')
else:
    print(f'Could not find Section 3 ({start_idx}) or Section 4 ({end_idx}).')
