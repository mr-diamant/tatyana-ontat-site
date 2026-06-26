import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add HTML block
old_html = """        <div class="color-meaning-item">
          <div class="color-dot" style="background: linear-gradient(135deg, #9830D5, #000000);"></div>
          <h4 data-i18n="cm3_title">Градиент — динамика и переход</h4>
          <p data-i18n="cm3_text">Плавный переход от насыщенного фиолетового к глубокому чёрному символизирует процесс трансформации и перетекание энергии.</p>
        </div>
      </div>"""

new_html = """        <div class="color-meaning-item">
          <div class="color-dot" style="background: linear-gradient(135deg, #9830D5, #000000);"></div>
          <h4 data-i18n="cm3_title">Градиент — динамика и переход</h4>
          <p data-i18n="cm3_text">Плавный переход от насыщенного фиолетового к глубокому чёрному символизирует процесс трансформации и перетекание энергии.</p>
        </div>
        <div class="color-meaning-item">
          <div class="color-dot" style="background: #ffffff; border: 1px solid rgba(255,255,255,0.3);"></div>
          <h4 data-i18n="cm4_title">Белый — чистота и свобода</h4>
          <p data-i18n="cm4_text">Белый цвет выступает как пространство для дыхания. Он дает легкость, подчеркивает открытость и готовность к новому началу.</p>
        </div>
      </div>"""

content = content.replace(old_html, new_html)

# 2. Add to JS Dictionary
js_old = "cm3_text: 'Плавный переход от насыщенного фиолетового к глубокому чёрному символизирует процесс трансформации и перетекание энергии.',"
js_new = """cm3_text: 'Плавный переход от насыщенного фиолетового к глубокому чёрному символизирует процесс трансформации и перетекание энергии.',
        cm4_title: 'Белый — чистота и свобода',
        cm4_text: 'Белый цвет выступает как пространство для дыхания. Он дает легкость, подчеркивает открытость и готовность к новому началу.',"""

content = content.replace(js_old, js_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("White meaning added.")
