import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert gradient swatch before White
white_swatch = """        <div class="color-swatch">
          <div class="color-block" style="background: #ffffff; border: 1px solid #eee;"></div>"""

gradient_swatch = """        <div class="color-swatch">
          <div class="color-block" style="background: linear-gradient(135deg, #9830D5, #000000);"></div>
          <div class="color-meta">
            <div class="color-name">Purple Gradient</div>
            <div class="color-hex">#9830D5 → #000000</div>
            <div class="color-role" data-i18n="c4_role">Переходный градиент</div>
          </div>
        </div>
"""
content = content.replace(white_swatch, gradient_swatch + white_swatch)

# 2. Insert gradient meaning after Black
black_meaning = """        <div class="color-meaning-item">
          <div class="color-dot" style="background: #000000;"></div>
          <h4 data-i18n="cm2_title">Чёрный — строгость и профессионализм</h4>
          <p data-i18n="cm2_text">Чёрный цвет создает сильный контраст, придает бренду премиальность, элегантность и стабильность.</p>
        </div>"""

gradient_meaning = """
        <div class="color-meaning-item">
          <div class="color-dot" style="background: linear-gradient(135deg, #9830D5, #000000);"></div>
          <h4 data-i18n="cm3_title">Градиент — динамика и переход</h4>
          <p data-i18n="cm3_text">Плавный переход от насыщенного фиолетового к глубокому чёрному символизирует процесс трансформации и перетекание энергии.</p>
        </div>"""

content = content.replace(black_meaning, black_meaning + gradient_meaning)

# 3. Update JS dictionaries
cm2_js = "cm2_text: 'Чёрный цвет создает сильный контраст, придает бренду премиальность, элегантность и стабильность.',"
cm3_js = "        cm3_title: 'Градиент — динамика и переход',\n        cm3_text: 'Плавный переход от насыщенного фиолетового к глубокому чёрному символизирует процесс трансформации и перетекание энергии.',"

c3_js = "c3_role: 'Фоновый',"
c4_js = "        c4_role: 'Переходный градиент',"

# We will just replace all instances globally since ru, en, tr are identical
content = content.replace(cm2_js, cm2_js + "\n" + cm3_js)
content = content.replace(c3_js, c3_js + "\n" + c4_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Gradient added.")
