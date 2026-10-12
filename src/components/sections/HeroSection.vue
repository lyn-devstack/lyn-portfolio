<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

defineProps({
  theme: String
})

const { locale } = useI18n()
// La base de Vite ('/lyn-portfolio/') se antepone para que el enlace funcione en GitHub Pages
const cvUrl = computed(() => `${import.meta.env.BASE_URL}cv/CV_Leslie_Carolyn_${locale.value.toUpperCase()}.pdf`)
</script>

<template>
  <section class="hero-full">
    <div class="hero-content">
      <p class="hero-eyebrow">{{ $t('hero.eyebrow') }}</p>
      <h1 class="hero-title" :class="theme === 'pro' ? 'text-white' : 'text-gray-900'">
        Leslie <span class="text-accent">Carolyn</span>
      </h1>
      <p class="hero-role">
        {{ $t('hero.role') }}
        <span class="hero-stack">{{ $t('hero.stack') }}</span>
      </p>
      <p class="hero-desc" :class="theme === 'pro' ? 'text-white/90' : 'text-gray-700'">
        {{ $t('hero.description') }}
      </p>
      <p class="hero-location">📍 {{ $t('hero.location') }}</p>

      <div class="hero-actions">
        <a href="#projects" class="hero-btn primary">{{ $t('hero.ctaProjects') }}</a>
        <a :href="cvUrl" target="_blank" rel="noopener" class="hero-btn secondary">{{ $t('hero.ctaCv') }}</a>
      </div>

      <div class="scroll-indicator" :class="theme === 'pro' ? 'text-white' : 'text-gray-400'">
        <span class="mouse" :class="theme === 'pro' ? 'border-white' : 'border-gray-400'"></span>
        <p class="scroll-text">{{ $t('sections.explore') }}</p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero-full {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 7rem 5%;
  position: relative;
  z-index: 10;
}

.hero-title { 
  font-size: clamp(3rem, 12vw, 8.5rem); 
  font-weight: 900; 
  line-height: 0.85; 
  margin: 0; 
}

.text-accent {
  color: var(--accent-color);
  transition: all 0.5s ease;
}

/* El color del acento lo manejamos con las clases globales .pro y .creative 
   que ya tienes en el main-container de App.vue */

.hero-eyebrow {
  font-size: 0.8rem;
  font-weight: 800;
  letter-spacing: 0.4em;
  text-transform: uppercase;
  color: var(--accent-color);
  margin-bottom: 1.5rem;
}

.hero-role {
  margin-top: 2rem;
  font-size: clamp(1.2rem, 2.5vw, 1.8rem);
  font-weight: 800;
  color: var(--text-color);
}

.hero-stack {
  display: block;
  margin-top: 0.4rem;
  font-size: 0.6em;
  font-weight: 600;
  letter-spacing: 0.15em;
  color: var(--accent-color);
}

.hero-desc {
  font-size: clamp(1rem, 1.6vw, 1.25rem);
  max-width: 650px;
  margin: 1.5rem auto 1rem;
  line-height: 1.6;
}

.hero-location {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-muted);
}

.hero-actions {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 1rem;
  margin-top: 2.5rem;
}

.hero-btn {
  padding: 0.9rem 2rem;
  border-radius: 14px;
  font-weight: 800;
  text-decoration: none;
  transition: transform 0.3s ease, background-color 0.3s ease, color 0.3s ease;
}
.hero-btn:hover { transform: translateY(-3px); }
.hero-btn.primary { background: var(--accent-color); color: #fff; }
.hero-btn.secondary {
  border: 1px solid var(--accent-soft-border);
  background: var(--accent-soft);
  color: var(--accent-color);
  backdrop-filter: blur(10px);
}

/* Scroll Indicator */
.scroll-indicator {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.mouse {
  width: 26px;
  height: 42px;
  border: 2px solid;
  border-radius: 20px;
  position: relative;
}

.mouse::before {
  content: '';
  position: absolute;
  top: 8px;
  left: 50%;
  width: 4px;
  height: 8px;
  background: currentColor;
  transform: translateX(-50%);
  border-radius: 2px;
  animation: scroll-wheel 2s infinite;
}

@keyframes scroll-wheel {
  0% { opacity: 1; transform: translateX(-50%) translateY(0); }
  100% { opacity: 0; transform: translateX(-50%) translateY(15px); }
}

/* En pantallas bajas o móviles taparía los botones */
@media (max-height: 820px), (max-width: 640px) {
  .scroll-indicator { display: none; }
}

.scroll-text {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.3em;
  font-weight: 800;
}
</style>