<script setup>
defineProps({
  theme: String
})

// Los nombres de tecnologías no se traducen; los que sí, van como { t: 'clave' } bajo skills.items
const groups = [
  { key: 'frontend', icon: '</>', skills: ['Vue.js', 'TypeScript', 'JavaScript', 'Pinia', 'SCSS', 'Tailwind CSS'] },
  { key: 'backend', icon: '{ }', skills: ['PHP', 'C# / .NET Core', { t: 'microservices' }, { t: 'restApis' }, 'Swagger'] },
  { key: 'data', icon: 'DB', skills: ['MySQL', 'SQL Server', 'Firebase', 'IndexedDB'] },
  { key: 'tools', icon: '⚙', skills: ['Git / GitHub', 'Jira', 'Scrum / Kanban', 'Node.js / Gulp', 'Code Reviews'] }
]
const other = ['Kotlin / Android', 'WordPress', 'Three.js']
</script>

<template>
  <section id="skills" class="skills-section" :class="theme">
    <h2 class="section-title">{{ $t('skills.title') }}</h2>

    <div class="skills-grid">
      <div v-for="group in groups" :key="group.key" class="skill-card group">
        <div class="skill-icon group-hover:scale-110" aria-hidden="true">{{ group.icon }}</div>
        <h3 class="skill-title">{{ $t(`skills.${group.key}`) }}</h3>
        <ul class="chip-list">
          <li v-for="skill in group.skills" :key="skill.t || skill" class="chip">
            {{ skill.t ? $t(`skills.items.${skill.t}`) : skill }}
          </li>
        </ul>
      </div>
    </div>

    <p class="other-skills">
      <span class="other-label">{{ $t('skills.other') }}:</span>
      {{ other.join(' · ') }}
    </p>
  </section>
</template>

<style scoped>
.skills-section {
  padding: 3rem 5% 5rem;
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

.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(240px, 100%), 1fr));
  gap: 2rem;
}

.skill-card {
  padding: 2rem;
  border-radius: 2rem;
  background: var(--surface);
  border: 1px solid var(--surface-border);
  box-shadow: var(--card-shadow);
  transition: border-color 0.5s ease, box-shadow 0.5s ease;
}

.skill-card:hover {
  border-color: var(--accent-soft-border);
  box-shadow: var(--card-shadow-hover);
}

.skill-icon {
  width: 3rem;
  height: 3rem;
  border-radius: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
  font-weight: 800;
  background: var(--accent-soft);
  color: var(--accent-color);
  transition: transform 0.3s ease;
}

.skill-title {
  font-size: 0.85rem;
  font-weight: 800;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--card-title);
  margin-bottom: 1.5rem;
}

.chip-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
}

.chip {
  padding: 0.3rem 0.8rem;
  border-radius: 0.6rem;
  font-size: 0.75rem;
  font-weight: 700;
  background: var(--accent-soft);
  color: var(--accent-color);
  border: 1px solid var(--accent-soft-border);
}

.other-skills {
  margin-top: 2.5rem;
  text-align: center;
  font-size: 0.9rem;
  color: var(--text-muted);
}

.other-label { font-weight: 800; color: var(--text-color); }
</style>
