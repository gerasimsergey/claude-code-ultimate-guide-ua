import sys
import re

path = '/Users/sergey/Documents/CLAUDE COWORK/Cowork Guide/claude-code-ultimate-guide/guide/ultimate-guide.uk.md'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Section 2 header
content = content.replace('## 2. Основні концепції', '# 2. Основні концепції')

# Ensure TOC has 12 and 13
if '- [12. Висновки' not in content:
    toc_end_pattern = r'(- \[11\. AI екосистема: додаткові інструменти\].*?)\n---'
    content = re.sub(toc_end_pattern, r'\1\n- [12. Висновки](#12-висновки-від-оператора-до-архітектора)\n- [13. Ресурси та спільнота](#13-ресурси-та-спільнота)\n\n---', content, flags=re.DOTALL)

# Fix some common issues where code block comments might be at start of line
# Actually, the grep showed them, so they are likely at column 0
# I'll just leave them for now unless they break TOC/Rendering

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Final structural polish applied.')
