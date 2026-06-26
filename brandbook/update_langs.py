import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
css_old_desktop = "    .lang-btn.active {\n      background: var(--gold);\n      color: #1a1a1a;\n      border-color: var(--gold);\n    }"
css_new_desktop = "    .lang-btn.active {\n      background: var(--gold);\n      color: #ffffff;\n      border-color: var(--gold);\n    }"
content = content.replace(css_old_desktop, css_new_desktop)

css_old_mobile = "      .mob-lang-btn.active { background: var(--gold); color: #1a1a1a; border-color: var(--gold); }"
css_new_mobile = "      .mob-lang-btn.active { background: var(--gold); color: #ffffff; border-color: var(--gold); }"
content = content.replace(css_old_mobile, css_new_mobile)

# 2. Update HTML Desktop Lang Switcher
html_old_desktop = """    <button class="lang-btn active" onclick="setLang('ru')">RU</button>
    <button class="lang-btn" onclick="setLang('kz')">KZ</button>"""

html_new_desktop = """    <button class="lang-btn active" onclick="setLang('ru')">RU</button>
    <button class="lang-btn" onclick="setLang('en')">EN</button>
    <button class="lang-btn" onclick="setLang('tr')">TR</button>"""
content = content.replace(html_old_desktop, html_new_desktop)

# 3. Update HTML Mobile Lang Switcher
html_old_mobile = """        <button class="mob-lang-btn active" id="mob-btn-ru" onclick="setLang('ru')">RU</button>
        <button class="mob-lang-btn" id="mob-btn-kz" onclick="setLang('kz')">KZ</button>"""

html_new_mobile = """        <button class="mob-lang-btn active" id="mob-btn-ru" onclick="setLang('ru')">RU</button>
        <button class="mob-lang-btn" id="mob-btn-en" onclick="setLang('en')">EN</button>
        <button class="mob-lang-btn" id="mob-btn-tr" onclick="setLang('tr')">TR</button>"""
content = content.replace(html_old_mobile, html_new_mobile)

# 4. Update JS Buttons logic (mobile)
js_old_mob = """      document.getElementById('mob-btn-ru').classList.remove('active');
      document.getElementById('mob-btn-kz').classList.remove('active');
      document.getElementById('mob-btn-' + lang).classList.add('active');"""

js_new_mob = """      document.getElementById('mob-btn-ru').classList.remove('active');
      document.getElementById('mob-btn-en').classList.remove('active');
      document.getElementById('mob-btn-tr').classList.remove('active');
      document.getElementById('mob-btn-' + lang).classList.add('active');"""
content = content.replace(js_old_mob, js_new_mob)

# 5. Extract 'ru' block and replace 'kz' block with 'en' and 'tr'
ru_start = content.find('ru: {')
kz_start = content.find('kz: {')

if ru_start != -1 and kz_start != -1:
    ru_end = content.find('      },', ru_start)
    ru_block = content[ru_start:ru_end+7]
    
    # We will just replace kz block with en and tr blocks (copy of ru)
    en_block = ru_block.replace('ru: {', 'en: {')
    tr_block = ru_block.replace('ru: {', 'tr: {')
    
    # We will remove kz block and insert en and tr
    # Find the end of kz block
    kz_end = content.find('      }', kz_start) + 7
    
    content = content[:kz_start] + en_block + '\n' + tr_block + '\n' + content[kz_end:]


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Lang logic updated.")
