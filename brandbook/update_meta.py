import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update meta
content = content.replace('<link rel="icon" type="image/png" href="logo2.png" />', '<link rel="icon" type="image/png" href="tat.png" />')
content = content.replace('<link rel="apple-touch-icon" href="logo2.png" />', '<link rel="apple-touch-icon" href="tat.png" />')
content = content.replace('<meta property="og:image" content="logo2.png" />', '<meta property="og:image" content="preview.webp" />')
content = content.replace('<meta name="twitter:image" content="logo2.png" />', '<meta name="twitter:image" content="preview.webp" />')

# 2. Update cover logo
old_cover = """    <div style="background: white; width: 340px; height: 340px; display: flex; align-items: center; justify-content: center; padding: 30px; border-radius: 4px; box-shadow: 0 8px 40px rgba(0,0,0,0.25); margin-bottom: 60px;">
      <img src="logo2.png" alt="Татьяна Онтюрклер" style="max-width: 280px; width: 100%; display: block;" />
    </div>"""

new_cover = """    <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 60px; padding: 0 20px;">
      <img src="logo11.png" alt="Татьяна Онтюрклер" style="max-width: 600px; width: 100%; display: block;" />
    </div>"""

content = content.replace(old_cover, new_cover)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Meta and Cover logo updated.")
