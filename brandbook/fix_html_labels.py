import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '>Наружная вывеска</span>': '>Блокнот с гравировкой</span>',
    '>Мерч · Одежда</span>': '>Визитная карточка</span>',
    '>Визитные карточки</span>': '>Неоновая вывеска</span>',
    '>Фирменный бланк</span>': '>Мерч · Футболка</span>',
    '>Золотое тиснение</span>': '>Фирменная кружка</span>'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML labels fixed.")
