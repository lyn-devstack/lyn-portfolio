import { createI18n } from 'vue-i18n'
import en from './locales/en.json'
import es from './locales/es.json'

const i18n = createI18n({
  legacy: false, // Usamos el modo moderno de Vue 3
  locale: 'es',  // Idioma por defecto
  fallbackLocale: 'en', // Si falta algo en español, búscalo en inglés
  messages: { en, es }
})

export default i18n