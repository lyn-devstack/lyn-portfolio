<script setup>
import { ref, computed, watch, onUnmounted } from 'vue'
import { useI18n } from 'vue-i18n'

const props = defineProps({
  project: { type: Object, required: true },
  theme: { type: String, default: 'pro' }
})

const { t, te } = useI18n()
const isModalOpen = ref(false)
const isVideoOpen = ref(false)

const textKey = (key) => `projects.${props.project.id}.${key}`
const details = computed(() =>
  props.project.details.map(([label, text]) => ({ label: t(`labels.${label}`), text: t(textKey(text)) }))
)
const note = computed(() => (te(textKey('note')) ? t(textKey('note')) : null))
const modalTitleId = computed(() => `modal-title-${props.project.id}`)

const onKeydown = (e) => {
  if (e.key === 'Escape') isModalOpen.value = isVideoOpen.value = false
}

// Bloquea el scroll de fondo y permite cerrar con Escape mientras un modal está abierto
watch(() => isModalOpen.value || isVideoOpen.value, (open) => {
  document.body.style.overflow = open ? 'hidden' : ''
  if (open) window.addEventListener('keydown', onKeydown)
  else window.removeEventListener('keydown', onKeydown)
})

onUnmounted(() => {
  window.removeEventListener('keydown', onKeydown)
  document.body.style.overflow = ''
})
</script>

<template>
  <article :class="['project-card', theme, 'p-6 rounded-[2rem] group flex flex-col h-full']">
    <div class="card-media h-48 rounded-2xl mb-6 overflow-hidden">
      <img
        v-if="project.image"
        :src="project.image"
        :alt="t('labels.previewAlt', { title: project.title })"
        loading="lazy"
        class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-700"
      />
      <div v-else class="w-full h-full flex items-center justify-center text-xs tracking-widest">PREVIEW</div>
    </div>

    <ul class="flex flex-wrap gap-2 mb-4">
      <li v-for="tech in project.stack" :key="tech" class="tech-chip px-3 py-1 text-[10px] font-bold uppercase rounded-full">
        {{ tech }}
      </li>
    </ul>

    <h3 class="card-title text-2xl font-medium mb-2">{{ project.title }}</h3>
    <p class="card-text text-sm mb-8 leading-relaxed flex-grow">{{ t(textKey('description')) }}</p>

    <div class="flex flex-wrap gap-3">
      <button @click="isModalOpen = true" class="btn-primary flex-1 py-3 px-4 text-sm font-bold rounded-xl">
        {{ project.architectureImg ? t('labels.viewArchitecture') : t('labels.viewDetails') }}
      </button>
      <a v-if="project.repo" :href="project.repo" target="_blank" rel="noopener noreferrer"
         class="btn-secondary py-3 px-4 text-sm font-bold rounded-xl">
        {{ t('labels.code') }}
      </a>
      <a v-if="project.demo" :href="project.demo" target="_blank" rel="noopener noreferrer"
         class="btn-secondary py-3 px-4 text-sm font-bold rounded-xl">
        {{ t('labels.demo') }}
      </a>
      <button v-if="project.video" @click="isVideoOpen = true" class="btn-secondary py-3 px-4 text-sm font-bold rounded-xl">
        {{ t('labels.video') }}
      </button>
    </div>

    <Teleport to="body">
      <div v-if="isVideoOpen" :class="['project-modal', theme, 'fixed inset-0 z-[100] flex items-center justify-center p-4 md:p-10']">
        <div class="modal-backdrop absolute inset-0 backdrop-blur-md" @click="isVideoOpen = false"></div>
        <div role="dialog" aria-modal="true" :aria-label="t('labels.videoOf', { title: project.title })"
             class="modal-panel relative w-full max-w-5xl rounded-[1.5rem] p-3 md:p-4">
          <button @click="isVideoOpen = false" :aria-label="t('labels.close')"
                  class="modal-close absolute -top-10 right-2 text-3xl">&times;</button>
          <video :src="project.video" :poster="project.image" controls autoplay muted playsinline
                 class="w-full h-auto rounded-xl block"></video>
        </div>
      </div>
    </Teleport>

    <Teleport to="body">
      <div v-if="isModalOpen" :class="['project-modal', theme, 'fixed inset-0 z-[100] flex items-center justify-center p-4 md:p-10']">
        <div class="modal-backdrop absolute inset-0 backdrop-blur-md" @click="isModalOpen = false"></div>

        <div role="dialog" aria-modal="true" :aria-labelledby="modalTitleId"
             class="modal-panel relative w-full max-w-5xl max-h-full overflow-y-auto rounded-[2.5rem]">
          <button @click="isModalOpen = false" :aria-label="t('labels.close')" class="modal-close absolute top-6 right-6 text-2xl">&times;</button>

          <div :class="['p-8 md:p-12 grid grid-cols-1 gap-12', project.architectureImg ? 'lg:grid-cols-2' : 'max-w-2xl mx-auto']">
            <div v-if="project.architectureImg">
              <h4 class="accent-text text-xs font-bold tracking-[0.2em] uppercase mb-4">{{ t('labels.blueprint') }}</h4>
              <div class="card-media rounded-3xl overflow-hidden mb-6">
                <img :src="project.architectureImg" class="w-full h-auto" :alt="t('labels.diagramAlt', { title: project.title })" />
              </div>
              <p class="card-text text-[11px] italic text-center">{{ t('labels.technicalSource') }}</p>
            </div>

            <div class="flex flex-col justify-center">
              <h2 :id="modalTitleId" class="card-title text-4xl font-light mb-6 italic">
                {{ project.title }} <span class="accent-text not-italic font-medium">{{ t('labels.inside') }}</span>
              </h2>

              <dl class="space-y-6">
                <div v-for="item in details" :key="item.label">
                  <dt class="card-title text-sm font-bold mb-1 uppercase tracking-wider">{{ item.label }}</dt>
                  <dd class="card-text text-sm leading-relaxed">{{ item.text }}</dd>
                </div>
              </dl>

              <div v-if="note" class="note-box mt-10 p-6 rounded-2xl">
                <p class="accent-text text-xs leading-relaxed">
                  <strong>{{ t('labels.authorNote') }}</strong>
                  {{ note }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Teleport>
  </article>
</template>

<style scoped>
/* Los colores salen de las variables de tema definidas en style.css (.pro / .creative) */
.project-card {
  background: var(--surface);
  border: 1px solid var(--surface-border);
  box-shadow: var(--card-shadow);
  transition: border-color 0.5s ease, background-color 0.5s ease, box-shadow 0.5s ease;
}
.project-card:hover { border-color: var(--accent-soft-border); box-shadow: var(--card-shadow-hover); }

.card-media { background: var(--media-bg); border: 1px solid var(--surface-border); color: var(--text-muted); }
.card-title { color: var(--card-title); }
.card-text { color: var(--text-muted); }
.accent-text { color: var(--accent-color); }

.tech-chip {
  background: var(--accent-soft);
  color: var(--accent-color);
  border: 1px solid var(--accent-soft-border);
}

.btn-primary, .btn-secondary {
  text-align: center;
  cursor: pointer;
  transition: background-color 0.3s ease, color 0.3s ease, transform 0.3s ease;
}
.btn-primary { background: var(--btn-bg); color: var(--btn-text); }
.btn-primary:hover { background: var(--accent-color); color: #fff; }
.btn-secondary { background: transparent; color: var(--card-title); border: 1px solid var(--surface-border); }
.btn-secondary:hover { border-color: var(--accent-color); color: var(--accent-color); }

.modal-backdrop { background: var(--backdrop); }
.modal-panel { background: var(--surface); border: 1px solid var(--surface-border); box-shadow: var(--card-shadow-hover); }
.modal-close { color: var(--text-muted); }
.modal-close:hover { color: var(--card-title); }
.note-box { background: var(--accent-soft); border: 1px solid var(--accent-soft-border); }
</style>
