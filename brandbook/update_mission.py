import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update HTML direct content
old_html = """    <div class="mission-quote" data-i18n="mission_quote" style="color: #ffffff;">
      Стать надежным мостом на пути к <span style="color: #9830D5;">осознанности</span>, <span style="color: #9830D5;">трансформации</span> и возвращению к своей подлинной природе.
    </div>"""

new_html = """    <div class="mission-quote" data-i18n="mission_quote" style="color: #ffffff; max-width: 900px;">
      Создавать пространство, в котором человек может остановиться, услышать себя, обрести ясность и сделать шаг к глубокой <span style="color: #9830D5;">внутренней трансформации</span>.
    </div>"""

content = content.replace(old_html, new_html)
# In case spacing was off in HTML:
content = re.sub(r'<div class="mission-quote" data-i18n="mission_quote" style="color: #ffffff;">\s*Стать надежным мостом.*?\s*</div>', new_html, content, flags=re.DOTALL)


# Update JS Dictionary
lines = content.split('\n')
in_ru = in_en = in_tr = False

for i, line in enumerate(lines):
    if 'ru: {' in line:
        in_ru = True; in_en = False; in_tr = False
    elif 'en: {' in line:
        in_en = True; in_ru = False; in_tr = False
    elif 'tr: {' in line:
        in_tr = True; in_ru = False; in_en = False
    
    if "mission_quote:" in line:
        if in_ru:
            lines[i] = re.sub(r"mission_quote:\s*'.*?'", "mission_quote: 'Создавать пространство, в котором человек может остановиться, услышать себя, обрести ясность и сделать шаг к глубокой <span style=\"color: #9830D5;\">внутренней трансформации</span>.'", line)
        elif in_en:
            lines[i] = re.sub(r"mission_quote:\s*'.*?'", "mission_quote: 'To create a space where a person can stop, hear themselves, gain clarity, and take a step towards deep <span style=\"color: #9830D5;\">inner transformation</span>.'", line)
        elif in_tr:
            lines[i] = re.sub(r"mission_quote:\s*'.*?'", "mission_quote: 'Kişinin durabileceği, kendini duyabileceği, netlik kazanabileceği ve derin bir <span style=\"color: #9830D5;\">içsel dönüşüme</span> adım atabileceği bir alan yaratmak.'", line)

content = '\n'.join(lines)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mission quote updated.")
