import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  base: '/lyn-portfolio/', // <--- Asegúrate de que este sea el nombre exacto de tu repo en GitHub
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
})