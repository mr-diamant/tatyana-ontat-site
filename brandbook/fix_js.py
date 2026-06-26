import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the duplicate `};` at the end of T object
content = re.sub(r'\}\s*;\s*\}\s*;\s*function setLang', '};\n\n    function setLang', content)

# Fix the setLang function to handle RU, EN, TR
old_setLang = """    function setLang(lang) {
      const dict = T[lang];
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key] !== undefined) el.innerHTML = dict[key];
      });
      // Desktop buttons
      document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.textContent === lang.toUpperCase());
      });
      // Mobile buttons
      const mbRu = document.getElementById('mob-btn-ru');
      const mbKz = document.getElementById('mob-btn-kz');
      if (mbRu) mbRu.classList.toggle('active', lang === 'ru');
      if (mbKz) mbKz.classList.toggle('active', lang === 'kz');

      document.documentElement.lang = lang === 'kz' ? 'kk' : 'ru';
      localStorage.setItem('fg_lang', lang);
      // Close mobile menu on language switch
      document.getElementById('mob-nav-btn')?.classList.remove('open');
      document.getElementById('mob-nav-menu')?.classList.remove('open');
    }"""

new_setLang = """    function setLang(lang) {
      const dict = T[lang];
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key] !== undefined) el.innerHTML = dict[key];
      });
      // Desktop buttons
      document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.textContent === lang.toUpperCase());
      });
      // Mobile buttons
      const mbRu = document.getElementById('mob-btn-ru');
      const mbEn = document.getElementById('mob-btn-en');
      const mbTr = document.getElementById('mob-btn-tr');
      if (mbRu) mbRu.classList.toggle('active', lang === 'ru');
      if (mbEn) mbEn.classList.toggle('active', lang === 'en');
      if (mbTr) mbTr.classList.toggle('active', lang === 'tr');

      document.documentElement.lang = lang;
      localStorage.setItem('fg_lang', lang);
      // Close mobile menu on language switch
      document.getElementById('mob-nav-btn')?.classList.remove('open');
      document.getElementById('mob-nav-menu')?.classList.remove('open');
    }"""

content = content.replace(old_setLang, new_setLang)

# What if `old_setLang` didn't match perfectly? Let's check.
if old_setLang not in content:
    print("WARNING: old_setLang not found! Doing a regex replacement instead.")
    content = re.sub(r'function setLang\(lang\)\s*\{.*?\}(?=\s*// Init)', new_setLang, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("JS syntax fixed.")
