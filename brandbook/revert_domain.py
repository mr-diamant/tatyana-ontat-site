with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Revert all standard occurrences
content = content.replace('Ontyurkler-TV.ru', 'ontat.ru')

# Revert the large display title
content = content.replace('Ontyurkler-TV<span style="color: #9830D5;">.ru</span>', 'ontat<span style="color: #9830D5;">.ru</span>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Domain reverted to ontat.ru everywhere.")
