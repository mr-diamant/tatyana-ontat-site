with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all occurrences of ontat.ru
content = content.replace('ontat.ru', 'Ontyurkler-TV.ru')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Domain updated to Ontyurkler-TV.ru everywhere.")
