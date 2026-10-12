<script setup>
import { ref, computed, watch, onMounted, onUnmounted, defineAsyncComponent } from 'vue'
import { useI18n } from 'vue-i18n'

// Three.js es la mayor parte del bundle: se carga aparte para que el contenido aparezca antes
const LogicCore = defineAsyncComponent(() => import('./components/LogicCore.vue'))

// Importación de Secciones Modularizadas
import HeroSection from './components/sections/HeroSection.vue'
import ExperienceSection from './components/sections/ExperienceSection.vue'
import ProjectsSection from './components/sections/ProjectsSection.vue'
import SkillsSection from './components/sections/SkillsSection.vue'
import ContactSection from './components/sections/ContactSection.vue'

// Estado Global
const scrollProgress = ref(0)
const scrolled = ref(false)
const menuOpen = ref(false)
const theme = ref('pro')
const { locale } = useI18n()

// Mantiene <html lang> sincronizado con el idioma elegido (lectores de pantalla, SEO)
watch(locale, (lang) => { document.documentElement.lang = lang }, { immediate: true })

const navLinks = [
  { id: 'experience', key: 'nav.experience' },
  { id: 'projects', key: 'nav.projects' },
  { id: 'skills', key: 'nav.skills' },
  { id: 'contact', key: 'nav.contact' }
]
const cvUrl = computed(() => `${import.meta.env.BASE_URL}cv/CV_Leslie_Carolyn_${locale.value.toUpperCase()}.pdf`)

const toggleTheme = () => {
  theme.value = theme.value === 'pro' ? 'creative' : 'pro'
}

const onScroll = () => {
  const h = document.documentElement
  scrollProgress.value = h.scrollTop / (h.scrollHeight - h.clientHeight)
  scrolled.value = h.scrollTop > 24
}

onMounted(() => window.addEventListener('scroll', onScroll, { passive: true }))
onUnmounted(() => window.removeEventListener('scroll', onScroll))
</script>

<template>
  <main :class="['main-container', theme]">

    <div class="canvas-background">
      <LogicCore :scrollProgress="scrollProgress" :theme="theme" />
    </div>

    <div class="content-layer">
      <header :class="['nav-container', { scrolled: scrolled || menuOpen }]">
        <a href="#top" class="brand" @click="menuOpen = false">
          Leslie <span>Carolyn</span>
        </a>

        <nav :class="['nav-links', { open: menuOpen }]" :aria-label="$t('nav.label')">
          <a v-for="link in navLinks" :key="link.id" :href="`#${link.id}`" @click="menuOpen = false">
            {{ $t(link.key) }}
          </a>
          <a :href="cvUrl" target="_blank" rel="noopener" class="nav-cv" @click="menuOpen = false">{{ $t('hero.ctaCv') }}</a>
        </nav>

        <div class="nav-controls">
          <button
            @click="toggleTheme"
            class="control-btn"
            :aria-label="theme === 'pro' ? $t('nav.lightTheme') : $t('nav.darkTheme')"
            :title="theme === 'pro' ? $t('nav.lightTheme') : $t('nav.darkTheme')"
          >
            <!-- Sol en modo oscuro (pasar a claro) y luna en modo claro (pasar a oscuro) -->
            <svg v-if="theme === 'pro'" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true">
              <circle cx="12" cy="12" r="4" />
              <path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4" />
            </svg>
            <svg v-else viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z" />
            </svg>
          </button>

          <div class="lang-group" role="group" :aria-label="$t('nav.language')">
            <button @click="$i18n.locale = 'es'" class="nav-btn" :class="{ active: $i18n.locale === 'es' }" :aria-pressed="$i18n.locale === 'es'">ES</button>
            <span class="divider" aria-hidden="true">|</span>
            <button @click="$i18n.locale = 'en'" class="nav-btn" :class="{ active: $i18n.locale === 'en' }" :aria-pressed="$i18n.locale === 'en'">EN</button>
          </div>

          <button class="control-btn menu-toggle" @click="menuOpen = !menuOpen" :aria-expanded="menuOpen" :aria-label="$t('nav.menu')">
            <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true">
              <path v-if="!menuOpen" d="M4 7h16M4 12h16M4 17h16" />
              <path v-else d="M6 6l12 12M18 6L6 18" />
            </svg>
          </button>
        </div>
      </header>

      <div id="top"></div>
      <HeroSection :theme="theme" />
      <ExperienceSection :theme="theme" />
      <ProjectsSection :theme="theme" />
      <SkillsSection :theme="theme" />
      <ContactSection :theme="theme" />

      <footer class="footer">&copy; 2026 Leslie Carolyn · DevStack • {{ $t('role') }}</footer>
    </div>
  </main>
</template>

<style scoped>
/* ESTRUCTURA BASE */
.main-container {
  min-height: 100vh;
  width: 100%;
  transition: background 0.8s ease;
  position: relative;
  overflow-x: hidden;
}
.canvas-background { position: fixed; top: 0; left: 0; width: 100%; height: 100vh; z-index: 1; }
.content-layer { position: relative; z-index: 2; width: 100%; }

/* NAVEGACIÓN: transparente arriba del todo, con fondo difuminado al hacer scroll */
.nav-container {
  position: fixed;
  top: 0;
  width: 100%;
  padding: 1.25rem 5%;
  display: flex;
  align-items: center;
  gap: 2rem;
  z-index: 100;
  border-bottom: 1px solid transparent;
  transition: background-color 0.3s ease, padding 0.3s ease, border-color 0.3s ease;
}
.nav-container.scrolled {
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
  background: var(--nav-bg);
  border-bottom-color: var(--control-border);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
}

.brand {
  font-weight: 700;
  font-size: 1.15rem;
  color: var(--text-color);
  text-decoration: none;
  white-space: nowrap;
}
.brand span { color: var(--accent-color); }

.nav-links {
  display: flex;
  align-items: center;
  gap: 1.75rem;
  margin-left: auto;
}
.nav-links a {
  color: var(--text-color);
  text-decoration: none;
  font-weight: 700;
  font-size: 0.95rem;
  opacity: 0.8;
  transition: opacity 0.2s ease, color 0.2s ease;
}
.nav-links a:hover { opacity: 1; color: var(--accent-color); }
.nav-links .nav-cv {
  opacity: 1;
  padding: 0.5rem 1.1rem;
  border-radius: 999px;
  background: var(--accent-color);
  color: #fff;
}
.nav-links .nav-cv:hover { color: #fff; filter: brightness(1.1); }

.nav-controls { display: flex; align-items: center; gap: 0.75rem; }

.control-btn {
  width: 2.5rem;
  height: 2.5rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 999px;
  cursor: pointer;
  color: var(--text-color);
  background: var(--control-bg);
  border: 1px solid var(--control-border);
  transition: color 0.2s ease, border-color 0.2s ease;
}
.control-btn:hover { color: var(--accent-color); border-color: var(--accent-color); }

.lang-group {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  height: 2.5rem;
  padding: 0 1rem;
  border-radius: 999px;
  background: var(--control-bg);
  border: 1px solid var(--control-border);
  color: var(--text-color);
}
.nav-btn { background: none; border: none; color: inherit; font-weight: 800; cursor: pointer; opacity: 0.5; }
.nav-btn.active { opacity: 1; color: var(--accent-color); }
.divider { opacity: 0.4; }

.menu-toggle { display: none; }

/* MÓVIL: los enlaces pasan a un desplegable */
@media (max-width: 860px) {
  .nav-container { gap: 1rem; }
  .nav-controls { margin-left: auto; }
  .menu-toggle { display: inline-flex; }
  .nav-links {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    flex-direction: column;
    align-items: stretch;
    gap: 0;
    padding: 0.5rem 5% 1.25rem;
    background: var(--nav-solid);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-bottom: 1px solid var(--control-border);
  }
  .nav-links.open { display: flex; }
  .nav-links a { padding: 0.85rem 0; font-size: 1.05rem; }
  .nav-links .nav-cv { margin-top: 0.75rem; text-align: center; padding: 0.75rem; }
}

/* COLORES GLOBALES POR TEMA */
/* Solo el contenedor principal: las secciones también llevan la clase del tema
   y, con estilos scoped, heredarían este fondo opaco tapando las partículas */
.main-container.pro { background-color: #0b0d1a; color: white; }
.main-container.creative { background-color: #faf7f2; color: #2a2024; }

.footer { padding: 3rem 5%; text-align: center; opacity: 0.5; font-weight: 800; color: var(--text-color); }
</style>
