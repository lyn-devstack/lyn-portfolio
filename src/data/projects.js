// Datos de cada proyecto. Los textos viven en locales/*.json bajo projects.<id>
// details: pares [clave de labels, clave de projects.<id>] que se muestran en el modal
export const projects = [
  {
    id: 'infinite',
    title: 'Infinite',
    stack: ['PHP', 'MVC', 'MySQL', 'AJAX', 'Docker'],
    image: './images/infinite-preview.png',
    architectureImg: './images/infinite-db.png',
    details: [
      ['challenge', 'challenge'],
      ['architecture', 'architecture'],
      ['security', 'security'],
      ['database', 'database']
    ],
    repo: 'https://github.com/lyn-devstack/infinite-beauty-center',
    demo: null
  },
  {
    id: 'bookyBloom',
    title: 'Booky Bloom',
    stack: ['Kotlin', 'Firebase', 'Material Design'],
    image: './images/booky-preview.png',
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
    image: './images/matchatest-preview.png',
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
