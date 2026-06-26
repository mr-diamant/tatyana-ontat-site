import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace JS dictionary lines
replacements = {
    "moc1: 'Наружная вывеска',": "moc1: 'Фирменный стиль',",
    "moc2: 'Мерч · Одежда',": "moc2: 'Печатная продукция',",
    "moc3: 'Визитные карточки',": "moc3: 'Рабочие тетради',",
    "moc4: 'Фирменный бланк',": "moc4: 'Материалы для ретрита',",
    "moc5: 'Золотое тиснение',": "moc5: 'Оформление соцсетей',"
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mockup labels updated.")
