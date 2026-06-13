<template>
  <div v-if="music || cover" class="rounded-3xl border border-line bg-gradient-to-b from-card-soft to-card p-6 shadow-card">
    <div class="mb-4 flex items-center gap-2.5 border-b border-line pb-4 text-base font-extrabold text-ink">
      <span class="h-5 w-[3px] shrink-0 rounded-full bg-brand" aria-hidden="true"></span>
      <svg width="14" height="22" viewBox="0 0 21 31" fill="currentColor" class="text-brand" aria-hidden="true">
        <path d="M10.5 0.125V18.1479C9.49208 17.5671 8.33042 17.2083 7.08333 17.2083C3.30792 17.2083 0.25 20.2663 0.25 24.0417C0.25 27.8171 3.30792 30.875 7.08333 30.875C10.8588 30.875 13.9167 27.8171 13.9167 24.0417V6.95833H20.75V0.125H10.5Z" />
      </svg>
      <span>موسیقی</span>
    </div>

    <div class="mb-4 aspect-square overflow-hidden rounded-2xl bg-card-soft shadow-pop">
      <img
        v-if="cover"
        :src="cover"
        :alt="`${music_title} - ${music_artist}`"
        loading="lazy"
        class="h-full w-full object-cover transition-transform duration-1000"
        :class="isPlaying ? 'animate-spin-slow' : ''"
      />
      <div v-else class="flex h-full w-full items-center justify-center text-ink-faint">
        <svg width="40" height="40" viewBox="0 0 21 31" fill="currentColor">
          <path d="M10.5 0.125V18.1479C9.49208 17.5671 8.33042 17.2083 7.08333 17.2083C3.30792 17.2083 0.25 20.2663 0.25 24.0417C0.25 27.8171 3.30792 30.875 7.08333 30.875C10.8588 30.875 13.9167 27.8171 13.9167 24.0417V6.95833H20.75V0.125H10.5Z" />
        </svg>
      </div>
    </div>

    <div class="mb-4 text-center" aria-live="polite">
      <h4 class="truncate text-[15px] font-extrabold text-ink">{{ music_title || 'بدون عنوان' }}</h4>
      <p class="text-sm text-ink-faint">{{ music_artist || 'هنرمند' }}</p>
    </div>

    <div ref="equalizerRef" class="mb-3 flex h-8 items-end justify-between gap-[3px]" aria-hidden="true"></div>

    <div class="flex items-center justify-between gap-3">
      <span class="min-w-9 text-center text-xs tabular-nums text-ink-faint" aria-live="polite" aria-label="زمان پخش">{{ currentTime }}</span>

      <button
        @click="togglePlay"
        class="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-gradient-to-tr from-brand-strong to-brand text-white shadow-glow transition-transform duration-200 hover:scale-105"
        :aria-label="isPlaying ? 'توقف' : 'پخش'"
      >
        <svg v-if="isPlaying" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z" />
        </svg>
        <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M8 5v14l11-7z" />
        </svg>
      </button>

      <span class="min-w-9 text-center text-xs tabular-nums text-ink-faint" aria-label="مدت کل">{{ duration }}</span>
    </div>

    <audio ref="audioRef" preload="none" :src="music"></audio>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

defineProps({
  music: { type: String, default: '' },
  cover: { type: String, default: '' },
  music_title: { type: String, default: '' },
  music_artist: { type: String, default: '' },
})

const audioRef = ref<HTMLAudioElement | null>(null)
const equalizerRef = ref<HTMLDivElement | null>(null)
const isPlaying = ref(false)
const currentTime = ref('۰:۰۰')
const duration = ref('۰:۰۰')

const BAR_COUNT = 28
const bars: HTMLDivElement[] = []
let animFrame = 0

const toPersian = (n: number | string) =>
  n.toString().replace(/\d/g, d => '۰۱۲۳۴۵۶۷۸۹'[parseInt(d)])

const formatTime = (s: number) => {
  const m = Math.floor(s / 60)
  const sec = Math.floor(s % 60)
  return `${toPersian(m)}:${toPersian(sec.toString().padStart(2, '0'))}`
}

const updateVisualizer = () => {
  if (!audioRef.value || !isPlaying.value) return
  const progress = audioRef.value.currentTime / (audioRef.value.duration || 1)
  const activeBars = Math.round(BAR_COUNT * progress)
  bars.forEach((bar, i) => {
    bar.style.opacity = i < activeBars ? '1' : '0.18'
  })
  animFrame = requestAnimationFrame(updateVisualizer)
}

const togglePlay = () => {
  if (!audioRef.value) return
  if (audioRef.value.paused) {
    audioRef.value.play()
    isPlaying.value = true
    animFrame = requestAnimationFrame(updateVisualizer)
  } else {
    audioRef.value.pause()
    isPlaying.value = false
    cancelAnimationFrame(animFrame)
  }
}

onMounted(() => {
  if (!equalizerRef.value || !audioRef.value) return

  for (let i = 0; i < BAR_COUNT; i++) {
    const bar = document.createElement('div')
    bar.className = 'w-[3px] rounded-full bg-brand transition-opacity duration-300'
    bar.style.height = `${Math.random() * 20 + 8}px`
    bar.style.opacity = '0.18'
    equalizerRef.value.appendChild(bar)
    bars.push(bar)
  }

  audioRef.value.addEventListener('loadedmetadata', () => {
    duration.value = formatTime(audioRef.value!.duration)
  })
  audioRef.value.addEventListener('timeupdate', () => {
    currentTime.value = formatTime(audioRef.value!.currentTime)
  })
  audioRef.value.addEventListener('ended', () => {
    isPlaying.value = false
    cancelAnimationFrame(animFrame)
  })
})

onBeforeUnmount(() => {
  cancelAnimationFrame(animFrame)
  audioRef.value?.pause()
})
</script>
