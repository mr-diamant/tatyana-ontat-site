import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Renumber sections in HTML and JS
# Old 02 to 10 should become 01 to 09
replacements = {
    '02': '01',
    '03': '02',
    '04': '03',
    '05': '04',
    '06': '05',
    '07': '06',
    '08': '07',
    '09': '08',
    '10': '09'
}

# Update nav-num in mob-nav-menu
for old, new in replacements.items():
    content = content.replace(f'<span class="nav-num">{old}</span>', f'<span class="nav-num">{new}</span>')
    content = content.replace(f'{old} — ', f'{new} — ')
    content = content.replace(f'{old}.1 — ', f'{new}.1 — ')

# Replace logo description in HTML
logo_html_old = """      <div class="logo-info">
        <div class="logo-element">
          <h4 data-i18n="le1_title">Глобус · Символ охвата</h4>
          <p data-i18n="le1_text">Сфера с горизонтальными линиями — это глобус, символ широкого охвата знаний, глобального финансового мышления и системного подхода к деньгам.</p>
        </div>
        <div class="logo-element">
          <h4 data-i18n="le2_title">Горизонтальные линии · Уровни</h4>
          <p data-i18n="le2_text">Параллельные линии символизируют структурированность, уровни финансовой грамотности и путь клиента — от базового понимания к мастерству.</p>
        </div>
        <div class="logo-element">
          <h4 data-i18n="le3_title">Золотой градиент · Ценность</h4>
          <p data-i18n="le3_text">Золото — универсальный символ ценности, богатства и качества. Переливающийся градиент передаёт динамику роста и премиальность услуг.</p>
        </div>
        <div class="logo-element">
          <h4 data-i18n="le4_title">Зелёный шрифт · Рост</h4>
          <p data-i18n="le4_text">Зелёный цвет (#9830D5) — цвет роста, стабильности и доверия. Сочетание с золотом создаёт баланс между надёжностью и процветанием.</p>
        </div>
      </div>"""

logo_html_new = """      <div class="logo-info">
        <div class="logo-element">
          <h4 data-i18n="le1_title">Имя эксперта</h4>
          <p data-i18n="le1_text">Татьяна Онтюрклер</p>
        </div>
      </div>"""

if logo_html_old in content:
    content = content.replace(logo_html_old, logo_html_new)
else:
    # Just in case whitespace is different
    content = re.sub(r'<div class="logo-info">.*?</div>\s*</div>\s*<!-- Versions -->', logo_html_new + '\n    </div>\n\n    <!-- Versions -->', content, flags=re.DOTALL)

# Update JS strings for le1_title and le1_text
content = re.sub(r"le1_title:\s*'.*?',", "le1_title: 'Имя эксперта',", content)
content = re.sub(r"le1_text:\s*'.*?',", "le1_text: 'Татьяна Онтюрклер',", content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
