import { createI18n } from 'vue-i18n'
import en from './locales/en.json'
import es from './locales/es.json'

const i18n = createI18n({
  legacy: false, // Usamos el modo moderno de Vue 3
  locale: 'es',  // Idioma por defecto
  fallbackLocale: 'en', // Si falta algo en español, búscalo en inglés
  messages: { en, es }
})

const messages = {
  es: {
    projects: {
      infinite: {
        description: "Gestión integral para centros de estética. Control de citas, stock y usuarios con arquitectura robusta.",
        challenge: "Digitalizar una agenda física eliminando conflictos de citas.",
        architecture: "Implementación de Modelo-Vista-Controlador para separar la lógica de negocio de la interfaz.",
        security: "Rutas protegidas mediante .htaccess y encriptación de datos sensibles.",
        database: "Esquema relacional normalizado con disparadores para control de inventario."
      },
      bookyBloom: {
        description: "Biblioteca digital interactiva. Gestión de catálogo PDF y comunidad de lectores en tiempo real.",
        functionality: "Sistema de subida y lectura de PDFs con soporte para visualización offline.",
        stackInfo: "Uso de Firebase Realtime Database para interacciones y Storage para archivos binarios.",
        uxui: "Interfaz adaptativa con Modo Oscuro nativo y navegación fluida.",
        roles: "Módulo administrativo para gestión de contenido y módulo cliente para lectura y reseñas."
      }
    },
    labels: {
      challenge: "El Reto",
      architecture: "Arquitectura",
      security: "Seguridad",
      database: "Base de Datos",
      functionality: "Funcionalidad",
      stack: "Stack Técnico",
      uxui: "UX/UI",
      roles: "Roles"
    }
  },
  en: {
    projects: {
      infinite: {
        description: "Comprehensive management for beauty centers. Appointment control, stock, and users with a robust architecture.",
        challenge: "Digitalizing a physical agenda, eliminating appointment conflicts.",
        architecture: "Implementation of Model-View-Controller to separate business logic from the interface.",
        security: "Protected routes via .htaccess and sensitive data encryption.",
        database: "Normalized relational schema with triggers for inventory control."
      },
      // ... lo mismo para Booky Bloom en inglés
    },
    labels: {
      challenge: "The Challenge",
      architecture: "Architecture",
      security: "Security",
      database: "Database",
      // ... etc
    }
  }
}

export default i18n