<script setup>
import { useI18n } from 'vue-i18n'

defineProps({
  theme: String
})

// tm() devuelve los arrays de las traducciones; rt() resuelve cada texto
const { tm, rt } = useI18n()
</script>

<template>
  <section id="experience" class="experience-section" :class="theme">
    <h2 class="section-title">{{ $t('experience.title') }}</h2>

    <div class="experience-grid">
      <div class="readable-panel">
        <h3 class="column-title">{{ $t('experience.jobsTitle') }}</h3>
        <ol class="timeline">
          <li v-for="job in tm('experience.jobs')" :key="rt(job.company)" class="timeline-item">
            <span class="timeline-dot" aria-hidden="true"></span>
            <p class="item-period">{{ rt(job.period) }}</p>
            <h4 class="item-title">{{ rt(job.role) }} <span class="item-company">· {{ rt(job.company) }}</span></h4>
            <p class="item-summary">{{ rt(job.summary) }}</p>
            <ul class="item-bullets">
              <li v-for="bullet in job.bullets" :key="rt(bullet)">{{ rt(bullet) }}</li>
            </ul>
          </li>
        </ol>
      </div>

      <div class="readable-panel">
        <h3 class="column-title">{{ $t('experience.educationTitle') }}</h3>
        <ul class="education-list">
          <li v-for="item in tm('experience.education')" :key="rt(item.title)" class="education-card">
            <h4 class="item-title">{{ rt(item.title) }}</h4>
            <p class="item-period">{{ rt(item.detail) }}</p>
          </li>
        </ul>

        <h3 class="column-title mt-10">{{ $t('experience.languagesTitle') }}</h3>
        <p class="item-summary">{{ $t('experience.languages') }}</p>

        <h3 class="column-title mt-10">{{ $t('experience.certsTitle') }}</h3>
        <p class="item-summary">{{ $t('experience.certs') }}</p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.experience-section {
  padding: 6rem 5%;
  max-width: 1300px;
  margin: 0 auto;
  position: relative;
  z-index: 10;
  color: var(--text-color);
}

.section-title {
  font-size: clamp(2.5rem, 6vw, 4rem);
  font-weight: 700;
  text-align: center;
  margin-bottom: 4rem;
}

.experience-grid {
  display: grid;
  grid-template-columns: minmax(0, 3fr) minmax(0, 2fr);
  gap: 4rem;
}

@media (max-width: 900px) {
  .experience-grid { grid-template-columns: minmax(0, 1fr); }
}

.column-title {
  font-size: 0.75rem;
  font-weight: 800;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--accent-color);
  margin-bottom: 1.5rem;
}

/* LÍNEA DE TIEMPO */
.timeline {
  border-left: 2px solid var(--accent-soft-border);
  padding-left: 2rem;
  display: flex;
  flex-direction: column;
  gap: 2.5rem;
}

.timeline-item { position: relative; }

.timeline-dot {
  position: absolute;
  left: calc(-2rem - 7px);
  top: 0.3rem;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--accent-color);
  box-shadow: 0 0 0 4px var(--accent-soft);
}

.item-period {
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--text-muted);
  margin-bottom: 0.3rem;
}

.item-title {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--card-title);
}

.item-company { color: var(--accent-color); }

.item-summary {
  margin-top: 0.6rem;
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--text-muted);
}

.item-bullets {
  margin-top: 0.8rem;
  padding-left: 1.1rem;
  list-style: disc;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  font-size: 0.9rem;
  line-height: 1.55;
  color: var(--text-muted);
}

.item-bullets li::marker { color: var(--accent-color); }

/* FORMACIÓN */
.education-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.education-card {
  padding: 1.2rem 1.4rem;
  border-radius: 1.2rem;
  background: var(--surface);
  border: 1px solid var(--surface-border);
}

.education-card .item-title { font-size: 1rem; margin-bottom: 0.3rem; }
.education-card .item-period { margin-bottom: 0; }
</style>
