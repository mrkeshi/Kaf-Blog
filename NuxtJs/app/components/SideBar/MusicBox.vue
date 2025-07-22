<template>
  <div>
    <div class="rounded-xl my-8 max-md:my-6">
      <div class="header-aside-box flex items-center">
        <svg width="21" height="31" viewBox="0 0 21 31" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M10.5 0.125V18.1479C9.49208 17.5671 8.33042 17.2083 7.08333 17.2083C3.30792 17.2083 0.25 20.2663 0.25 24.0417C0.25 27.8171 3.30792 30.875 7.08333 30.875C10.8588 30.875 13.9167 27.8171 13.9167 24.0417V6.95833H20.75V0.125H10.5Z" fill="black"/>
        </svg>
        <span class="mx-1">
          <svg width="3" height="35" viewBox="0 0 4 41" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="-2.48486" width="6.21212" height="41" fill="#323232"/>
          </svg>
        </span>
        <h4 class="text-[17px] max-md:text-base text-black-300 font-black">موسیقی</h4>
      </div>
      <div class="BodyCardCateGory w-full flex flex-col mt-5">
        <img :src="cover" class="w-full rounded-2xl h-auto" loading="lazy"  :alt="music_title+music_artist"/>
        <h4 class="font-black text-center text-[17px] mt-3 text-black-400">{{ music_title }} </h4>
        <h5 class="font-medium text-base text-center text-black-200">{{music_artist}}</h5>
        <div class="rounded-xl p-0 w-full mt-2">
          <audio ref="audioRef"  preload="none" :src="audioSrc"></audio>
          <div class="flex flex-row-reverse items-end justify-between gap-3">
            <div class="flex flex-col items-center w-16">
              <button @click="togglePlay" class="w-full h-16 text-white bg-black-400 rounded-full text-3xl flex items-center justify-center">
                {{ isPlaying ? '⏸' : '▶' }}
              </button>
              <span class="text-sm text-gray-600 mt-1">{{ currentTime }}</span>
            </div>
            <div class="flex flex-col items-center justify-end flex-1">
              <div ref="equalizerRef" class="flex items-end justify-between h-14 w-full flex-row-reverse"></div>
              <div class="text-sm text-gray-600 mt-2 self-start">{{ duration }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>



defineProps({
  music:{
    type:String ,
    default:' '
  },
  cover:{
    type:String,
    default:' '
  },
  music_title:{
    type:String,
    default:' '
  },
  music_artist:{
    type:String,
    default:' '
  },
})

import { ref, onMounted, onBeforeUnmount } from 'vue'
import { string } from 'yup'

const audioSrc = './heydo.mp3'
const audioRef = ref<HTMLAudioElement | null>(null)
const equalizerRef = ref<HTMLDivElement | null>(null)

const isPlaying = ref(false)
const currentTime = ref('۰:۰۰')
const duration = ref('۰:۰۰')

const BAR_COUNT = 40
const bars: HTMLDivElement[] = []

const toPersian = (num: number | string) =>
  num.toString().replace(/\d/g, d => '۰۱۲۳۴۵۶۷۸۹'[parseInt(d)])

const formatTime = (seconds: number) => {
  const m = Math.floor(seconds / 60)
  const s = Math.floor(seconds % 60)
  return `${toPersian(m)}:${toPersian(s.toString().padStart(2, '0'))}`
}

const updateVisualizer = () => {
  if (audioRef.value && isPlaying.value) {
    const percent = audioRef.value.currentTime / (audioRef.value.duration || 1)
    const activeBars = Math.round(BAR_COUNT * percent)

    bars.forEach((bar, i) => {
      bar.style.opacity = i < activeBars ? '1' : '0.2'
    })

    requestAnimationFrame(updateVisualizer)
  }
}

const togglePlay = () => {
  if (!audioRef.value) return

  // فقط اگر src خالی بود، تنظیمش کن
  if (!audioRef.value.src) {
    audioRef.value.src = music || ''
  }

  if (audioRef.value.paused) {
    audioRef.value.play()
    isPlaying.value = true
    updateVisualizer()
  } else {
    audioRef.value.pause()
    isPlaying.value = false
    bars.forEach(bar => (bar.style.animationPlayState = 'paused'))
  }
}


onMounted(() => {
  if (!audioRef.value || !equalizerRef.value) return

  for (let i = 0; i < BAR_COUNT; i++) {
    const bar = document.createElement('div')
    bar.classList.add('bar', 'bg-black')
    bar.style.height = `${Math.random() * 40 + 20}px`
    equalizerRef.value.appendChild(bar)
    bars.push(bar)
  }

  audioRef.value.addEventListener('loadedmetadata', () => {
    duration.value = formatTime(audioRef.value!.duration)
  })

  audioRef.value.addEventListener('timeupdate', () => {
    currentTime.value = formatTime(audioRef.value!.currentTime)
  })
})

onBeforeUnmount(() => {
  if (!audioRef.value) return
  audioRef.value.pause()
})
</script>

<style scoped>
.bar {
  width: 2px;
  margin-left: 2px;
  margin-right: 2px;
  border-radius: 1px;
  transition: opacity 0.3s;
}
.bg-black {
  background-color: black;
}
</style>
