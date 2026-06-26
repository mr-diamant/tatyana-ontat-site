import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix mission highlight color
content = content.replace('<span style="color: var(--green);">', '<span style="color: #9830D5;">')
# Just in case JS was escaped
content = content.replace('<span style=\\"color: var(--green);\\">', '<span style=\\"color: #9830D5;\\">')

# Fix red to #9830D5 in the rules block
content = content.replace('background: rgba(255,0,0,0.08);', 'background: rgba(152,48,213,0.08);')
content = content.replace('border-left: 3px solid #c0392b;', 'border-left: 3px solid #9830D5;')
content = content.replace('color: #e74c3c;', 'color: #9830D5;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Colors fixed.")
