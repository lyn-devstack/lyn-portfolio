<script setup>
import { ref } from 'vue'

const props = defineProps({
  title: String,
  description: String,
  stack: Array,
  details: Object,
  image: String,
  architectureImg: String // Para el diagrama de la memoria
})

const isModalOpen = ref(false)
</script>

<template>
  <div class="bg-[#1c1c1e] border border-gray-800 p-6 rounded-[2rem] hover:border-blue-500/50 transition-all duration-500 group flex flex-col h-full">
    <div class="h-48 bg-black rounded-2xl mb-6 overflow-hidden border border-gray-800">
      <img v-if="image" :src="image" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
      <div v-else class="w-full h-full bg-gradient-to-br from-blue-900/20 to-black flex items-center justify-center text-gray-700 text-xs tracking-widest">
        PREVIEW
      </div>
    </div>
    
    <div class="flex flex-wrap gap-2 mb-4">
      <span v-for="tech in stack" :key="tech" class="px-3 py-1 bg-blue-500/10 text-blue-400 text-[10px] font-bold uppercase rounded-full border border-blue-500/20">
        {{ tech }}
      </span>
    </div>

    <h3 class="text-2xl font-medium text-white mb-2">{{ title }}</h3>
    <p class="text-gray-400 text-sm mb-8 leading-relaxed flex-grow">{{ description }}</p>
    
    <button @click="isModalOpen = true" class="w-full py-3 bg-white text-black text-sm font-bold rounded-xl hover:bg-blue-500 hover:text-white transition-all duration-300">
      {{ $t('labels.viewArchitecture') }}
    </button>

    <Teleport to="body">
      <div v-if="isModalOpen" class="fixed inset-0 z-[100] flex items-center justify-center p-4 md:p-10">
        <div class="absolute inset-0 bg-black/80 backdrop-blur-md" @click="isModalOpen = false"></div>
        
        <div class="relative bg-[#1c1c1e] w-full max-w-5xl max-h-full overflow-y-auto rounded-[2.5rem] border border-gray-800 shadow-2xl shadow-blue-500/10">
          <button @click="isModalOpen = false" class="absolute top-6 right-6 text-gray-400 hover:text-white text-2xl">&times;</button>
          
          <div class="p-8 md:p-12 grid grid-cols-1 lg:grid-cols-2 gap-12">
            <div>
              <h4 class="text-blue-500 text-xs font-bold tracking-[0.2em] uppercase mb-4">Technical Blueprint</h4>
              <div class="bg-black rounded-3xl border border-gray-800 overflow-hidden mb-6">
                 <img :src="architectureImg" class="w-full h-auto opacity-80 hover:opacity-100 transition-opacity" alt="Architecture Diagram" />
              </div>
              <p class="text-gray-500 text-[11px] italic text-center">{{ $t('labels.technicalSource') }}</p>
            </div>

            <div class="flex flex-col justify-center">
              <h2 class="text-4xl font-light text-white mb-6 italic">{{ title }} <span class="text-blue-500 not-italic font-medium">Inside</span></h2>
              
              <div class="space-y-6">
                <div v-for="(info, label) in details" :key="label">
                  <h5 class="text-white text-sm font-bold mb-1 uppercase tracking-wider">{{ label }}</h5>
                  <p class="text-gray-400 text-sm leading-relaxed">{{ info }}</p>
                </div>
              </div>

              <div class="mt-10 p-6 bg-blue-500/5 rounded-2xl border border-blue-500/10">
                <p class="text-blue-400 text-xs leading-relaxed">
                    <strong>{{ $t('labels.authorNote') }}</strong> 
                    {{ title === 'Infinite' ? $t('labels.noteInfinite') : $t('labels.noteBooky') }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Teleport>
  </div>
</template>