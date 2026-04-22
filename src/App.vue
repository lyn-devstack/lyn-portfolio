<script setup>
import { ref } from 'vue'
import ProjectCard from './components/ProjectCard.vue'

// --- Lógica de Contacto ---
const email = "tu.email@ejemplo.com" // Pon aquí tu email real
const copied = ref(false)

const copyToClipboard = () => {
  navigator.clipboard.writeText(email)
  copied.value = true
  setTimeout(() => copied.value = false, 2000)
}
</script>

<template>
  <main class="min-h-screen w-full bg-black text-white px-6 py-20 flex flex-col items-center">
    
    <nav class="fixed top-10 right-10 flex gap-6 z-50">
      <button 
        @click="$i18n.locale = 'es'" 
        :class="{'text-blue-500 border-b border-blue-500': $i18n.locale === 'es'}"
        class="text-xs tracking-[0.2em] font-bold hover:text-blue-500 transition-colors uppercase pb-1"
      >
        ES
      </button>
      <button 
        @click="$i18n.locale = 'en'" 
        :class="{'text-blue-500 border-b border-blue-500': $i18n.locale === 'en'}"
        class="text-xs tracking-[0.2em] font-bold hover:text-blue-500 transition-colors uppercase pb-1"
      >
        EN
      </button>
    </nav>

    <section class="text-center mb-24 mt-10">
      <h1 class="text-6xl md:text-8xl font-extralight tracking-tighter italic mb-4">
        Lyn <span class="text-blue-500 not-italic font-medium">DevStack</span>
      </h1>
      <p class="text-gray-400 text-lg font-light max-w-lg mx-auto leading-relaxed">
        {{ $t('description') }}
      </p>
    </section>

    <section class="grid grid-cols-1 md:grid-cols-2 gap-12 max-w-6xl w-full mb-32">
      <ProjectCard 
        title="Infinite" 
        :description="$t('projects.infinite.description')"
        :stack="['PHP', 'MVC', 'MySQL', 'AJAX']"
        image="/images/infinite-preview.png"
        architectureImg="/images/infinite-db.png"
        :details="{
          [$t('labels.challenge')]: $t('projects.infinite.challenge'),
          [$t('labels.architecture')]: $t('projects.infinite.architecture'),
          [$t('labels.security')]: $t('projects.infinite.security'),
          [$t('labels.database')]: $t('projects.infinite.database')
        }"
      />

      <ProjectCard 
        title="Booky Bloom" 
        :description="$t('projects.bookyBloom.description')"
        :stack="['Kotlin', 'Firebase', 'Material Design']"
        image="/images/booky-preview.png" 
        architectureImg="/images/booky-diagram.png"
        :details="{
          [$t('labels.functionality')]: $t('projects.bookyBloom.functionality'),
          [$t('labels.stack')]: $t('projects.bookyBloom.stackInfo'),
          [$t('labels.uxui')]: $t('projects.bookyBloom.uxui'),
          [$t('labels.roles')]: $t('projects.bookyBloom.roles')
        }"
      />
    </section>

    <section class="max-w-6xl w-full mb-32 px-4">
      <h2 class="text-3xl font-extralight italic mb-16 text-center tracking-widest text-white/80">
        {{ $t('skills.title') }}
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        <div class="group bg-gradient-to-b from-[#1c1c1e] to-black border border-blue-500/30 p-8 rounded-[2.5rem] hover:border-blue-500 transition-all duration-500 shadow-xl">
          <div class="w-12 h-12 bg-blue-500/10 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
            <span class="text-blue-500 font-bold text-xl">#</span>
          </div>
          <h3 class="text-white text-sm font-bold tracking-widest uppercase mb-6">{{ $t('skills.mainStack') }}</h3>
          <div class="flex flex-wrap gap-3">
            <span class="px-3 py-1 bg-blue-500/20 rounded-lg text-xs text-blue-400 border border-blue-500/30 font-bold">C#</span>
            <span class="px-3 py-1 bg-blue-500/20 rounded-lg text-xs text-blue-400 border border-blue-500/30 font-bold">ASP.NET Core</span>
            <span class="px-3 py-1 bg-white/5 rounded-lg text-xs text-gray-400 border border-white/10">Entity Framework</span>
            <span class="px-3 py-1 bg-white/5 rounded-lg text-xs text-gray-400 border border-white/10">LINQ</span>
          </div>
        </div>

        <div class="group bg-[#1c1c1e] border border-white/5 p-8 rounded-[2.5rem] hover:border-green-500/50 transition-all duration-500 shadow-xl">
          <div class="w-12 h-12 bg-green-500/10 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
            <span class="text-green-500 font-bold text-xl">M</span>
          </div>
          <h3 class="text-white text-sm font-bold tracking-widest uppercase mb-6">{{ $t('skills.mobile') }}</h3>
          <div class="flex flex-wrap gap-3">
            <span v-for="s in ['Kotlin', 'Android SDK', 'Firebase', 'Material']" :key="s" class="px-3 py-1 bg-white/5 rounded-lg text-xs text-gray-400 border border-white/10">{{s}}</span>
          </div>
        </div>

        <div class="group bg-[#1c1c1e] border border-white/5 p-8 rounded-[2.5rem] hover:border-purple-500/50 transition-all duration-500 shadow-xl">
          <div class="w-12 h-12 bg-purple-500/10 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
            <span class="text-purple-500 font-bold text-xl">DB</span>
          </div>
          <h3 class="text-white text-sm font-bold tracking-widest uppercase mb-6">{{ $t('skills.database') }}</h3>
          <div class="flex flex-wrap gap-3">
            <span v-for="s in ['MySQL', 'Realtime DB', 'Cloud Storage', 'SQLite']" :key="s" class="px-3 py-1 bg-white/5 rounded-lg text-xs text-gray-400 border border-white/10">{{s}}</span>
          </div>
        </div>

        <div class="group bg-[#1c1c1e] border border-white/5 p-8 rounded-[2.5rem] hover:border-orange-500/50 transition-all duration-500 shadow-xl">
          <div class="w-12 h-12 bg-orange-500/10 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
            <span class="text-orange-500 font-bold text-xl">...</span>
          </div>
          <h3 class="text-white text-sm font-bold tracking-widest uppercase mb-6">{{ $t('skills.learning') }}</h3>
          <div class="flex flex-wrap gap-3">
            <span class="px-3 py-1 bg-white/5 rounded-lg text-xs text-gray-400 border border-white/10 italic">Java / Spring</span>
            <span v-for="s in ['Git', 'Postman', 'Figma']" :key="s" class="px-3 py-1 bg-white/5 rounded-lg text-xs text-gray-400 border border-white/10">{{s}}</span>
          </div>
        </div>
      </div>
    </section>

    <section class="max-w-4xl w-full text-center pb-32 px-4">
      <h2 class="text-4xl font-extralight italic mb-4 text-white">
        {{ $t('contact.title') }}
      </h2>
      <p class="text-gray-500 mb-12 font-light">
        {{ $t('contact.subtitle') }}
      </p>

      <div class="flex flex-col sm:flex-row items-center justify-center gap-6">
        <a href="TU_LINKEDIN_AQUI" target="_blank" class="w-full sm:w-auto flex items-center justify-center gap-3 px-8 py-4 bg-[#1c1c1e] border border-white/5 rounded-2xl hover:border-blue-500/50 transition-all">
          <span class="text-blue-500 font-bold">in</span>
          <span class="text-sm tracking-widest uppercase font-bold text-white">{{ $t('contact.linkedin') }}</span>
        </a>

        <button @click="copyToClipboard" class="w-full sm:w-auto flex items-center justify-center gap-3 px-8 py-4 bg-white text-black rounded-2xl hover:bg-blue-500 hover:text-white transition-all shadow-xl font-bold uppercase tracking-widest text-sm">
          {{ copied ? $t('contact.copied') : $t('contact.copyEmail') }}
        </button>

        <a href="TU_GITHUB_AQUI" target="_blank" class="w-full sm:w-auto flex items-center justify-center gap-3 px-8 py-4 bg-[#1c1c1e] border border-white/5 rounded-2xl hover:border-gray-500 transition-all">
          <span class="text-sm tracking-widest uppercase font-bold text-white">{{ $t('contact.github') }}</span>
        </a>
      </div>
    </section>

    <footer class="mt-auto pb-10 text-gray-600 text-[10px] tracking-[0.3em] uppercase">
      &copy; 2024 Lyn DevStack • {{ $t('role') }}
    </footer>

  </main>
</template>

<style scoped>
button { cursor: pointer; outline: none; }
</style>