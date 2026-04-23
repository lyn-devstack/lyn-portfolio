<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'
import * as THREE from 'three'

const props = defineProps({
  scrollProgress: { type: Number, default: 0 },
  theme: { type: String, default: 'pro' }
})

const coreCanvas = ref(null)
let scene, camera, renderer, particles, positions
let mouse = new THREE.Vector2(0, 0)
const SEPARATION = 0.35, AMOUNTX = 60, AMOUNTY = 60

const onWindowResize = () => {
  camera.aspect = window.innerWidth / window.innerHeight
  camera.updateProjectionMatrix()
  renderer.setSize(window.innerWidth, window.innerHeight)
}

const onMouseMove = (event) => {
  mouse.x = (event.clientX / window.innerWidth) * 2 - 1
  mouse.y = -(event.clientY / window.innerHeight) * 2 + 1
}

onMounted(() => {
  scene = new THREE.Scene()
  camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 1000)
  camera.position.z = 12
  camera.position.y = 6
  camera.lookAt(0, 0, 0)

  renderer = new THREE.WebGLRenderer({ 
    canvas: coreCanvas.value, 
    alpha: true, 
    antialias: true 
  })
  renderer.setSize(window.innerWidth, window.innerHeight)
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))

  const numParticles = AMOUNTX * AMOUNTY
  positions = new Float32Array(numParticles * 3)
  const geometry = new THREE.BufferGeometry()

  let i = 0
  for (let ix = 0; ix < AMOUNTX; ix++) {
    for (let iy = 0; iy < AMOUNTY; iy++) {
      positions[i] = ix * SEPARATION - (AMOUNTX * SEPARATION) / 2
      positions[i + 1] = 0
      positions[i + 2] = iy * SEPARATION - (AMOUNTY * SEPARATION) / 2
      i += 3
    }
  }

  geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3))
  const material = new THREE.PointsMaterial({ 
    color: props.theme === 'pro' ? 0x4facfe : 0xff4081, 
    size: 0.06,
    transparent: true,
    opacity: 0.6
  })

  particles = new THREE.Points(geometry, material)
  scene.add(particles)

  window.addEventListener('resize', onWindowResize)
  window.addEventListener('mousemove', onMouseMove)

  let count = 0
  const animate = () => {
    requestAnimationFrame(animate)
    
    const posAttr = particles.geometry.attributes.position
    let i = 0
    for (let ix = 0; ix < AMOUNTX; ix++) {
      for (let iy = 0; iy < AMOUNTY; iy++) {
        // Efecto Olas (Sinoidal)
        const wave = (Math.sin((ix + count) * 0.3) * 0.4) + (Math.sin((iy + count) * 0.5) * 0.4)
        
        // Reacción al Mouse (Distancia)
        const posX = posAttr.array[i]
        const posZ = posAttr.array[i + 2]
        const dist = Math.sqrt(Math.pow(posX - mouse.x * 10, 2) + Math.pow(posZ - (-mouse.y * 10), 2))
        const mouseEffect = Math.max(0, (4 - dist) * 0.8)

        posAttr.array[i + 1] = wave + mouseEffect
        i += 3
      }
    }
    posAttr.needsUpdate = true
    count += 0.04
    
    renderer.render(scene, camera)
  }
  animate()
})

watch(() => props.theme, (newVal) => {
  if (particles) {
    particles.material.color.set(newVal === 'pro' ? 0x4facfe : 0xff4081)
  }
})

onUnmounted(() => {
  window.removeEventListener('resize', onWindowResize)
  window.removeEventListener('mousemove', onMouseMove)
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