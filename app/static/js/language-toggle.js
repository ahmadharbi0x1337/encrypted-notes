document.addEventListener("DOMContentLoaded", function () {
  const langToggleBtn = document.getElementById("lang-toggle");
  const langLabel = document.getElementById("langLabel");

  let currentLang = localStorage.getItem("language") || "en";

  function applyLanguage(lang) {
    fetch('/static/lang/translations.json')
      .then(response => response.json())
      .then(translations => {
        const language = localStorage.getItem('language') || 'en';
        const elements = document.querySelectorAll('[data-i18n]');
        elements.forEach(el => {
          const key = el.getAttribute('data-i18n');
          let translation = translations[language][key];

          if (translation.includes('%username%')) {
            const username = el.getAttribute('data-username');
            translation = translation.replace('%username%', `<strong>${username}</strong>`);
            el.innerHTML = translation;
          } else {
            el.textContent = translation;
          }
      });
        // Set direction and label
        document.documentElement.dir = lang === "ar" ? "rtl" : "ltr";
        langLabel.textContent = lang === "ar" ? "English" : "عربي";
      });

    localStorage.setItem("language", lang);
  }

  langToggleBtn.addEventListener("click", () => {
    currentLang = currentLang === "en" ? "ar" : "en";
    applyLanguage(currentLang);
  });

  // Apply on load
  applyLanguage(currentLang);
});
