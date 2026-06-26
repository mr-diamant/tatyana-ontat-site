import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

updates = {
    's02_tag': ('01 — Логотип', '01 — Logo', '01 — Logo'),
    's021_tag': ('02 — Иконка', '02 — Icon', '02 — İkon'),
    's04_tag': ('03 — Типографика', '03 — Typography', '03 — Tipografi'),
    's03_tag': ('04 — Цвета', '04 — Colors', '04 — Renkler'),
    's06_tag': ('05 — Эксперт', '05 — Expert', '05 — Uzman'),
    's00_tag': ('06 — Целевая аудитория', '06 — Target Audience', '06 — Hedef Kitle'),
    's07_tag': ('07 — Применение', '07 — Application', '07 — Uygulama'),
    's08_tag': ('08 — Запрещённые использования', '08 — Prohibited uses', '08 — Yasaklanmış kullanımlar'),
    's09_tag': ('09 — Цифровое присутствие', '09 — Digital presence', '09 — Dijital Varlık')
}

for key, (ru, en, tr) in updates.items():
    content = re.sub(rf'(data-i18n="{key}">)(.*?)(</div>)', rf'\g<1>{ru}\g<3>', content)

lines = content.split('\n')
in_ru = False
in_en = False
in_tr = False

for i, line in enumerate(lines):
    if 'ru: {' in line:
        in_ru = True; in_en = False; in_tr = False
    elif 'en: {' in line:
        in_en = True; in_ru = False; in_tr = False
    elif 'tr: {' in line:
        in_tr = True; in_ru = False; in_en = False
    
    for key, (ru, en, tr) in updates.items():
        if f"{key}:" in line:
            if in_ru:
                lines[i] = re.sub(rf"{key}:\s*'.*?'", f"{key}: '{ru}'", line)
            elif in_en:
                lines[i] = re.sub(rf"{key}:\s*'.*?'", f"{key}: '{en}'", line)
            elif in_tr:
                lines[i] = re.sub(rf"{key}:\s*'.*?'", f"{key}: '{tr}'", line)

content = '\n'.join(lines)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Numbering updated!")
