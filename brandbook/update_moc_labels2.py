import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace JS dictionary lines
replacements = {
    "moc1: 'Фирменный стиль',": "moc1: 'Блокнот с гравировкой',",
    "moc2: 'Печатная продукция',": "moc2: 'Визитная карточка',",
    "moc3: 'Рабочие тетради',": "moc3: 'Неоновая вывеска',",
    "moc4: 'Материалы для ретрита',": "moc4: 'Мерч · Футболка',",
    "moc5: 'Оформление соцсетей',": "moc5: 'Фирменная кружка',"
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mockup labels updated accurately.")
