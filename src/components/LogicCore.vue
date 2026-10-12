<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'
import * as THREE from 'three'

const props = defineProps({
  scrollProgress: { type: Number, default: 0 },
  theme: { type: String, default: 'pro' }
})

/*
  Una sola nube de partículas que cambia de forma según la sección visible:
    · Portada  → avatar (public/particles/avatar.bin, generado a partir de la ilustración)
    · Centro   → ola (malla animada, como el fondo original)
    · Contacto → sobre
  Cada partícula tiene un pequeño retraso aleatorio para que la transición sea orgánica.
*/

// Por tema: acento, fondo (para atenuar la ola detrás del texto) y colores del avatar a línea
const THEMES = {
  // Retrato punteado: cada tema tiene su propia nube (file). En oscuro los puntos marcan las luces;
  // en claro, las sombras (como un grabado). line: puntos más intensos · fill: los más tenues
  pro: { accent: 0x8b7cff, bg: 0x0b0d1a, line: 0xd6d0fa, fill: 0x3c3678, dark: 0x7868e6, file: 'portrait-dark.bin' },
  creative: { accent: 0xe8505b, bg: 0xfaf7f2, line: 0xbe3246, fill: 0xf0aaaf, dark: 0xbe3c4c, file: 'portrait-light.bin' }
}
const WAVE_STRENGTH = 0.4   // 1 = ola con el color de acento pleno; menos = más discreta tras el texto
const MOBILE_BREAKPOINT = 900          // mismo corte que en el CSS de la portada y contacto
const SHAPE_DISTANCE = 9               // distancia de la cámara al plano del avatar y el sobre

const coreCanvas = ref(null)
let scene, camera, renderer, points, rafId
let N = 0, GRID = 0, SEPARATION = 0
let positions, colors, waveBase, delays, envelopeUV
// Nube del retrato por tema, y mezcla actual entre ellas (0 = oscuro, 1 = claro) para recomponerlo al cambiar de tema
const portraits = {}
const themeMix = { value: 0, target: 0 }
let avatarLoaded = false
// Pesos actuales de cada forma: avanzan hacia el objetivo marcado por el scroll a velocidad constante
const blend = { avatar: 0, envelope: 0, last: 0 }
const MORPH_SECONDS = 1.6   // duración de una transición completa entre formas
const mouse = new THREE.Vector2(0, 0)
const smoothMouse = new THREE.Vector2(0, 0)   // sigue al ratón con retraso, para un movimiento suave
const accent = new THREE.Color(), waveColor = new THREE.Color(), lineColor = new THREE.Color(), fillColor = new THREE.Color(), darkColor = new THREE.Color()
const view = { halfH: 1, halfW: 1, mobile: false }
const right = new THREE.Vector3(), up = new THREE.Vector3(), forward = new THREE.Vector3()
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches

const clamp01 = (v) => Math.min(1, Math.max(0, v))
const smooth = (v) => v * v * (3 - 2 * v)

// Malla de la ola: cuadrícula centrada en el origen sobre el plano XZ
function buildWave(count) {
  GRID = Math.ceil(Math.sqrt(count))
  SEPARATION = 21 / GRID
  waveBase = new Float32Array(count * 2)
  for (let i = 0; i < count; i++) {
    waveBase[i * 2] = (i % GRID) * SEPARATION - (GRID * SEPARATION) / 2
    waveBase[i * 2 + 1] = Math.floor(i / GRID) * SEPARATION - (GRID * SEPARATION) / 2
  }
}

// Sobre: contorno, solapa y pliegues inferiores, más un relleno suave (coordenadas con alto = 1)
function buildEnvelope(count) {
  const W = 1.5, H = 1, pts = new Float32Array(count * 2)
  const segs = [
    [-W / 2, -H / 2, W / 2, -H / 2], [W / 2, -H / 2, W / 2, H / 2], [W / 2, H / 2, -W / 2, H / 2], [-W / 2, H / 2, -W / 2, -H / 2],
    [-W / 2, H / 2, 0, -0.05], [W / 2, H / 2, 0, -0.05],
    [-W / 2, -H / 2, -0.18, 0.08], [W / 2, -H / 2, 0.18, 0.08]
  ]
  const lens = segs.map(([x1, y1, x2, y2]) => Math.hypot(x2 - x1, y2 - y1))
  const total = lens.reduce((a, b) => a + b, 0)
  let seed = 11
  const rand = () => ((seed = (seed * 16807) % 2147483647) / 2147483647)
  const outline = Math.floor(count * 0.72)
  for (let i = 0; i < count; i++) {
    let x, y
    if (i < outline) {
      let d = rand() * total, s = 0
      while (d > lens[s]) d -= lens[s++]
      const [x1, y1, x2, y2] = segs[s], t = d / lens[s]
      x = x1 + (x2 - x1) * t + (rand() - 0.5) * 0.025
      y = y1 + (y2 - y1) * t + (rand() - 0.5) * 0.025
    } else {
      x = (rand() - 0.5) * W
      y = (rand() - 0.5) * H
    }
    pts[i * 2] = x
    pts[i * 2 + 1] = y
  }
  return pts
}

// Dónde va cada forma en pantalla (en coordenadas de la cámara)
function shapeLayout(kind) {
  const { halfH, halfW, mobile } = view
  if (kind === 'avatar') {
    return mobile
      ? { cx: 0, cy: halfH * 0.5, size: halfH * 0.8 }
      : { cx: halfW * 0.48, cy: -halfH * 0.04, size: halfH * 1.55 }
  }
  return mobile
    ? { cx: 0, cy: halfH * 0.5, size: halfH * 0.45 }
    : { cx: halfW * 0.5, cy: 0, size: halfH * 0.75 }
}

function updateView() {
  camera.aspect = window.innerWidth / window.innerHeight
  camera.updateProjectionMatrix()
  view.halfH = SHAPE_DISTANCE * Math.tan(THREE.MathUtils.degToRad(camera.fov / 2))
  view.halfW = view.halfH * camera.aspect
  view.mobile = window.innerWidth <= MOBILE_BREAKPOINT
  camera.matrixWorld.extractBasis(right, up, forward)  // forward = eje Z de la cámara (hacia atrás)
}

// Pesos de cada forma según el scroll: 1 = forma completa
function shapeWeights() {
  const y = window.scrollY, vh = window.innerHeight
  const hero = document.querySelector('.hero-full')
  const contact = document.getElementById('contact')
  const heroH = hero ? hero.offsetHeight : vh
  let avatar = 1 - clamp01(y / (heroH * 0.55))
  let envelope = 0
  if (contact && !view.mobile) {
    const top = contact.getBoundingClientRect().top
    envelope = clamp01((vh * 0.85 - top) / (vh * 0.5))
  }
  if (!avatarLoaded) avatar = 0
  return { avatar, envelope }
}

// Suaviza el cambio de pesos en el tiempo, para que un scroll brusco no haga saltar la forma
function smoothWeights(time) {
  const target = shapeWeights()
  if (reduceMotion) { blend.avatar = target.avatar; blend.envelope = target.envelope; themeMix.value = themeMix.target; return blend }
  const dt = blend.last ? Math.min(0.1, (time - blend.last) / 1000) : 0
  blend.last = time
  const step = dt / MORPH_SECONDS
  const toward = (cur, to) => cur + Math.sign(to - cur) * Math.min(Math.abs(to - cur), step)
  blend.avatar = toward(blend.avatar, target.avatar)
  blend.envelope = toward(blend.envelope, target.envelope)
  themeMix.value = toward(themeMix.value, themeMix.target)
  return blend
}

function frame(time) {
  const t = time * 0.001
  const { avatar, envelope } = smoothWeights(time)
  const A = shapeLayout('avatar'), E = shapeLayout('envelope')
  const cam = camera.position
  const waveT = reduceMotion ? 0 : t * 1.0
  const P0 = portraits.pro, P1 = portraits.creative
  if (!reduceMotion) smoothMouse.lerp(mouse, 0.05)
  const pmx = smoothMouse.x, pmy = smoothMouse.y

  for (let i = 0; i < N; i++) {
    const d = delays[i]
    // Transición escalonada: cada partícula empieza a moverse en un momento distinto
    // Cada partícula hace su viaje en el 60% del tiempo total, empezando con un retraso propio
    const wa = reduceMotion ? avatar : smooth(clamp01((avatar - d * 0.4) / 0.6))
    const we = reduceMotion ? envelope : smooth(clamp01((envelope - d * 0.4) / 0.6))
    const ww = Math.max(0, 1 - wa - we)

    // Ola
    const bx = waveBase[i * 2], bz = waveBase[i * 2 + 1]
    const gx = i % GRID, gz = Math.floor(i / GRID)
    let wy = Math.sin((gx * 0.63 + waveT * 3) * 0.3) * 0.4 + Math.sin((gz * 0.63 + waveT * 3) * 0.5) * 0.4
    const dist = Math.hypot(bx - mouse.x * 10, bz + mouse.y * 10)
    wy += Math.max(0, (4 - dist) * 0.8)

    let x = bx * ww, y = wy * ww, z = bz * ww

    // Formas en el plano frente a la cámara
    if (wa > 0 || we > 0) {
      let vx = 0, vy = 0, vz = 0
      if (wa > 0) {
        const tm = reduceMotion ? themeMix.value : smooth(clamp01((themeMix.value - d * 0.4) / 0.6))
        let ax = A.cx + (P0.uv[i * 2] + (P1.uv[i * 2] - P0.uv[i * 2]) * tm) * A.size
        let ay = A.cy + (P0.uv[i * 2 + 1] + (P1.uv[i * 2 + 1] - P0.uv[i * 2 + 1]) * tm) * A.size
        let az = -SHAPE_DISTANCE
        // Paralaje: todo el retrato sigue al ratón un poco, y cada punto con una profundidad
        // distinta, de modo que se mueve en bloque con sensación de volumen (sin abrir huecos)
        const depth = 0.92 + d * 0.16
        ax += pmx * 0.28 * depth
        ay += pmy * 0.2 * depth
        // Ligero giro hacia el ratón: el lado al que apunta se acerca a la cámara
        az += (ax - A.cx) * pmx * 0.12 + (ay - A.cy) * pmy * 0.08
        if (!reduceMotion) ay += Math.sin(t * 1.4 + i) * 0.012
        vx += ax * wa; vy += ay * wa; vz += az * wa
      }
      if (we > 0) {
        vz += -SHAPE_DISTANCE * we
        vx += (E.cx + envelopeUV[i * 2] * E.size) * we
        vy += (E.cy + envelopeUV[i * 2 + 1] * E.size + (reduceMotion ? 0 : Math.sin(t * 1.2 + i) * 0.01)) * we
      }
      const ws = wa + we
      // Coordenadas de cámara → mundo (la cámara está fija)
      x += cam.x * ws + right.x * vx + up.x * vy - forward.x * -vz
      y += cam.y * ws + right.y * vx + up.y * vy - forward.y * -vz
      z += cam.z * ws + right.z * vx + up.z * vy - forward.z * -vz
    }

    positions[i * 3] = x
    positions[i * 3 + 1] = y
    positions[i * 3 + 2] = z

    // Color: contornos del avatar marcados, relleno tenue; la ola, atenuada; el sobre, acento pleno
    const cur = themeMix.target > 0.5 ? P1 : P0
    const ink = cur.ink[i], dk = cur.dark[i]
    let ar = fillColor.r + (lineColor.r - fillColor.r) * ink
    let ag = fillColor.g + (lineColor.g - fillColor.g) * ink
    let ab = fillColor.b + (lineColor.b - fillColor.b) * ink
    ar += (darkColor.r - ar) * dk; ag += (darkColor.g - ag) * dk; ab += (darkColor.b - ab) * dk
    colors[i * 3] = waveColor.r * ww + ar * wa + accent.r * we
    colors[i * 3 + 1] = waveColor.g * ww + ag * wa + accent.g * we
    colors[i * 3 + 2] = waveColor.b * ww + ab * wa + accent.b * we
  }
  points.geometry.attributes.position.needsUpdate = true
  points.geometry.attributes.color.needsUpdate = true
  renderer.render(scene, camera)
}

const renderOnce = () => { if (renderer && !rafId) frame(performance.now()) }

const onWindowResize = () => {
  updateView()
  renderer.setSize(window.innerWidth, window.innerHeight)
  renderOnce()
}

const onMouseMove = (event) => {
  mouse.x = (event.clientX / window.innerWidth) * 2 - 1
  mouse.y = -(event.clientY / window.innerHeight) * 2 + 1
}

async function loadPortrait(theme) {
  const res = await fetch(`${import.meta.env.BASE_URL}particles/${THEMES[theme].file}`)
  const buf = await res.arrayBuffer()
  const count = new DataView(buf).getUint32(0, true)
  const xy = new Int16Array(buf, 4, count * 2)
  const ink = new Uint8Array(buf, 4 + count * 4, count)
  const dark = new Uint8Array(buf, 4 + count * 5, count)
  const P = portraits[theme]
  for (let i = 0; i < N; i++) {
    const j = i % count
    P.uv[i * 2] = xy[j * 2] / 10000
    P.uv[i * 2 + 1] = xy[j * 2 + 1] / 10000
    P.ink[i] = ink[j] / 255
    P.dark[i] = dark[j] / 255
  }
}

async function loadAvatar() {
  try {
    await Promise.all(Object.keys(THEMES).map(loadPortrait))
    avatarLoaded = true
    renderOnce()
  } catch {
    // Sin retrato la portada sigue mostrando la ola
  }
}

onMounted(() => {
  scene = new THREE.Scene()
  camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 1000)
  camera.position.set(0, 6, 12)
  camera.lookAt(0, 0, 0)
  camera.updateMatrixWorld()

  renderer = new THREE.WebGLRenderer({ canvas: coreCanvas.value, alpha: true, antialias: true })
  renderer.setSize(window.innerWidth, window.innerHeight)
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))

  N = 15000
  buildWave(N)
  envelopeUV = buildEnvelope(N)
  for (const theme of Object.keys(THEMES)) {
    portraits[theme] = { uv: new Float32Array(N * 2), ink: new Float32Array(N), dark: new Float32Array(N) }
  }
  themeMix.value = themeMix.target = props.theme === 'creative' ? 1 : 0
  delays = new Float32Array(N).map(() => Math.random())
  positions = new Float32Array(N * 3)
  colors = new Float32Array(N * 3)
  applyTheme(props.theme)

  const geometry = new THREE.BufferGeometry()
  geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3))
  geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3))
  const material = new THREE.PointsMaterial({ size: 0.05, vertexColors: true, transparent: true, opacity: 0.9 })
  points = new THREE.Points(geometry, material)
  scene.add(points)

  updateView()
  window.addEventListener('resize', onWindowResize)
  window.addEventListener('mousemove', onMouseMove)
  loadAvatar()

  if (reduceMotion) {
    // Sin animación continua: se redibuja solo al hacer scroll o cambiar el tamaño
    window.addEventListener('scroll', renderOnce, { passive: true })
    renderOnce()
  } else {
    const loop = (time) => { rafId = requestAnimationFrame(loop); frame(time) }
    rafId = requestAnimationFrame(loop)
  }
})

function applyTheme(theme) {
  const t = THEMES[theme] || THEMES.pro
  accent.set(t.accent)
  waveColor.set(t.bg).lerp(accent, WAVE_STRENGTH)
  lineColor.set(t.line)
  fillColor.set(t.fill)
  darkColor.set(t.dark)
}

watch(() => props.theme, (theme) => {
  applyTheme(theme)
  themeMix.target = theme === 'creative' ? 1 : 0
  renderOnce()
})

onUnmounted(() => {
  cancelAnimationFrame(rafId)
  window.removeEventListener('resize', onWindowResize)
  window.removeEventListener('mousemove', onMouseMove)
  window.removeEventListener('scroll', renderOnce)
  points?.geometry.dispose()
  points?.material.dispose()
  renderer?.dispose()
})
</script>

<template>
  <canvas ref="coreCanvas" class="core-canvas"></canvas>
</template>

<style scoped>
.core-canvas {
  width: 100vw !important;
  height: 100vh !important;
  display: block;
}
</style>
