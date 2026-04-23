<script setup>
import { ref } from 'vue'

defineProps({
  theme: String
})

const email = "tu.email@ejemplo.com"
const copied = ref(false)

const copyToClipboard = () => {
  navigator.clipboard.writeText(email)
  copied.value = true
  setTimeout(() => copied.value = false, 2000)
}
</script>

<template>
  <section class="contact-section">
    <h2 class="section-title">{{ $t('contact.title') }}</h2>
    <div class="contact-links">
      <a href="#" target="_blank" class="contact-btn-secondary">LinkedIn</a>
      
      <button @click="copyToClipboard" class="contact-btn-primary">
        {{ copied ? $t('contact.copied') : $t('contact.copyEmail') }}
      </button>
      
      <a href="#" target="_blank" class="contact-btn-secondary">GitHub</a>
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
  margin-bottom: 4rem;
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
:deep(.pro) .contact-btn-primary {
  background: rgba(79, 172, 254, 0.15);
  color: #4facfe;
  border: 1px solid rgba(79, 172, 254, 0.3);
}

:deep(.pro) .contact-btn-secondary {
  background: rgba(255, 255, 255, 0.05);
  color: white;
}

:deep(.pro) .contact-btn-primary:hover, 
:deep(.pro) .contact-btn-secondary:hover {
  background: rgba(79, 172, 254, 0.3);
  transform: translateY(-5px);
  box-shadow: 0 12px 40px rgba(79, 172, 254, 0.3);
}

/* --- ADAPTACIÓN POR TEMAS (CREATIVE) --- */
:deep(.creative) .contact-btn-primary {
  background: rgba(255, 64, 129, 0.1);
  color: #ff4081;
  border: 1px solid rgba(255, 64, 129, 0.2);
}

:deep(.creative) .contact-btn-secondary {
  background: rgba(255, 255, 255, 0.4);
  color: #2d2d2d;
  border: 1px solid rgba(0, 0, 0, 0.05);
}

:deep(.creative) .contact-btn-primary:hover, 
:deep(.creative) .contact-btn-secondary:hover {
  background: rgba(255, 64, 129, 0.2);
  transform: translateY(-5px);
  box-shadow: 0 12px 40px rgba(255, 64, 129, 0.2);
}
</style>