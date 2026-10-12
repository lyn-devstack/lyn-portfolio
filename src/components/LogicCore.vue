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

const ACCENTS = { pro: new THREE.Color(0x8b7cff), creative: new THREE.Color(0xe8505b) }
const MOBILE_BREAKPOINT = 900          // mismo corte que en el CSS de la portada y contacto
const SHAPE_DISTANCE = 9               // distancia de la cámara al plano del avatar y el sobre

const coreCanvas = ref(null)
let scene, camera, renderer, points, rafId
let N = 0, GRID = 0, SEPARATION = 0
let positions, colors, waveBase, delays, avatarUV, avatarRGB, envelopeUV
let avatarLoaded = false, introStart = 0
const mouse = new THREE.Vector2(0, 0)
const accent = new THREE.Color()
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
      ? { cx: 0, cy: halfH * 0.52, size: halfH * 0.78 }
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
  else if (!reduceMotion) avatar *= clamp01((performance.now() - introStart) / 1600)
  return { avatar, envelope }
}

function frame(time) {
  const t = time * 0.001
  const { avatar, envelope } = shapeWeights()
  const A = shapeLayout('avatar'), E = shapeLayout('envelope')
  const cam = camera.position
  const mx = mouse.x * view.halfW, my = mouse.y * view.halfH
  const waveT = reduceMotion ? 0 : t * 1.0

  for (let i = 0; i < N; i++) {
    const d = delays[i]
    // Transición escalonada: cada partícula empieza a moverse en un momento distinto
    const wa = reduceMotion ? avatar : smooth(clamp01(avatar * 1.6 - d * 0.6))
    const we = reduceMotion ? envelope : smooth(clamp01(envelope * 1.6 - d * 0.6))
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
      let vx = 0, vy = 0, vz = -SHAPE_DISTANCE
      if (wa > 0) {
        let ax = A.cx + avatarUV[i * 2] * A.size
        let ay = A.cy + avatarUV[i * 2 + 1] * A.size
        // El avatar se aparta del ratón y "respira" ligeramente
        const dx = ax - mx, dy = ay - my, dm = Math.hypot(dx, dy)
        if (dm < 1.1 && dm > 0.0001) {
          const push = (1.1 - dm) * 0.55
          ax += (dx / dm) * push
          ay += (dy / dm) * push
        }
        if (!reduceMotion) ay += Math.sin(t * 1.4 + i) * 0.012
        vx += ax * wa; vy += ay * wa
      }
      if (we > 0) {
        vx += (E.cx + envelopeUV[i * 2] * E.size) * we
        vy += (E.cy + envelopeUV[i * 2 + 1] * E.size + (reduceMotion ? 0 : Math.sin(t * 1.2 + i) * 0.01)) * we
      }
      const ws = wa + we
      vz *= ws
      // Coordenadas de cámara → mundo (la cámara está fija)
      x += cam.x * ws + right.x * vx + up.x * vy - forward.x * -vz
      y += cam.y * ws + right.y * vx + up.y * vy - forward.y * -vz
      z += cam.z * ws + right.z * vx + up.z * vy - forward.z * -vz
    }

    positions[i * 3] = x
    positions[i * 3 + 1] = y
    positions[i * 3 + 2] = z

    // Color: el avatar mezcla los colores de la ilustración con el acento del tema
    const k = wa * 0.6
    colors[i * 3] = accent.r + (avatarRGB[i * 3] - accent.r) * k
    colors[i * 3 + 1] = accent.g + (avatarRGB[i * 3 + 1] - accent.g) * k
    colors[i * 3 + 2] = accent.b + (avatarRGB[i * 3 + 2] - accent.b) * k
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

async function loadAvatar() {
  try {
    const res = await fetch(`${import.meta.env.BASE_URL}particles/avatar.bin`)
    const buf = await res.arrayBuffer()
    const count = new DataView(buf).getUint32(0, true)
    const xy = new Int16Array(buf, 4, count * 2)
    const rgb = new Uint8Array(buf, 4 + count * 4, count * 3)
    for (let i = 0; i < N; i++) {
      const j = i % count
      avatarUV[i * 2] = xy[j * 2] / 10000
      avatarUV[i * 2 + 1] = xy[j * 2 + 1] / 10000
      avatarRGB[i * 3] = rgb[j * 3] / 255
      avatarRGB[i * 3 + 1] = rgb[j * 3 + 1] / 255
      avatarRGB[i * 3 + 2] = rgb[j * 3 + 2] / 255
    }
    avatarLoaded = true
    introStart = performance.now()
    renderOnce()
  } catch {
    // Sin avatar la portada sigue mostrando la ola
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

  N = 9000
  buildWave(N)
  envelopeUV = buildEnvelope(N)
  avatarUV = new Float32Array(N * 2)
  avatarRGB = new Float32Array(N * 3)
  delays = new Float32Array(N).map(() => Math.random())
  positions = new Float32Array(N * 3)
  colors = new Float32Array(N * 3)
  accent.copy(ACCENTS[props.theme] || ACCENTS.pro)

  const geometry = new THREE.BufferGeometry()
  geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3))
  geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3))
  const material = new THREE.PointsMaterial({ size: 0.055, vertexColors: true, transparent: true, opacity: 0.8 })
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

watch(() => props.theme, (theme) => {
  accent.copy(ACCENTS[theme] || ACCENTS.pro)
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
