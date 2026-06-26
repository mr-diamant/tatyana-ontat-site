import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update HTML
old_audience_html = """      <h2 class="section-title" data-i18n="s00_title">Кому помогает FinGuide Expert</h2>
      <p style="font-size: 16px; color: var(--gray); max-width: 680px; line-height: 1.7; margin-bottom: 60px;" data-i18n="s00_desc">Бренд создан для трёх чётко определённых аудиторий — каждая со своей задачей и точкой входа.</p>
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px;" class="audience-grid">
        <!-- Segment 1 -->
        <div style="border: 1px solid var(--light-gray); border-radius: 4px; padding: 40px 32px; position: relative; overflow: hidden;">
          <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, var(--green), var(--green-light));"></div>
          <div style="font-size: 11px; font-weight: 700; letter-spacing: 4px; text-transform: uppercase; color: var(--green); margin-bottom: 20px;" data-i18n="aud1_num">01</div>
          <div style="font-size: 22px; font-weight: 800; color: #1a1a1a; margin-bottom: 16px; line-height: 1.3;" data-i18n="aud1_title">Начинающие и работающие бухгалтеры</div>
          <div style="width: 32px; height: 2px; background: var(--gold); margin-bottom: 20px;"></div>
          <p style="font-size: 14px; line-height: 1.75; color: var(--gray);" data-i18n="aud1_text">Девушки, обучающиеся на бухгалтера или уже работающие в профессии. Хотят повысить квалификацию, стать увереннее в налогах и стать настоящим экспертом — не просто исполнителем.</p>
          <div style="margin-top: 24px; padding-top: 24px; border-top: 1px solid var(--light-gray);">
            <div style="font-size: 11px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: var(--gray); margin-bottom: 10px;" data-i18n="aud_goal">Запрос</div>
            <div style="font-size: 13px; font-weight: 600; color: #1a1a1a;" data-i18n="aud1_goal">Рост экспертности · Профессиональное признание</div>
          </div>
        </div>
        <!-- Segment 2 -->
        <div style="border: 1px solid var(--light-gray); border-radius: 4px; padding: 40px 32px; position: relative; overflow: hidden; background: var(--green);">
          <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, var(--gold-dark), var(--gold-light));"></div>
          <div style="font-size: 11px; font-weight: 700; letter-spacing: 4px; text-transform: uppercase; color: var(--gold-light); margin-bottom: 20px;" data-i18n="aud2_num">02</div>
          <div style="font-size: 22px; font-weight: 800; color: #fff; margin-bottom: 16px; line-height: 1.3;" data-i18n="aud2_title">Состоявшиеся бизнесмены</div>
          <div style="width: 32px; height: 2px; background: var(--gold); margin-bottom: 20px;"></div>
          <p style="font-size: 14px; line-height: 1.75; color: rgba(255,255,255,0.75);" data-i18n="aud2_text">Владельцы бизнеса, у которых уже есть дело, но финансы ведутся хаотично. Хотят навести порядок в учёте, оптимизировать налоги и получить чёткое понимание финансового состояния компании.</p>
          <div style="margin-top: 24px; padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.15);">
            <div style="font-size: 11px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: rgba(255,255,255,0.5); margin-bottom: 10px;" data-i18n="aud_goal">Запрос</div>
            <div style="font-size: 13px; font-weight: 600; color: var(--gold-light);" data-i18n="aud2_goal">Порядок в финансах · Налоговая оптимизация</div>
          </div>
        </div>
        <!-- Segment 3 -->
        <div style="border: 1px solid var(--light-gray); border-radius: 4px; padding: 40px 32px; position: relative; overflow: hidden;">
          <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, var(--gold-dark), var(--gold-light));"></div>
          <div style="font-size: 11px; font-weight: 700; letter-spacing: 4px; text-transform: uppercase; color: var(--gold-dark); margin-bottom: 20px;" data-i18n="aud3_num">03</div>
          <div style="font-size: 22px; font-weight: 800; color: #1a1a1a; margin-bottom: 16px; line-height: 1.3;" data-i18n="aud3_title">Молодые предприниматели и стартаперы</div>
          <div style="width: 32px; height: 2px; background: var(--gold); margin-bottom: 20px;"></div>
          <p style="font-size: 14px; line-height: 1.75; color: var(--gray);" data-i18n="aud3_text">Начинающие предприниматели, которые только открывают своё дело. Хотят с самого старта выстроить финансовую грамотность: ИП, налоги, учёт — чтобы бизнес рос без болезненных ошибок.</p>
          <div style="margin-top: 24px; padding-top: 24px; border-top: 1px solid var(--light-gray);">
            <div style="font-size: 11px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: var(--gray); margin-bottom: 10px;" data-i18n="aud_goal">Запрос</div>
            <div style="font-size: 13px; font-weight: 600; color: #1a1a1a;" data-i18n="aud3_goal">Финграмотность с нуля · Правильный старт</div>
          </div>
        </div>
      </div>"""

new_audience_html = """      <h2 class="section-title" data-i18n="s00_title">Кому помогает Татьяна Онтюрклер</h2>
      <p style="font-size: 16px; color: var(--gray); max-width: 680px; line-height: 1.7; margin-bottom: 60px;" data-i18n="s00_desc">Программы и консультации созданы для трёх ключевых аудиторий — каждая со своим уникальным запросом.</p>
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px;" class="audience-grid">
        <!-- Segment 1 -->
        <div style="border: 1px solid var(--light-gray); border-radius: 4px; padding: 40px 32px; position: relative; overflow: hidden;">
          <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, var(--green), var(--green-light));"></div>
          <div style="font-size: 11px; font-weight: 700; letter-spacing: 4px; text-transform: uppercase; color: var(--green); margin-bottom: 20px;" data-i18n="aud1_num">01</div>
          <div style="font-size: 22px; font-weight: 800; color: #1a1a1a; margin-bottom: 16px; line-height: 1.3;" data-i18n="aud1_title">Люди в кризисе и поиске себя</div>
          <div style="width: 32px; height: 2px; background: var(--gold); margin-bottom: 20px;"></div>
          <p style="font-size: 14px; line-height: 1.75; color: var(--gray);" data-i18n="aud1_text">Те, кто переживает жизненные трудности, потерю ориентиров и поиск смысла. Люди, которые чувствуют, что живут не своей жизнью под влиянием страхов и ограничивающих убеждений.</p>
          <div style="margin-top: 24px; padding-top: 24px; border-top: 1px solid var(--light-gray);">
            <div style="font-size: 11px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: var(--gray); margin-bottom: 10px;" data-i18n="aud_goal">Запрос</div>
            <div style="font-size: 13px; font-weight: 600; color: #1a1a1a;" data-i18n="aud1_goal">Найти внутреннюю опору · Вернуть смысл</div>
          </div>
        </div>
        <!-- Segment 2 -->
        <div style="border: 1px solid var(--light-gray); border-radius: 4px; padding: 40px 32px; position: relative; overflow: hidden; background: var(--green);">
          <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, var(--gold-dark), var(--gold-light));"></div>
          <div style="font-size: 11px; font-weight: 700; letter-spacing: 4px; text-transform: uppercase; color: var(--gold-light); margin-bottom: 20px;" data-i18n="aud2_num">02</div>
          <div style="font-size: 22px; font-weight: 800; color: #fff; margin-bottom: 16px; line-height: 1.3;" data-i18n="aud2_title">Ищущие осознанность и трансформацию</div>
          <div style="width: 32px; height: 2px; background: var(--gold); margin-bottom: 20px;"></div>
          <p style="font-size: 14px; line-height: 1.75; color: rgba(255,255,255,0.75);" data-i18n="aud2_text">Те, кто хочет глубже понять свою природу, раскрыть внутренний потенциал и осознать свои истинные ценности. Для них важно не просто решить проблему, а выйти на новый уровень развития.</p>
          <div style="margin-top: 24px; padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.15);">
            <div style="font-size: 11px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: rgba(255,255,255,0.5); margin-bottom: 10px;" data-i18n="aud_goal">Запрос</div>
            <div style="font-size: 13px; font-weight: 600; color: var(--gold-light);" data-i18n="aud2_goal">Раскрытие потенциала · Духовный рост</div>
          </div>
        </div>
        <!-- Segment 3 -->
        <div style="border: 1px solid var(--light-gray); border-radius: 4px; padding: 40px 32px; position: relative; overflow: hidden;">
          <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, var(--gold-dark), var(--gold-light));"></div>
          <div style="font-size: 11px; font-weight: 700; letter-spacing: 4px; text-transform: uppercase; color: var(--gold-dark); margin-bottom: 20px;" data-i18n="aud3_num">03</div>
          <div style="font-size: 22px; font-weight: 800; color: #1a1a1a; margin-bottom: 16px; line-height: 1.3;" data-i18n="aud3_title">Уставшие от внешнего шума</div>
          <div style="width: 32px; height: 2px; background: var(--gold); margin-bottom: 20px;"></div>
          <p style="font-size: 14px; line-height: 1.75; color: var(--gray);" data-i18n="aud3_text">Люди, нуждающиеся в отдыхе и замедлении. Участники выездных программ и ретритов, которые хотят восстановить внутренний ресурс и встретиться с собой настоящими.</p>
          <div style="margin-top: 24px; padding-top: 24px; border-top: 1px solid var(--light-gray);">
            <div style="font-size: 11px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: var(--gray); margin-bottom: 10px;" data-i18n="aud_goal">Запрос</div>
            <div style="font-size: 13px; font-weight: 600; color: #1a1a1a;" data-i18n="aud3_goal">Восстановление ресурса · Замедление</div>
          </div>
        </div>
      </div>"""

content = content.replace(old_audience_html, new_audience_html)

# 2. JS dictionary replace
old_js_aud = """        s00_title: 'Кому помогает FinGuide Expert',
        s00_desc: 'Бренд создан для трёх чётко определённых аудиторий — каждая со своей задачей и точкой входа.',
        aud1_title: 'Начинающие и работающие бухгалтеры',
        aud1_text: 'Девушки, обучающиеся на бухгалтера или уже работающие в профессии. Хотят повысить квалификацию, стать увереннее в налогах и стать настоящим экспертом — не просто исполнителем.',
        aud1_goal: 'Рост экспертности · Профессиональное признание',
        aud2_title: 'Состоявшиеся бизнесмены',
        aud2_text: 'Владельцы бизнеса, у которых уже есть дело, но финансы ведутся хаотично. Хотят навести порядок в учёте, оптимизировать налоги и получить чёткое понимание финансового состояния компании.',
        aud2_goal: 'Порядок в финансах · Налоговая оптимизация',
        aud3_title: 'Молодые предприниматели и стартаперы',
        aud3_text: 'Начинающие предприниматели, которые только открывают своё дело. Хотят с самого старта выстроить финансовую грамотность: ИП, налоги, учёт — чтобы бизнес рос без болезненных ошибок.',
        aud3_goal: 'Финграмотность с нуля · Правильный старт',"""

new_js_aud = """        s00_title: 'Кому помогает Татьяна Онтюрклер',
        s00_desc: 'Программы и консультации созданы для трёх ключевых аудиторий — каждая со своим уникальным запросом.',
        aud1_title: 'Люди в кризисе и поиске себя',
        aud1_text: 'Те, кто переживает жизненные трудности, потерю ориентиров и поиск смысла. Люди, которые чувствуют, что живут не своей жизнью под влиянием страхов и ограничивающих убеждений.',
        aud1_goal: 'Найти внутреннюю опору · Вернуть смысл',
        aud2_title: 'Ищущие осознанность и трансформацию',
        aud2_text: 'Те, кто хочет глубже понять свою природу, раскрыть внутренний потенциал и осознать свои истинные ценности. Для них важно не просто решить проблему, а выйти на новый уровень развития.',
        aud2_goal: 'Раскрытие потенциала · Духовный рост',
        aud3_title: 'Уставшие от внешнего шума',
        aud3_text: 'Люди, нуждающиеся в отдыхе и замедлении. Участники выездных программ и ретритов, которые хотят восстановить внутренний ресурс и встретиться с собой настоящими.',
        aud3_goal: 'Восстановление ресурса · Замедление',"""

content = content.replace(old_js_aud, new_js_aud)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Audience block updated.")
