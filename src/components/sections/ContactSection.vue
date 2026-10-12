<script setup>
defineProps({
  theme: String
})
</script>

<template>
  <section class="contact-section" :class="theme">
    <h2 class="section-title">{{ $t('contact.title') }}</h2>
    <p class="section-subtitle">{{ $t('contact.subtitle') }}</p>
    <div class="contact-links">
      <a href="https://www.linkedin.com/in/carolyn-lyn-dev" target="_blank" rel="noopener noreferrer" class="contact-btn-primary">
        {{ $t('contact.linkedin') }}
      </a>

      <a href="https://github.com/lyn-devstack" target="_blank" rel="noopener noreferrer" class="contact-btn-secondary">
        {{ $t('contact.github') }}
      </a>
    </div>
  </section>
</template>

<style scoped>
.contact-section {
  padding: 10rem 5%;
  text-align: center;
  position: relative;
  z-index: 10;
}

.section-title {
  font-size: clamp(2.5rem, 6vw, 4rem);
  font-weight: 900;
  margin-bottom: 1.5rem;
}

.section-subtitle {
  font-size: clamp(1rem, 2vw, 1.3rem);
  opacity: 0.8;
}

.contact-links {
  display: flex;
  justify-content: center;
  gap: 2rem;
  padding: 4rem 0;
  flex-wrap: wrap;
}

/* Estilo Base del Botón Espejo */
.contact-btn-primary, .contact-btn-secondary {
  padding: 1.2rem 2.5rem;
  border-radius: 16px;
  font-weight: 800;
  text-decoration: none;
  transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
  
  /* Efecto Cristal/Espejo */
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
  
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

/* --- ADAPTACIÓN POR TEMAS (PRO) --- */
.contact-section.pro .contact-btn-primary {
  background: rgba(79, 172, 254, 0.15);
  color: #4facfe;
  border: 1px solid rgba(79, 172, 254, 0.3);
}

.contact-section.pro .contact-btn-secondary {
  background: rgba(255, 255, 255, 0.05);
  color: white;
}

.contact-section.pro .contact-btn-primary:hover, 
.contact-section.pro .contact-btn-secondary:hover {
  background: rgba(79, 172, 254, 0.3);
  transform: translateY(-5px);
  box-shadow: 0 12px 40px rgba(79, 172, 254, 0.3);
}

/* --- ADAPTACIÓN POR TEMAS (CREATIVE) --- */
.contact-section.creative .contact-btn-primary {
  background: rgba(255, 64, 129, 0.1);
  color: #ff4081;
  border: 1px solid rgba(255, 64, 129, 0.2);
}

.contact-section.creative .contact-btn-secondary {
  background: rgba(255, 255, 255, 0.4);
  color: #2d2d2d;
  border: 1px solid rgba(0, 0, 0, 0.05);
}

.contact-section.creative .contact-btn-primary:hover, 
.contact-section.creative .contact-btn-secondary:hover {
  background: rgba(255, 64, 129, 0.2);
  transform: translateY(-5px);
  box-shadow: 0 12px 40px rgba(255, 64, 129, 0.2);
}
</style>