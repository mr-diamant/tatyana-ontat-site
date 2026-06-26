import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. "Правила использования"
old_typo = '<div style="font-size: 11px; font-weight: 700; letter-spacing: 4px; text-transform: uppercase; color: var(--gold-light); margin-bottom: 30px;" data-i18n="typo_rules_title">Правила использования</div>'
new_typo = '<div style="font-size: 11px; font-weight: 700; letter-spacing: 4px; text-transform: uppercase; color: #9830D5; margin-bottom: 30px;" data-i18n="typo_rules_title">Правила использования</div>'
content = content.replace(old_typo, new_typo)

# 2. "Рекомендуется к регистрации"
old_rec = '<div style="font-size: 11px; font-weight: 700; letter-spacing: 5px; text-transform: uppercase; color: var(--gold-light); margin-bottom: 20px; position: relative;" data-i18n="s09_rec">Рекомендуется к регистрации</div>'
new_rec = '<div style="font-size: 11px; font-weight: 700; letter-spacing: 5px; text-transform: uppercase; color: #9830D5; margin-bottom: 20px; position: relative;" data-i18n="s09_rec">Рекомендуется к регистрации</div>'
content = content.replace(old_rec, new_rec)

# 3. Footer Headings (Телефон, Instagram, Email)
# They look like: <div style="font-size: 10px; font-weight: 700; letter-spacing: 4px; text-transform: uppercase; color: var(--gold-light); margin-bottom: 12px;" ...
old_footer = 'font-size: 10px; font-weight: 700; letter-spacing: 4px; text-transform: uppercase; color: var(--gold-light); margin-bottom: 12px;'
new_footer = 'font-size: 10px; font-weight: 700; letter-spacing: 4px; text-transform: uppercase; color: #ffffff; opacity: 0.8; margin-bottom: 12px;'
content = content.replace(old_footer, new_footer)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Headings updated.")
