<script setup>
import ProjectCard from './components/ProjectCard.vue'
</script>

<template>
  <main class="min-h-screen w-full bg-black text-white px-6 py-20 flex flex-col items-center">
    
    <nav class="fixed top-10 right-10 flex gap-6 z-50">
      <button @click="$i18n.locale = 'es'" class="text-xs tracking-widest hover:text-blue-500 transition-colors">ES</button>
      <button @click="$i18n.locale = 'en'" class="text-xs tracking-widest hover:text-blue-500 transition-colors">EN</button>
    </nav>

    <section class="text-center mb-20 mt-10">
      <h1 class="text-6xl md:text-8xl font-extralight tracking-tighter italic mb-4">
        Lyn <span class="text-blue-500 not-italic font-medium">DevStack</span>
      </h1>
      <p class="text-gray-400 text-lg font-light max-w-lg mx-auto">
        {{ $t('description') }}
      </p>
    </section>

    <section class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl w-full">
      <ProjectCard 
        title="Infinite" 
        description="Software de gestión para centros de estética. Arquitectura robusta y escalable."
        image="/images/infinite.png"
        demoLink="#" 
        githubLink="#"
      />
      <ProjectCard 
        title="Booky Bloom" 
        description="Gestión de inventario para florerías. Una solución elegante para negocios locales."
        image="/images/booky.png"
        demoLink="#" 
        githubLink="#"
      />
    </section>

  </main>
</template>