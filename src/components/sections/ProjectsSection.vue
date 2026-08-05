<script setup>
import ProjectCard from '../ProjectCard.vue'

// Definimos la prop theme por si en el futuro quieres 
// cambiar colores de los títulos según el modo
defineProps({
  theme: String
})
</script>

<template>
  <section class="projects-section">
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
        :theme="theme"
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
                 class="styled-card" :theme="theme" 
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
  transition: transform 0.4s ease; 
  cursor: pointer; 
  border-radius: 20px; 
  overflow: hidden; 
}

.styled-card:hover { 
  transform: translateY(-15px); 
}
</style>