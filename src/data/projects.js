// Datos de cada proyecto. Los textos viven en locales/*.json bajo projects.<id>
// details: pares [clave de labels, clave de projects.<id>] que se muestran en el modal
export const projects = [
  {
    id: 'lumiere',
    title: 'Lumière Studio',
    stack: ['PHP', 'MVC', 'MySQL', 'AJAX', 'Docker'],
    image: './images/lumiere-preview.jpg',
    architectureImg: './images/lumiere-db.png',
    details: [
      ['challenge', 'challenge'],
      ['architecture', 'architecture'],
      ['security', 'security'],
      ['database', 'database']
    ],
    repo: 'https://github.com/lyn-devstack/lumiere-booking',
    demo: null,
    // Recorrido grabado (la app necesita PHP + MySQL, no se puede alojar en GitHub Pages)
    video: './videos/lumiere-demo.mp4'
  },
  {
    id: 'bookyBloom',
    title: 'Booky Bloom',
    stack: ['Kotlin', 'Firebase', 'Material Design'],
    image: './images/booky-cover.jpg',
    architectureImg: './images/booky-diagram.png',
    details: [
      ['functionality', 'functionality'],
      ['stack', 'stackInfo'],
      ['uxui', 'uxui'],
      ['roles', 'roles']
    ],
    repo: 'https://github.com/lyn-devstack/BookyBloom',
    demo: null
  },
  {
    id: 'matchaTest',
    title: 'matchaTest',
    stack: ['Vue 3', 'TypeScript', 'Tailwind', 'IndexedDB'],
    image: './images/matchatest-cover.jpg',
    architectureImg: null,
    details: [
      ['challenge', 'challenge'],
      ['functionality', 'functionality'],
      ['architecture', 'architecture'],
      ['uxui', 'uxui']
    ],
    repo: 'https://github.com/lyn-devstack/matchaTest',
    demo: 'https://lyn-devstack.github.io/matchaTest/'
  }
]
