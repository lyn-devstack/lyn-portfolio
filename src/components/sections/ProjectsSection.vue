<!-- ProjectsSection.vue -->
<script setup>
import ProjectCard from '../ProjectCard.vue'

defineProps({
  theme: String // Recibe 'pro' o 'creative'
})
</script>

<template>
  <section class="projects-section" :class="theme">
    <h2 class="section-title">{{ $i18n.locale === 'es' ? 'Proyectos' : 'Projects' }}</h2>
    <div class="projects-grid">
      <ProjectCard 
        title="Infinite" 
        :description="$t('projects.infinite.description')"
        :stack="['PHP', 'MVC', 'MySQL', 'AJAX']"
        image="./images/infinite-preview.png"
        architectureImg="./images/infinite-db.png"
        :details="{
          [$t('labels.challenge')]: $t('projects.infinite.challenge'),
          [$t('labels.architecture')]: $t('projects.infinite.architecture'),
          [$t('labels.security')]: $t('projects.infinite.security'),
          [$t('labels.database')]: $t('projects.infinite.database')
        }"
        class="styled-card" 
      />

      <ProjectCard 
        title="Booky Bloom" 
        :description="$t('projects.bookyBloom.description')"
        :stack="['Kotlin', 'Firebase', 'Material Design']"
        image="./images/booky-preview.png" 
        architectureImg="./images/booky-diagram.png"
        :details="{
          [$t('labels.functionality')]: $t('projects.bookyBloom.functionality'),
          [$t('labels.stack')]: $t('projects.bookyBloom.stackInfo'),
          [$t('labels.uxui')]: $t('projects.bookyBloom.uxui'),
          [$t('labels.roles')]: $t('projects.bookyBloom.roles')
        }"
        class="styled-card" 
      />
    </div>
  </section>
</template>

<style scoped>
.projects-section { 
  padding: 8rem 5%; 
  max-width: 1300px; 
  margin: 0 auto; 
  position: relative;
  z-index: 10;
  transition: background-color 0.4s ease, color 0.4s ease;
}

.section-title { 
  font-size: clamp(2.5rem, 6vw, 4rem); 
  font-weight: 900; 
  text-align: center; 
  margin-bottom: 4rem; 
}

.projects-grid { 
  display: grid; 
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); 
  gap: 3rem; 
}

.styled-card { 
  transition: transform 0.4s ease, background-color 0.4s ease, box-shadow 0.4s ease; 
  cursor: pointer; 
  border-radius: 20px; 
  overflow: hidden; 
}

.styled-card:hover { 
  transform: translateY(-15px); 
}

/* --- ESTILOS MODO PRO --- */
.projects-section.pro .section-title {
  color: white;
}

/* --- ESTILOS MODO CREATIVO / NEBULOSA --- */
.projects-section.creative .section-title {
  color: #2b1f2d;
}

/* TARJETA EN MODO CREATIVO (Rosa pastel / Nebulosa) */
.projects-section.creative :deep(.styled-card) {
  /* Fondo rosa pastel empolvado */
  background-color: #f8eef2; 
  /* Texto ciruela oscuro legible */
  color: #2d1d2b;
  /* Sombra sutil rosada */
  box-shadow: 0 10px 30px rgba(255, 64, 129, 0.12);
  border: 1px solid rgba(255, 64, 129, 0.2);
}

.projects-section.creative :deep(.styled-card:hover) {
  background-color: #fcf2f6;
  box-shadow: 0 15px 40px rgba(255, 64, 129, 0.25);
}

/* Títulos y textos dentro de la card */
.projects-section.creative :deep(.styled-card h3),
.projects-section.creative :deep(.styled-card .card-title) {
  color: #ff4081;
}

.projects-section.creative :deep(.styled-card p),
.projects-section.creative :deep(.styled-card .card-description) {
  color: #4a384c;
}
/* ==============================================
   --- ADAPTACIÓN DE ELEMENTOS INTERNOS (NEBULOSA / CREATIVE) ---
   ============================================== */

/* 1. BADGES / PILLS DE TECNOLOGÍAS (PHP, Kotlin, etc.) */
.projects-section.creative :deep(.styled-card .stack-tag),
.projects-section.creative :deep(.styled-card .tech-badge),
.projects-section.creative :deep(.styled-card span) {
  background: rgba(255, 64, 129, 0.12) !important;
  color: #d81b60 !important;
  border: 1px solid rgba(255, 64, 129, 0.25) !important;
}

/* 2. BOTONES PRINCIPALES (View Architecture) */
.projects-section.creative :deep(.styled-card button),
.projects-section.creative :deep(.styled-card .btn-architecture),
.projects-section.creative :deep(.styled-card a) {
  background: #ff4081 !important;
  color: #ffffff !important;
  border: none !important;
  box-shadow: 0 4px 15px rgba(255, 64, 129, 0.3) !important;
  transition: all 0.3s ease !important;
}

/* 3. HOVER DE LOS BOTONES */
.projects-section.creative :deep(.styled-card button:hover),
.projects-section.creative :deep(.styled-card .btn-architecture:hover),
.projects-section.creative :deep(.styled-card a:hover) {
  background: #e91e63 !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 8px 22px rgba(255, 64, 129, 0.45) !important;
}
</style>