import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('FinGuide Expert · Брендбук 2026', 'Стокгольм · Стамбул · 2026')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Page indicators updated.")
