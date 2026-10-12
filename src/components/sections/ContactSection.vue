<script setup>
defineProps({
  theme: String
})
</script>

<template>
  <section id="contact" class="contact-section" :class="theme">
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
  padding: 5rem 5% 3rem;
  text-align: center;
  position: relative;
  z-index: 10;
}

.section-title {
  font-size: clamp(2.5rem, 6vw, 4rem);
  font-weight: 700;
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
  padding: 2.5rem 0 0;
  flex-wrap: wrap;
}

/* En móvil la ola pasa por detrás del texto: se le da un fondo translúcido */
@media (max-width: 900px) {
  .contact-section > * { position: relative; }
  .contact-section { background: var(--panel-bg); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); }
}

/* En escritorio el texto va a la izquierda y las partículas forman un sobre a la derecha */
@media (min-width: 901px) {
  .contact-section {
    min-height: 70vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: left;
    max-width: 1300px;
    margin: 0 auto;
  }
  .contact-section > * { max-width: 50%; }
  .contact-links { justify-content: flex-start; }
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

/* Colores desde las variables del tema (style.css) */
.contact-btn-primary {
  background: var(--accent-soft);
  color: var(--accent-color);
  border: 1px solid var(--accent-soft-border);
}

.contact-btn-secondary {
  background: var(--control-bg);
  color: var(--text-color);
  border: 1px solid var(--control-border);
}

.contact-btn-primary:hover,
.contact-btn-secondary:hover {
  background: rgba(var(--accent-rgb), 0.22);
  transform: translateY(-5px);
  box-shadow: 0 12px 40px rgba(var(--accent-rgb), 0.25);
}
</style>