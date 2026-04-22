<script setup>
defineProps(['title', 'description', 'image', 'demoLink', 'githubLink'])
</script>

<template>
  <div class="bg-gray-900/50 border border-gray-800 p-6 rounded-3xl backdrop-blur-sm hover:border-blue-500/50 transition-all duration-500 group">
    <div class="h-48 bg-gray-800 rounded-2xl mb-6 overflow-hidden">
      <img v-if="image" :src="image" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
      <div v-else class="w-full h-full bg-gradient-to-br from-blue-900/20 to-black flex items-center justify-center text-gray-700 uppercase tracking-widest text-xs">
        No Image
      </div>
    </div>
    
    <h3 class="text-2xl font-light text-white mb-2">{{ title }}</h3>
    <p class="text-gray-400 text-sm mb-6 leading-relaxed h-12">{{ description }}</p>
    
    <div class="flex gap-4">
      <a :href="demoLink" target="_blank" class="flex-1 text-center py-2 bg-white text-black text-sm font-bold rounded-xl hover:bg-blue-500 hover:text-white transition-colors">
        Demo
      </a>
      <a :href="githubLink" target="_blank" class="flex-1 text-center py-2 border border-gray-700 text-white text-sm font-medium rounded-xl hover:bg-gray-800 transition-colors">
        GitHub
      </a>
    </div>
  </div>
</template>