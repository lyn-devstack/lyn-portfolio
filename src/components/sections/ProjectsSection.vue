<script setup>
import ProjectCard from '../ProjectCard.vue'
import { projects } from '../../data/projects'

defineProps({
  theme: String // Recibe 'pro' o 'creative'
})
</script>

<template>
  <section id="projects" class="projects-section" :class="theme">
    <h2 class="section-title">{{ $t('sections.projects') }}</h2>
    <div class="projects-grid">
      <ProjectCard
        v-for="project in projects"
        :key="project.id"
        :project="project"
        :theme="theme"
        class="styled-card"
      />
    </div>
  </section>
</template>

<style scoped>
.projects-section {
  padding: 5rem 5%;
  max-width: 1300px;
  margin: 0 auto;
  position: relative;
  z-index: 10;
}

.section-title {
  font-size: clamp(2.5rem, 6vw, 4rem);
  font-weight: 700;
  text-align: center;
  margin-bottom: 4rem;
  color: var(--text-color);
}

.projects-grid {
  display: grid;
  /* min() evita que las tarjetas desborden en móviles de menos de 350px */
  grid-template-columns: repeat(auto-fit, minmax(min(350px, 100%), 1fr));
  gap: 3rem;
}

.styled-card {
  transition: transform 0.4s ease;
}

.styled-card:hover {
  transform: translateY(-15px);
}
</style>
