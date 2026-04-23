<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import LogicCore from './components/LogicCore.vue'

// Importación de Secciones Modularizadas
import HeroSection from './components/sections/HeroSection.vue'
import ProjectsSection from './components/sections/ProjectsSection.vue'
import SkillsSection from './components/sections/SkillsSection.vue'
import ContactSection from './components/sections/ContactSection.vue'

// Estado Global
const scrollProgress = ref(0)
const theme = ref('pro') 

const toggleTheme = () => {
  theme.value = theme.value === 'pro' ? 'creative' : 'pro'
}

const onScroll = () => {
  const h = document.documentElement
  scrollProgress.value = h.scrollTop / (h.scrollHeight - h.clientHeight)
}

onMounted(() => window.addEventListener('scroll', onScroll))
onUnmounted(() => window.removeEventListener('scroll', onScroll))
</script>

<template>
  <main :class="['main-container', theme]">
    
    <div class="canvas-background">
      <LogicCore :scrollProgress="scrollProgress" :theme="theme" />
    </div>

    <div class="content-layer">
      <nav class="nav-container">
        <div class="nav-left">
          <button @click="toggleTheme" class="theme-toggle">
            {{ theme === 'pro' ? '🎨 Modo Creativo' : '💼 Modo Profesional' }}
          </button>
        </div>

        <div class="nav-right">
          <div class="lang-group">
            <button @click="$i18n.locale = 'es'" class="nav-btn" :class="{ active: $i18n.locale === 'es' }">ES</button>
            <span class="divider">|</span>
            <button @click="$i18n.locale = 'en'" class="nav-btn" :class="{ active: $i18n.locale === 'en' }">EN</button>
          </div>
        </div>
      </nav>

      <HeroSection :theme="theme" />
      <ProjectsSection :theme="theme" />
      <SkillsSection :theme="theme" />
      <ContactSection :theme="theme" />

      <footer class="footer">&copy; 2026 Carolyn DevStack • {{ $t('role') }}</footer>
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

/* NAVEGACIÓN */
.nav-container { position: fixed; top: 0; width: 100%; padding: 2rem 5%; display: flex; justify-content: space-between; align-items: center; z-index: 100; }
.lang-group { 
  display: flex; 
  gap: 0.8rem; 
  background: rgba(255, 255, 255, 0.1); 
  padding: 0.6rem 1.2rem; 
  border-radius: 50px; 
  backdrop-filter: blur(10px); 
  border: 1px solid rgba(255, 255, 255, 0.1); 
}
.nav-btn { background: none; border: none; color: inherit; font-weight: 800; cursor: pointer; opacity: 0.5; }
.nav-btn.active { opacity: 1; color: var(--accent-color); }
.theme-toggle { 
  padding: 0.8rem 1.5rem; 
  border-radius: 50px; 
  font-weight: 800; 
  cursor: pointer; 
  border: 1px solid rgba(255, 255, 255, 0.2); 
  background: rgba(255, 255, 255, 0.1); 
  color: inherit; 
}

/* COLORES GLOBALES POR TEMA */
.pro { background-color: #0a0f1e; color: white; --accent-color: #4facfe; }
.creative { background-color: #fdfaf6; color: #2d2d2d; --accent-color: #ff4081; }

.footer { padding: 5rem; text-align: center; opacity: 0.4; font-weight: 800; }
</style>