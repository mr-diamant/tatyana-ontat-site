import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_text = 'Специфические казахские и турецкие буквы отображаются корректно.'
new_text = 'Специфические турецкие буквы отображаются корректно.'

content = content.replace(old_text, new_text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Text replaced.")
