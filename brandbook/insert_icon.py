import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

icon_html = """  <div class="divider"></div>

  <!-- ICON -->
  <div class="section-full" id="section-icon">
    <div class="section">
      <div class="section-tag" style="color: #9830D5;" data-i18n="s021_tag">02 — Иконка</div>
      <div class="section-title" data-i18n="s021_title">Графический символ</div>
      <p class="section-desc" data-i18n="icon_desc" style="max-width: 800px;">Иконка — самостоятельный графический символ бренда. Используется там, где полное название нецелесообразно или не помещается.</p>
      
      <div style="background: var(--off-white); padding: 80px; text-align: center; margin-bottom: 50px;">
        <img src="tat.png" alt="Иконка" style="max-width: 200px; display: block; margin: 0 auto; filter: drop-shadow(0 10px 30px rgba(0,0,0,0.1));" />
      </div>

      <div class="grid-3" style="margin-top: 60px;">
        <div class="grid-item">
          <h4 data-i18n="icon_d1_title">Цифровые носители</h4>
          <p data-i18n="icon_d1_text">Favicon сайта, аватар в Instagram / Telegram / WhatsApp, иконка мобильного приложения, аватар почты.</p>
        </div>
        <div class="grid-item">
          <h4 data-i18n="icon_d2_title">Печать и упаковка</h4>
          <p data-i18n="icon_d2_text">Штамп, наклейка, тиснение на обложке, водяной знак в документах, элемент оформления сертификатов.</p>
        </div>
        <div class="grid-item">
          <h4 data-i18n="icon_d4_title">Требования</h4>
          <p data-i18n="icon_d4_text">Минимальный размер — 32×32 px. Не деформировать, не перекрашивать. Охранная зона — 20% от диаметра.</p>
        </div>
      </div>
    </div>
    <div class="page-indicator" data-i18n="page_indicator">Стокгольм · Стамбул · 2026</div>
  </div>"""

content = content.replace('  <!-- TYPOGRAPHY -->', icon_html + '\n\n  <!-- TYPOGRAPHY -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Icon section added.")
