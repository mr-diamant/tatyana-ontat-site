import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'https://finguide.kz/page/brandbook/moc1.png': 'moc5.webp',
    'https://finguide.kz/page/brandbook/moc2.png': 'moc6.webp',
    'https://finguide.kz/page/brandbook/moc3.png': 'moc7.webp',
    'https://finguide.kz/page/brandbook/moc4.png': 'moc8.webp',
    'https://finguide.kz/page/brandbook/moc5.png': 'moc9.webp'
}

for old_src, new_src in replacements.items():
    content = content.replace(old_src, new_src)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mockup images replaced.")
