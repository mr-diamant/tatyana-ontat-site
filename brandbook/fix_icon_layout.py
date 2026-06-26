import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new icon block using the requested layout but with dark theme colors.
new_icon_block = """  <!-- ICON -->
  <div class="section-full" id="section-icon">
    <div class="section">
      <div class="section-tag" style="color: #9830D5;" data-i18n="s021_tag">02 — Иконка</div>
      <div class="section-title" style="margin-bottom: 40px;" data-i18n="s021_title">Графический символ</div>
      
      <div class="icon-main-grid">
        <div class="icon-previews">
          <div style="width: 280px; height: 280px; background: #000000; border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.5);">
            <div style="position: absolute; width: 200px; height: 200px; background: radial-gradient(circle, rgba(152,48,213,0.15) 0%, transparent 70%);"></div>
            <img src="tat.png" style="width: 160px; height: 160px; object-fit: contain; position: relative; z-index: 2; filter: drop-shadow(0 10px 20px rgba(0,0,0,0.5));" alt="Иконка" />
          </div>
        </div>
        <div>
          <p style="font-size: 16px; color: rgba(255,255,255,0.8); line-height: 1.9; margin-bottom: 40px;" data-i18n="icon_desc">Иконка — самостоятельный графический символ бренда. Золотой глобус с горизонтальными линиями на прозрачном фоне. Используется там, где полное название нецелесообразно или не помещается.</p>
          <div class="icon-desc-grid">
            <div style="padding: 24px; background: rgba(255,255,255,0.02); border-left: 3px solid #9830D5; border-radius: 0 4px 4px 0;">
              <div style="font-size: 11px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #9830D5; margin-bottom: 10px;" data-i18n="icon_d1_title">Цифровые носители</div>
              <p style="font-size: 13px; color: rgba(255,255,255,0.6); line-height: 1.7;" data-i18n="icon_d1_text">Favicon сайта, аватар в Instagram / Telegram / WhatsApp, иконка мобильного приложения, аватар почты.</p>
            </div>
            <div style="padding: 24px; background: rgba(255,255,255,0.02); border-left: 3px solid #9830D5; border-radius: 0 4px 4px 0;">
              <div style="font-size: 11px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #9830D5; margin-bottom: 10px;" data-i18n="icon_d2_title">Печать и упаковка</div>
              <p style="font-size: 13px; color: rgba(255,255,255,0.6); line-height: 1.7;" data-i18n="icon_d2_text">Штамп, наклейка, тиснение на обложке, водяной знак в документах, элемент оформления сертификатов.</p>
            </div>
            <div style="padding: 24px; background: rgba(255,255,255,0.02); border-left: 3px solid #9830D5; border-radius: 0 4px 4px 0;">
              <div style="font-size: 11px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #9830D5; margin-bottom: 10px;" data-i18n="icon_d3_title">Декоративный элемент</div>
              <p style="font-size: 13px; color: rgba(255,255,255,0.6); line-height: 1.7;" data-i18n="icon_d3_text">Паттерн на фоне презентаций, декор угла страницы, разделитель между блоками.</p>
            </div>
            <div style="padding: 24px; background: rgba(255,255,255,0.02); border-left: 3px solid #9830D5; border-radius: 0 4px 4px 0;">
              <div style="font-size: 11px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: #9830D5; margin-bottom: 10px;" data-i18n="icon_d4_title">Требования</div>
              <p style="font-size: 13px; color: rgba(255,255,255,0.6); line-height: 1.7;" data-i18n="icon_d4_text">Минимальный размер — 32×32 px. Не деформировать, не перекрашивать. Охранная зона — 20% от диаметра.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="page-indicator" data-i18n="page_indicator">Стокгольм · Стамбул · 2026</div>
  </div>"""

# Replace the current icon section
content = re.sub(r'  <!-- ICON -->\n  <div class="section-full" id="section-icon">.*?<div class="page-indicator" data-i18n="page_indicator">Стокгольм · Стамбул · 2026</div>\n  </div>', new_icon_block, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Icon section layout updated.")
