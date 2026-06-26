import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. HTML Title change
content = content.replace('Кому помогает FinGuide Expert', 'Кому помогает Татьяна Онтюрклер')

# 2. HTML Expert Role change
content = content.replace('Трансперсональный психолог · Нумеролог · Автор выездных программ', 'Психолог · Практик осознанности · Автор трансформационных программ')

# 3. HTML Bio changes
old_bio_html = """          <p class="expert-bio" style="margin-bottom: 20px; font-size: 14px; line-height: 1.8; color: #444;" data-i18n="expert_bio_1">В своей работе я помогаю людям глубже понимать свою природу, видеть смысл происходящих событий и находить внутреннюю опору в периоды перемен. Мой подход объединяет психологию, трансперсональные методы самопознания, нумерологию и practices осознанности.</p>
          
          <p class="expert-bio" style="font-size: 14px; line-height: 1.8; color: #444;" data-i18n="expert_bio_2">Помимо индивидуальной работы, я создаю выездные программы и ретриты, где участники могут восстановить внутренний ресурс и встретиться с собой настоящими. Для меня работа с человеком — это сопровождение на пути осознанности и раскрытия своей подлинной природы.</p>"""

# Wait, my old HTML regex string might be slightly off. Let's use re.sub for the bio block.
new_bio_html = """          <p class="expert-bio" style="margin-bottom: 20px; font-size: 14px; line-height: 1.8; color: rgba(255,255,255,0.8);" data-i18n="expert_bio_1">Ко мне приходят в моменты, когда теряется ясность, повторяются одни и те же жизненные сценарии или возникает ощущение, что жизнь требует внутренних перемен. Вместе мы ищем причины происходящего, восстанавливаем внутреннюю опору и находим направление дальнейшего пути.</p>
          
          <p class="expert-bio" style="margin-bottom: 20px; font-size: 14px; line-height: 1.8; color: rgba(255,255,255,0.8);" data-i18n="expert_bio_2">В работе я использую психологические методы, практики осознанности и нумерологический анализ как дополнительный инструмент самопознания.</p>

          <p class="expert-bio" style="font-size: 14px; line-height: 1.8; color: rgba(255,255,255,0.8);" data-i18n="expert_bio_3">Помимо индивидуальной работы, я создаю выездные программы и ретриты, где участники могут восстановить внутренний ресурс и встретиться с собой настоящими. Для меня работа с человеком — это сопровождение на пути осознанности и раскрытия своей подлинной природы.</p>"""

content = re.sub(r'<p class="expert-bio".*?data-i18n="expert_bio_1">.*?</p>\s*<p class="expert-bio".*?data-i18n="expert_bio_2">.*?</p>', new_bio_html, content, flags=re.DOTALL)

# Now JS Dictionary updates
lines = content.split('\n')
in_ru = in_en = in_tr = False

for i, line in enumerate(lines):
    if 'ru: {' in line:
        in_ru = True; in_en = False; in_tr = False
    elif 'en: {' in line:
        in_en = True; in_ru = False; in_tr = False
    elif 'tr: {' in line:
        in_tr = True; in_ru = False; in_en = False
    
    if in_ru:
        if "s00_title:" in line:
            lines[i] = re.sub(r"s00_title:\s*'.*?'", "s00_title: 'Кому помогает Татьяна Онтюрклер'", line)
        if "expert_role:" in line:
            lines[i] = re.sub(r"expert_role:\s*'.*?'", "expert_role: 'Психолог · Практик осознанности · Автор трансформационных программ'", line)
        if "expert_bio_1:" in line:
            lines[i] = re.sub(r"expert_bio_1:\s*'.*?'", "expert_bio_1: 'Ко мне приходят в моменты, когда теряется ясность, повторяются одни и те же жизненные сценарии или возникает ощущение, что жизнь требует внутренних перемен. Вместе мы ищем причины происходящего, восстанавливаем внутреннюю опору и находим направление дальнейшего пути.'", line)
        if "expert_bio_2:" in line:
            lines[i] = re.sub(r"expert_bio_2:\s*'.*?'", "expert_bio_2: 'В работе я использую психологические методы, практики осознанности и нумерологический анализ как дополнительный инструмент самопознания.',\n        expert_bio_3: 'Помимо индивидуальной работы, я создаю выездные программы и ретриты, где участники могут восстановить внутренний ресурс и встретиться с собой настоящими. Для меня работа с человеком — это сопровождение на пути осознанности и раскрытия своей подлинной природы.'", line)
            
    elif in_en:
        if "expert_role:" in line:
            lines[i] = re.sub(r"expert_role:\s*'.*?'", "expert_role: 'Psychologist · Mindfulness Practitioner · Author of transformational programs'", line)
        if "expert_bio_1:" in line:
            lines[i] = re.sub(r"expert_bio_1:\s*'.*?'", "expert_bio_1: 'People come to me in moments when clarity is lost, the same life scenarios repeat, or there is a feeling that life requires internal changes. Together we look for the causes of what is happening, restore internal support and find the direction of the future path.'", line)
        if "expert_bio_2:" in line:
            lines[i] = re.sub(r"expert_bio_2:\s*'.*?'", "expert_bio_2: 'In my work, I use psychological methods, mindfulness practices and numerological analysis as an additional tool for self-discovery.',\n        expert_bio_3: 'In addition to individual work, I create retreat programs where participants can restore their inner resources and meet their true selves. For me, working with a person is accompanying them on the path of awareness and revealing their true nature.'", line)

    elif in_tr:
        if "expert_role:" in line:
            lines[i] = re.sub(r"expert_role:\s*'.*?'", "expert_role: 'Psikolog · Farkındalık Uygulayıcısı · Dönüşüm programlarının yazarı'", line)
        if "expert_bio_1:" in line:
            lines[i] = re.sub(r"expert_bio_1:\s*'.*?'", "expert_bio_1: 'İnsanlar netliğin kaybolduğu, aynı yaşam senaryolarının tekrarlandığı veya hayatın içsel değişiklikler gerektirdiği hissine kapıldıkları anlarda bana gelirler. Birlikte olanların nedenlerini arar, içsel desteği geri yükler ve gelecekteki yolun yönünü buluruz.'", line)
        if "expert_bio_2:" in line:
            lines[i] = re.sub(r"expert_bio_2:\s*'.*?'", "expert_bio_2: 'Çalışmalarımda psikolojik yöntemleri, farkındalık uygulamalarını ve numerolojik analizi kendini keşfetmek için ek bir araç olarak kullanıyorum.',\n        expert_bio_3: 'Bireysel çalışmalara ek olarak, katılımcıların içsel kaynaklarını geri yükleyebilecekleri ve gerçek benlikleriyle tanışabilecekleri inziva programları oluşturuyorum. Benim için bir insanla çalışmak, onlara farkındalık yolunda eşlik etmek ve gerçek doğalarını ortaya çıkarmaktır.'", line)

content = '\n'.join(lines)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates completed.")
