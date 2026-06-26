import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add @font-face
font_face_code = """
    @font-face {
      font-family: 'Compacta BT Cyr';
      src: url('compacta.ttf') format('truetype');
    }
    @font-face {
      font-family: 'Bella Script Cyr';
      src: url('bella.ttf') format('truetype');
    }
"""
if "@font-face {" not in content:
    content = content.replace("@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&display=swap');", 
                              "@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&display=swap');\n" + font_face_code)

# 2. Replace Typography HTML layout
old_typo_html = """        <div style="display: flex; align-items: baseline; gap: 20px; margin-bottom: 10px; flex-wrap: wrap;">
          <span class="font-name-big" style="font-size: 90px; font-weight: 800; color: var(--green-dark); line-height: 1; letter-spacing: -3px;">Montserrat</span>
        </div>
        <div style="font-size: 13px; letter-spacing: 4px; text-transform: uppercase; color: #aaa; margin-bottom: 50px;" data-i18n="font_sub">Google Fonts · Бесплатный · Кириллица · Казахский · Латиница</div>"""

new_typo_html = """        <div style="display: flex; flex-direction: column; gap: 40px; margin-bottom: 50px;">
          <!-- Compacta -->
          <div>
            <div style="font-family: 'Compacta BT Cyr', sans-serif; font-size: 90px; color: var(--green-dark); line-height: 1; margin-bottom: 10px;">Compacta BT Cyr</div>
            <div style="font-size: 13px; letter-spacing: 4px; text-transform: uppercase; color: #aaa;" data-i18n="font_sub_compacta">Логотип (Имя)</div>
          </div>
          
          <!-- Bella -->
          <div>
            <div style="font-family: 'Bella Script Cyr', cursive; font-size: 90px; color: var(--green-dark); line-height: 1; margin-bottom: 10px;">Bella Script Cyr</div>
            <div style="font-size: 13px; letter-spacing: 4px; text-transform: uppercase; color: #aaa;" data-i18n="font_sub_bella">Логотип (Фамилия)</div>
          </div>

          <!-- Montserrat -->
          <div>
            <div class="font-name-big" style="font-family: 'Montserrat', sans-serif; font-size: 90px; font-weight: 800; color: var(--green-dark); line-height: 1; letter-spacing: -3px; margin-bottom: 10px;">Montserrat</div>
            <div style="font-size: 13px; letter-spacing: 4px; text-transform: uppercase; color: #aaa;" data-i18n="font_sub">Основной шрифт (Google Fonts · Бесплатный · Кириллица · Латиница)</div>
          </div>
        </div>"""

content = content.replace(old_typo_html, new_typo_html)

# 3. Add JS keys
ru_js = "font_sub: 'Google Fonts · Бесплатный · Кириллица · Казахский · Латиница',"
new_ru_js = """font_sub: 'Основной шрифт (Google Fonts · Бесплатный · Кириллица · Латиница)',
        font_sub_compacta: 'Логотип (Имя)',
        font_sub_bella: 'Логотип (Фамилия)',"""

kz_js = "font_sub: 'Google Fonts · Тегін · Кириллица · Қазақша · Латынша',"
new_kz_js = """font_sub: 'Негізгі қаріп (Google Fonts · Тегін · Кириллица · Латынша)',
        font_sub_compacta: 'Логотип (Аты)',
        font_sub_bella: 'Логотип (Тегі)',"""

content = content.replace(ru_js, new_ru_js)
content = content.replace(kz_js, new_kz_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
