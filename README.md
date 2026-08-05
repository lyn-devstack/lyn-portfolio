# 📁 Carolyn DevStack Portfolio

[![Vue 3](https://img.shields.io/badge/Vue%203-3.4.0-4FC08D?logo=vue.js&logoColor=white)](https://vuejs.org/)
[![Vite](https://img.shields.io/badge/Vite-5.2.0-646CFF?logo=vite&logoColor=white)](https://vitejs.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/lyn-devstack/lyn-portfolio?style=social)](https://github.com/lyn-devstack/lyn-portfolio)

---

## 🎨 Dual‑Personality Visuals

**Carolyn DevStack** is a personal portfolio that lives in two worlds:

| **Deep Space (Professional)** | **Nebulosa (Creative)** |
|---|---|
| Dark navy background (`#0a0f1e`) <br> Cool blue accent (`#4facfe`) <br> Crisp white text | Soft pastel pink background (`#f8eef2`) <br> Warm pink accent (`#ff4081`) <br> Dark plum‑ish text |
| Perfect for a sleek, business‑like presentation. | Ideal for a playful, artistic vibe.

The theme can be switched instantly with the toggle button in the top‑right corner:

```html
<button @click="toggleTheme" class="theme-toggle">
  {{ theme === 'pro' ? '💫 Nebula' : '🪐 Deep Space' }}
</button>
```

> The button shows **💫 Nebula** when the site is in *Creative* mode and **🪐 Deep Space** when in *Professional* mode.

---

## 📸 Visual Demo

Below you can see the toggle in action – the same page rendered side‑by‑side in both themes.



---

## 🚀 Getting Started

### Prerequisites
- **Node.js** (>= 18.x)
- **npm** (>= 9.x) – comes with Node


## 🛠️ Tech Stack
- **Vue 3** – Composition API & `<script setup>`
- **Vite** – Lightning‑fast bundler and dev server
- **Tailwind‑like utility classes** (custom CSS scoped per component)
- **i18n** – Bilingual (English / Español) support
- **Dynamic theming** – Global `theme` ref passed to every section, with deep CSS overrides for the *Creative* mode.

---

## 📄 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments
- Inspired by modern glassmorphism and dark‑mode designs.
- Icons courtesy of **Google Material Icons**.
- Color palette generated with **Coolors**.

Enjoy exploring both universes! 🚀
