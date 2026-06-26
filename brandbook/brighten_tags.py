import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace gold-light with brand purple for all tags to make them brighter
content = content.replace('style="color: var(--gold-light);"', 'style="color: #9830D5;"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Tags brightened.")
