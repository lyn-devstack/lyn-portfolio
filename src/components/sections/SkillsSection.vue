<script setup>
defineProps({
  theme: String
})
</script>

<template>
  <section class="max-w-6xl w-full mx-auto mb-32 px-4 relative z-10">
    <h2 class="text-3xl font-extralight italic mb-16 text-center tracking-widest transition-colors duration-500"
        :class="theme === 'pro' ? 'text-white/80' : 'text-gray-800'">
      {{ $t('skills.title') }}
    </h2>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
      
      <div class="group p-8 rounded-[2.5rem] transition-all duration-500 shadow-xl border"
           :class="theme === 'pro' 
              ? 'bg-gradient-to-b from-[#1c1c1e] to-black border-blue-500/30 hover:border-blue-500' 
              : 'bg-white border-blue-200 hover:border-blue-400 text-gray-800'">
        <div class="w-12 h-12 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform"
             :class="theme === 'pro' ? 'bg-blue-500/10' : 'bg-blue-50'">
          <span class="text-blue-500 font-bold text-xl">#</span>
        </div>
        <h3 class="text-sm font-bold tracking-widest uppercase mb-6"
            :class="theme === 'pro' ? 'text-white' : 'text-gray-700'">{{ $t('skills.mainStack') }}</h3>
        <div class="flex flex-wrap gap-3">
          <span class="px-3 py-1 rounded-lg text-xs font-bold border"
                :class="theme === 'pro' ? 'bg-blue-500/20 text-blue-400 border-blue-500/30' : 'bg-blue-50 text-blue-600 border-blue-100'">C#</span>
          <span class="px-3 py-1 rounded-lg text-xs font-bold border"
                :class="theme === 'pro' ? 'bg-blue-500/20 text-blue-400 border-blue-500/30' : 'bg-blue-50 text-blue-600 border-blue-100'">ASP.NET Core</span>
          <span class="px-3 py-1 rounded-lg text-xs border"
                :class="theme === 'pro' ? 'bg-white/5 text-gray-400 border-white/10' : 'bg-gray-50 text-gray-500 border-gray-100'">Entity Framework</span>
          <span class="px-3 py-1 rounded-lg text-xs border"
                :class="theme === 'pro' ? 'bg-white/5 text-gray-400 border-white/10' : 'bg-gray-50 text-gray-500 border-gray-100'">LINQ</span>
        </div>
      </div>

      <div class="group p-8 rounded-[2.5rem] transition-all duration-500 shadow-xl border"
           :class="theme === 'pro' 
              ? 'bg-[#1c1c1e] border-white/5 hover:border-green-500/50' 
              : 'bg-white border-green-100 hover:border-green-400 text-gray-800'">
        <div class="w-12 h-12 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform"
             :class="theme === 'pro' ? 'bg-green-500/10' : 'bg-green-50'">
          <span class="text-green-500 font-bold text-xl">M</span>
        </div>
        <h3 class="text-sm font-bold tracking-widest uppercase mb-6"
            :class="theme === 'pro' ? 'text-white' : 'text-gray-700'">{{ $t('skills.mobile') }}</h3>
        <div class="flex flex-wrap gap-3">
          <span v-for="s in ['Kotlin', 'Android SDK', 'Firebase', 'Material']" :key="s" 
                class="px-3 py-1 rounded-lg text-xs border"
                :class="theme === 'pro' ? 'bg-white/5 text-gray-400 border-white/10' : 'bg-gray-50 text-gray-500 border-gray-100'">{{s}}</span>
        </div>
      </div>

      <div class="group p-8 rounded-[2.5rem] transition-all duration-500 shadow-xl border"
           :class="theme === 'pro' 
              ? 'bg-[#1c1c1e] border-white/5 hover:border-purple-500/50' 
              : 'bg-white border-purple-100 hover:border-purple-400 text-gray-800'">
        <div class="w-12 h-12 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform"
             :class="theme === 'pro' ? 'bg-purple-500/10' : 'bg-purple-50'">
          <span class="text-purple-500 font-bold text-xl">DB</span>
        </div>
        <h3 class="text-sm font-bold tracking-widest uppercase mb-6"
            :class="theme === 'pro' ? 'text-white' : 'text-gray-700'">{{ $t('skills.database') }}</h3>
        <div class="flex flex-wrap gap-3">
          <span v-for="s in ['MySQL', 'Realtime DB', 'Cloud Storage', 'SQLite']" :key="s" 
                class="px-3 py-1 rounded-lg text-xs border"
                :class="theme === 'pro' ? 'bg-white/5 text-gray-400 border-white/10' : 'bg-gray-50 text-gray-500 border-gray-100'">{{s}}</span>
        </div>
      </div>

      <div class="group p-8 rounded-[2.5rem] transition-all duration-500 shadow-xl border"
           :class="theme === 'pro' 
              ? 'bg-[#1c1c1e] border-white/5 hover:border-orange-500/50' 
              : 'bg-white border-orange-100 hover:border-orange-400 text-gray-800'">
        <div class="w-12 h-12 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform"
             :class="theme === 'pro' ? 'bg-orange-500/10' : 'bg-orange-50'">
          <span class="text-orange-500 font-bold text-xl">...</span>
        </div>
        <h3 class="text-sm font-bold tracking-widest uppercase mb-6"
            :class="theme === 'pro' ? 'text-white' : 'text-gray-700'">{{ $t('skills.learning') }}</h3>
        <div class="flex flex-wrap gap-3">
          <span class="px-3 py-1 rounded-lg text-xs border italic"
                :class="theme === 'pro' ? 'bg-white/5 text-gray-400 border-white/10' : 'bg-orange-50 text-orange-600 border-orange-100'">Java / Spring</span>
          <span v-for="s in ['Git', 'Postman', 'Figma']" :key="s" 
                class="px-3 py-1 rounded-lg text-xs border"
                :class="theme === 'pro' ? 'bg-white/5 text-gray-400 border-white/10' : 'bg-gray-50 text-gray-500 border-gray-100'">{{s}}</span>
        </div>
      </div>

    </div>
  </section>
</template>