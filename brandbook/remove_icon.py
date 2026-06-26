import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove mobile nav link
nav_link_pattern = r'\s*<a href="#section-icon".*?</a>\n'
content = re.sub(nav_link_pattern, '\n', content)

# 2. Remove ICON SECTION
icon_section_pattern = r'\s*<!-- ICON SECTION -->\s*<div id="section-icon".*?</div>\s*</div>\s*</div>'
# Because there are nested divs, regex might be tricky. Let's do string replacement from <!-- ICON SECTION --> to the end of the block.
icon_html_start = '  <!-- ICON SECTION -->'
icon_html_end = '<!-- DOWNLOADS -->'
start_idx = content.find(icon_html_start)
end_idx = content.find(icon_html_end)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + '  <!-- SECTION 02 ICON REMOVED -->\n\n  ' + content[end_idx:]

# 3. Renumber 03 to 09 down by 1
replacements = {
    '03': '02',
    '04': '03',
    '05': '04',
    '06': '05',
    '07': '06',
    '08': '07',
    '09': '08'
}

for old, new in replacements.items():
    content = content.replace(f'<span class="nav-num">{old}</span>', f'<span class="nav-num">{new}</span>')
    content = content.replace(f'{old} — ', f'{new} — ')
    # Also fix the JS object labels if they match
    content = content.replace(f"'{old} — ", f"'{new} — ")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Icon section removed and renumbered.")
