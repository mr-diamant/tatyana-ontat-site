import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. HTML Replacement
old_expert_html = """        <div style="position: relative;">
          <div style="aspect-ratio: 3/4; overflow: hidden; background: var(--light-gray);">
            <img src="https://finguide.kz/page/brandbook/ainur.jpg" alt="Айнур Рысмаганбетова" style="width: 100%; height: 100%; object-fit: cover; object-position: top;" />
          </div>
          <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 20px 24px; background: linear-gradient(transparent, rgba(0,0,0,0.85));">
            <div style="font-size: 10px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: var(--gold-light);">Айнур Рысмаганбетова</div>
          </div>
        </div>
        <div>
          <div class="expert-name" data-i18n="expert_name">Рысмаганбетова<br/>Айнур Сериковна</div>
          <div class="expert-title" data-i18n="expert_role">Профессиональный бухгалтер · Финансовый коуч · Налоговый эксперт</div>
          <p class="expert-bio" data-i18n="expert_bio">Более 20 лет практики в области бухгалтерского учёта, налогообложения и финансового консалтинга. Автор трансформационной игры по финансовой грамотности. Помогает предпринимателям и частным лицам наладить осознанные отношения с деньгами.</p>
          <ul class="certs-list" style="margin-bottom: 40px;">
            <li><span class="cert-tag">CAP</span> Certified Accounting Practitioner</li>
            <li><span class="cert-tag">CIPA</span> Certified International Professional Accountant</li>
            <li><span class="cert-tag">ICU</span> <span data-i18n="cert_icu">Профессиональный коуч — Международная Ассоциация ICU</span></li>
            <li><span class="cert-tag">ПБ</span> <span data-i18n="cert_pb">Сертификат Профессионального Бухгалтера</span></li>
          </ul>
          <div class="stats-grid">
            <div class="stat-box">
              <div class="stat-number">20+</div>
              <div class="stat-label" data-i18n="stat1">лет в профессии</div>
            </div>
            <div class="stat-box">
              <div class="stat-number">4</div>
              <div class="stat-label" data-i18n="stat2">международных сертификата</div>
            </div>
            <div class="stat-box">
              <div class="stat-number">3</div>
              <div class="stat-label" data-i18n="stat3">направления экспертизы</div>
            </div>
            <div class="stat-box">
              <div class="stat-number">1</div>
              <div class="stat-label" data-i18n="stat4">трансформационная игра</div>
            </div>
          </div>
        </div>"""

new_expert_html = """        <div style="position: relative;">
          <div style="aspect-ratio: 3/4; overflow: hidden; background: var(--light-gray);">
            <!-- Placeholder photo or current one, but alt text updated -->
            <img src="logo1.png" alt="Татьяна Онтюрклер" style="width: 100%; height: 100%; object-fit: cover; object-position: center; padding: 40px; background: #111;" />
          </div>
          <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 20px 24px; background: linear-gradient(transparent, rgba(0,0,0,0.85));">
            <div style="font-size: 10px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: var(--gold-light);">Татьяна Онтюрклер</div>
          </div>
        </div>
        <div>
          <div class="expert-name" data-i18n="expert_name">Онтюрклер<br/>Татьяна</div>
          <div class="expert-title" data-i18n="expert_role" style="font-size: 15px; letter-spacing: 3px; line-height: 1.6; margin-bottom: 30px; font-weight: 600; color: var(--green);">Трансперсональный психолог · Нумеролог · Автор выездных программ</div>
          
          <p class="expert-bio" style="margin-bottom: 20px; font-size: 14px; line-height: 1.8; color: #444;" data-i18n="expert_bio_1">В своей работе я помогаю людям глубже понимать свою природу, видеть смысл происходящих событий и находить внутреннюю опору в периоды перемен. Мой подход объединяет психологию, трансперсональные методы самопознания, нумерологию и практики осознанности.</p>
          
          <p class="expert-bio" style="font-size: 14px; line-height: 1.8; color: #444;" data-i18n="expert_bio_2">Помимо индивидуальной работы, я создаю выездные программы и ретриты, где участники могут восстановить внутренний ресурс и встретиться с собой настоящими. Для меня работа с человеком — это сопровождение на пути осознанности и раскрытия своей подлинной природы.</p>
        </div>"""

content = content.replace(old_expert_html, new_expert_html)

# 2. Update JS Dict entries (doing it via string replace for ru, en, tr since they're cloned)
old_js_expert = """        expert_name: 'Рысмаганбетова<br/>Айнур Сериковна',
        expert_role: 'Профессиональный бухгалтер · Финансовый коуч · Налоговый эксперт',
        expert_bio: 'Более 20 лет практики в области бухгалтерского учёта, налогообложения и финансового консалтинга. Автор трансформационной игры по финансовой грамотности. Помогает предпринимателям и частным лицам наладить осознанные отношения с деньгами.',
        cert_icu: 'Профессиональный коуч — Международная Ассоциация ICU',
        cert_pb: 'Сертификат Профессионального Бухгалтера',
        stat1: 'лет в профессии',
        stat2: 'международных сертификата',
        stat3: 'направления экспертизы',
        stat4: 'трансформационная игра',"""

new_js_expert = """        expert_name: 'Онтюрклер<br/>Татьяна',
        expert_role: 'Трансперсональный психолог · Нумеролог · Автор выездных программ',
        expert_bio_1: 'В своей работе я помогаю людям глубже понимать свою природу, видеть смысл происходящих событий и находить внутреннюю опору в периоды перемен. Мой подход объединяет психологию, трансперсональные методы самопознания, нумерологию и практики осознанности.',
        expert_bio_2: 'Помимо индивидуальной работы, я создаю выездные программы и ретриты, где участники могут восстановить внутренний ресурс и встретиться с собой настоящими. Для меня работа с человеком — это сопровождение на пути осознанности и раскрытия своей подлинной природы.',"""

content = content.replace(old_js_expert, new_js_expert)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Expert block updated.")
