<script setup>
defineProps({
  theme: String
})
</script>

<template>
  <section class="hero-full">
    <div class="hero-content">
      <h1 class="hero-title" :class="theme === 'pro' ? 'text-white' : 'text-gray-900'">
        Carolyn <span class="text-accent">DevStack</span>
      </h1>
      <p class="hero-desc" :class="theme === 'pro' ? 'text-white/90' : 'text-gray-700'">
        {{ $t('description') }}
      </p>
      
      <div class="scroll-indicator" :class="theme === 'pro' ? 'text-white' : 'text-gray-400'">
        <span class="mouse" :class="theme === 'pro' ? 'border-white' : 'border-gray-400'"></span>
        <p class="scroll-text">{{ $i18n.locale === 'es' ? 'Explorar' : 'Explore' }}</p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero-full {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 0 5%;
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
  transition: all 0.5s ease;
}

/* El color del acento lo manejamos con las clases globales .pro y .creative 
   que ya tienes en el main-container de App.vue */

.hero-desc { 
  font-size: clamp(1.1rem, 2vw, 1.6rem); 
  max-width: 650px; 
  margin: 2rem auto; 
  font-style: italic; 
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

.scroll-text {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.3em;
  font-weight: 800;
}
</style>