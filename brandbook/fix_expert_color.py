import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace white text with dark gray in expert-bio paragraphs
content = content.replace('class="expert-bio" style="margin-bottom: 20px; font-size: 14px; line-height: 1.8; color: rgba(255,255,255,0.8);"', 'class="expert-bio" style="margin-bottom: 20px; font-size: 14px; line-height: 1.8; color: #444;"')
content = content.replace('class="expert-bio" style="font-size: 14px; line-height: 1.8; color: rgba(255,255,255,0.8);"', 'class="expert-bio" style="font-size: 14px; line-height: 1.8; color: #444;"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Expert bio colors fixed.")
