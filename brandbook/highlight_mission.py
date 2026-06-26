import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove -webkit-text-fill-color
content = content.replace('style="color: #ffffff; -webkit-text-fill-color: #ffffff;"', 'style="color: #ffffff;"')

# 2. Update HTML directly
old_mission_html = "Стать надежным мостом на пути к осознанности, трансформации и возвращению к своей подлинной природе."
new_mission_html = 'Стать надежным мостом на пути к <span style="color: var(--green);">осознанности</span>, <span style="color: var(--green);">трансформации</span> и возвращению к своей подлинной природе.'

old_strategy_html = "Я не останавливаюсь на решении сиюминутных проблем. Пока человек идёт по пути я рядом до результата."
new_strategy_html = 'Я не останавливаюсь на решении сиюминутных проблем. Пока человек идёт по пути я <span style="color: var(--green);">рядом до результата</span>.'

content = content.replace(old_mission_html, new_mission_html)
content = content.replace(old_strategy_html, new_strategy_html)

# 3. Update JS Dictionary (ru, en, tr)
# The JS dictionary currently has:
# mission_quote: 'Стать надежным мостом на пути к <span>осознанности</span>, трансформации и возвращению к своей подлинной природе.',
# strategy_text: 'Я не останавливаюсь на решении сиюминутных проблем. Пока человек идёт по пути я рядом до результата.',

content = content.replace(
    "mission_quote: 'Стать надежным мостом на пути к <span>осознанности</span>, трансформации и возвращению к своей подлинной природе.',",
    "mission_quote: 'Стать надежным мостом на пути к <span style=\"color: var(--green);\">осознанности</span>, <span style=\"color: var(--green);\">трансформации</span> и возвращению к своей подлинной природе.',"
)
content = content.replace(
    "strategy_text: 'Я не останавливаюсь на решении сиюминутных проблем. Пока человек идёт по пути я рядом до результата.',",
    "strategy_text: 'Я не останавливаюсь на решении сиюминутных проблем. Пока человек идёт по пути я <span style=\"color: var(--green);\">рядом до результата</span>.',"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Highlights applied.")
