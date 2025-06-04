/* DARK MODE TOGGLE FUNCTIONALITY */
window.addEventListener("DOMContentLoaded", () => {
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "dark") {
    document.body.classList.add("dark-mode");
    themeIcon.classList.remove("fa-moon");
    themeIcon.classList.add("fa-sun");
  }
});

const toggleBtn = document.getElementById("themeToggle");
const themeIcon = document.getElementById("themeIcon");
const create_note = document.querySelector(".btnALIAS");

toggleBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");

  // Toggle icon
  if (document.body.classList.contains("dark-mode")) {
    themeIcon.classList.remove("fa-moon");
    themeIcon.classList.add("fa-sun");
    create_note.classList.remove("btn-success");
    create_note.classList.add("btn-secondary");

  } else {
    themeIcon.classList.remove("fa-sun");
    themeIcon.classList.add("fa-moon");
    create_note.classList.remove("btn-secondary");
    create_note.classList.add("btn-success");

  }

  // Save preference to localStorage
  localStorage.setItem("theme", document.body.classList.contains("dark-mode") ? "dark" : "light");
});



/* ARABIC LANGUAGE TOGGLE FUNCTIONALITY */
document.addEventListener("DOMContentLoaded", () => {
  const langToggle = document.getElementById("lang-toggle");
  const langLabel = document.getElementById("langLabel");
  const htmlTag = document.getElementById("htmlTag");
  // Load saved language from localStorage
  let currentLang = localStorage.getItem("language") || "en";
  applyLanguage(currentLang);
  langToggle.addEventListener("click", () => {
    currentLang = currentLang === "en" ? "ar" : "en";
    localStorage.setItem("language", currentLang);
    applyLanguage(currentLang);
  });
  function applyLanguage(lang) {
    if (lang === "ar") {
      htmlTag.setAttribute("lang", "ar");
      htmlTag.setAttribute("dir", "rtl");
      langLabel.textContent = "English";
      document.body.classList.add("rtl");
    } else {
      htmlTag.setAttribute("lang", "en");
      htmlTag.setAttribute("dir", "ltr");
      langLabel.textContent = "عربي";

      document.body.classList.remove("rtl");
    }
  }
});
