import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace variables in :root
content = re.sub(r'--green:\s*#[a-f0-9]+;', '--green: #9830D5;', content, flags=re.IGNORECASE)
content = re.sub(r'--green-dark:\s*#[a-f0-9]+;', '--green-dark: #000000;', content, flags=re.IGNORECASE)
content = re.sub(r'--green-light:\s*#[a-f0-9]+;', '--green-light: #b050f0;', content, flags=re.IGNORECASE)

content = re.sub(r'--gold:\s*#[a-f0-9]+;', '--gold: #000000;', content, flags=re.IGNORECASE)
content = re.sub(r'--gold-light:\s*#[a-f0-9]+;', '--gold-light: #333333;', content, flags=re.IGNORECASE)
content = re.sub(r'--gold-dark:\s*#[a-f0-9]+;', '--gold-dark: #000000;', content, flags=re.IGNORECASE)

# Replace logos
content = re.sub(r'https://finguide\.kz/page/brandbook/logo_t\.webp', 'logo2.png', content)
content = re.sub(r'https://finguide\.kz/page/brandbook/logo_w\.jpg', 'logo2.png', content)
content = re.sub(r'https://finguide\.kz/page/brandbook/logo_b\.jpg', 'logo1.png', content)
content = re.sub(r'https://finguide\.kz/page/brandbook/logo\.jpg', 'logo2.png', content)
content = re.sub(r'https://finguide\.kz/page/brandbook/menu_logo\.png', 'logo1.png', content)
content = re.sub(r'https://finguide\.kz/page/brandbook/icon\.png', 'logo2.png', content)

# Replace specific hardcoded colors
content = content.replace('#43795e', '#9830D5').replace('#43795E', '#9830D5')
content = content.replace('#2d5240', '#000000').replace('#2D5240', '#000000')
content = content.replace('#1a2e24', '#000000').replace('#1A2E24', '#000000')
content = content.replace('rgba(26,46,36,', 'rgba(0,0,0,')
content = content.replace('#c9a84c', '#000000').replace('#C9A84C', '#000000')
content = content.replace('#e8c96a', '#333333').replace('#E8C96A', '#333333')
content = content.replace('#a07830', '#000000').replace('#A07830', '#000000')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
