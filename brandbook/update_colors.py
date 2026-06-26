import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the section tag from 02 to 03 in HTML
content = content.replace('data-i18n="s03_tag">02 — Цвета</div>', 'data-i18n="s03_tag">03 — Цвета</div>')
content = content.replace("s03_tag: '02 — Цвета',", "s03_tag: '03 — Цвета',")

# HTML layout replacement for color swatches
old_colors_html = """      <div class="color-palette">
        <div class="color-swatch">
          <div class="color-block" style="background: #9830D5;"></div>
          <div class="color-meta">
            <div class="color-name">Forest Green</div>
            <div class="color-hex">#9830D5</div>
            <div class="color-role" data-i18n="c1_role">Основной</div>
          </div>
        </div>
        <div class="color-swatch">
          <div class="color-block" style="background: linear-gradient(135deg, #000000, #333333, #000000);"></div>
          <div class="color-meta">
            <div class="color-name">Gold Gradient</div>
            <div class="color-hex">#000000 → #333333</div>
            <div class="color-role" data-i18n="c2_role">Акцентный</div>
          </div>
        </div>
        <div class="color-swatch">
          <div class="color-block" style="background: #000000;"></div>
          <div class="color-meta">
            <div class="color-name">Deep Forest</div>
            <div class="color-hex">#000000</div>
            <div class="color-role" data-i18n="c3_role">Тёмный вариант</div>
          </div>
        </div>
        <div class="color-swatch">
          <div class="color-block" style="background: #f8f6f1;"></div>
          <div class="color-meta">
            <div class="color-name">Warm White</div>
            <div class="color-hex">#F8F6F1</div>
            <div class="color-role" data-i18n="c4_role">Фоновый</div>
          </div>
        </div>
      </div>
      <div class="color-meaning">
        <div class="color-meaning-item">
          <div class="color-dot" style="background: #9830D5;"></div>
          <h4 data-i18n="cm1_title">Зелёный — доверие и рост</h4>
          <p data-i18n="cm1_text">Профессиональный зелёный передаёт стабильность, надёжность и уверенность. Ассоциируется с ростом капитала и финансовым здоровьем.</p>
        </div>
        <div class="color-meaning-item">
          <div class="color-dot" style="background: linear-gradient(135deg, #000000, #333333);"></div>
          <h4 data-i18n="cm2_title">Золото — ценность и экспертиза</h4>
          <p data-i18n="cm2_text">Золото — символ богатства, достижений и высокого стандарта. Переливающийся градиент подчёркивает динамику и движение к финансовой цели.</p>
        </div>
      </div>"""

new_colors_html = """      <div class="color-palette">
        <div class="color-swatch">
          <div class="color-block" style="background: #9830D5;"></div>
          <div class="color-meta">
            <div class="color-name">Vivid Purple</div>
            <div class="color-hex">#9830D5</div>
            <div class="color-role" data-i18n="c1_role">Основной</div>
          </div>
        </div>
        <div class="color-swatch">
          <div class="color-block" style="background: #000000;"></div>
          <div class="color-meta">
            <div class="color-name">Pure Black</div>
            <div class="color-hex">#000000</div>
            <div class="color-role" data-i18n="c2_role">Акцентный / Текст</div>
          </div>
        </div>
        <div class="color-swatch">
          <div class="color-block" style="background: #ffffff; border: 1px solid #eee;"></div>
          <div class="color-meta">
            <div class="color-name">Clean White</div>
            <div class="color-hex">#FFFFFF</div>
            <div class="color-role" data-i18n="c3_role">Фоновый</div>
          </div>
        </div>
      </div>
      <div class="color-meaning">
        <div class="color-meaning-item">
          <div class="color-dot" style="background: #9830D5;"></div>
          <h4 data-i18n="cm1_title">Фиолетовый — осознанность и глубина</h4>
          <p data-i18n="cm1_text">Глубокий фиолетовый цвет символизирует трансформацию, духовность и выход на новый уровень. Это цвет осознанности и внутреннего роста.</p>
        </div>
        <div class="color-meaning-item">
          <div class="color-dot" style="background: #000000;"></div>
          <h4 data-i18n="cm2_title">Чёрный — строгость и профессионализм</h4>
          <p data-i18n="cm2_text">Чёрный цвет создает сильный контраст, придает бренду премиальность, элегантность и стабильность.</p>
        </div>
      </div>"""

content = content.replace(old_colors_html, new_colors_html)

# JS Dictionary strings replacements (since they are identical in ru, en, tr, we can just replace globally)
content = content.replace("c2_role: 'Акцентный',", "c2_role: 'Акцентный / Текст',")
content = content.replace("c3_role: 'Тёмный вариант',", "c3_role: 'Фоновый',")

content = content.replace("cm1_title: 'Зелёный — доверие и рост',", "cm1_title: 'Фиолетовый — осознанность и глубина',")
content = content.replace("cm1_text: 'Профессиональный зелёный передаёт стабильность, надёжность и уверенность. Ассоциируется с ростом капитала и финансовым здоровьем.',", "cm1_text: 'Глубокий фиолетовый цвет символизирует трансформацию, духовность и выход на новый уровень. Это цвет осознанности и внутреннего роста.',")

content = content.replace("cm2_title: 'Золото — ценность и экспертиза',", "cm2_title: 'Чёрный — строгость и профессионализм',")
content = content.replace("cm2_text: 'Золото — символ богатства, достижений и высокого стандарта. Переливающийся градиент подчёркивает динамику и движение к финансовой цели.',", "cm2_text: 'Чёрный цвет создает сильный контраст, придает бренду премиальность, элегантность и стабильность.',")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Colors section updated successfully.")
