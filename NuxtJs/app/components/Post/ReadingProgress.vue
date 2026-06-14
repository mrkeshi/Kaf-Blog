<template>
  <Teleport to="body">
    <!-- Fixed reading-progress bar at very top of viewport -->
    <div
      role="progressbar"
      :aria-valuenow="Math.round(progress)"
      aria-valuemin="0"
      aria-valuemax="100"
      :aria-label="`پیشرفت خواندن: ${Math.round(progress)} درصد`"
      class="reading-progress-bar"
      :style="{ transform: `scaleX(${progress / 100})` }"
    ></div>

    <!-- Reading time + progress pill that floats bottom-right -->
    <Transition
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0 translate-y-4"
      leave-active-class="transition-all duration-200 ease-in"
      leave-to-class="opacity-0 translate-y-4"
    >
      <div
        v-if="showPill && readingTime > 0"
        class="fixed bottom-6 left-6 z-40 flex items-center gap-2 rounded-full border border-line bg-card/90 px-4 py-2 shadow-pop backdrop-blur-md"
        aria-live="polite"
      >
        <!-- Clock icon -->
        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" class="shrink-0 text-brand" aria-hidden="true">
          <path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67V7z"/>
        </svg>

        <span class="text-xs font-bold text-ink-soft" aria-hidden="true">
          {{ remainingLabel }}
        </span>

        <!-- Mini circular progress -->
        <svg width="22" height="22" viewBox="0 0 22 22" class="shrink-0 -rotate-90" aria-hidden="true">
          <circle cx="11" cy="11" r="8" fill="none" stroke="var(--color-line)" stroke-width="2.5"/>
          <circle
            cx="11" cy="11" r="8"
            fill="none"
            stroke="var(--color-brand)"
            stroke-width="2.5"
            stroke-linecap="round"
            :stroke-dasharray="circumference"
            :stroke-dashoffset="dashOffset"
            class="transition-all duration-150"
          />
        </svg>
      </div>
    </Transition>
  </Teleport>
</template>

<script lang="ts" setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'

const props = defineProps<{
  /** Word count of the article (approximate) */
  wordCount: number
  /** Selector for the scrollable article element */
  articleSelector?: string
}>()

const WORDS_PER_MINUTE = 200
const circumference = 2 * Math.PI * 8  // r=8

const progress   = ref(0)
const showPill   = ref(false)

/** Total reading time in minutes */
const readingTime = computed(() =>
  props.wordCount > 0 ? Math.max(1, Math.ceil(props.wordCount / WORDS_PER_MINUTE)) : 0
)

const remainingMinutes = computed(() => {
  const done = progress.value / 100
  const left = Math.ceil(readingTime.value * (1 - done))
  return left
})

const remainingLabel = computed(() => {
  if (progress.value >= 98) return 'خواندید!'
  const m = remainingMinutes.value
  return m <= 1 ? 'کمتر از ۱ دقیقه' : `${toPersian(m)} دقیقه مانده`
})

const dashOffset = computed(() =>
  circumference * (1 - progress.value / 100)
)

function toPersian(n: number) {
  return n.toString().replace(/\d/g, d => '۰۱۲۳۴۵۶۷۸۹'[parseInt(d)])
}

function calcProgress() {
  const article = props.articleSelector
    ? document.querySelector<HTMLElement>(props.articleSelector)
    : document.querySelector<HTMLElement>('[role="article"]')

  if (!article) {
    // Fallback: use full page scroll
    const scrollTop  = window.scrollY
    const docHeight  = document.documentElement.scrollHeight - window.innerHeight
    progress.value   = docHeight > 0 ? Math.min(100, (scrollTop / docHeight) * 100) : 0
    return
  }

  const rect = article.getBoundingClientRect()
  const articleTop    = rect.top + window.scrollY
  const articleHeight = article.offsetHeight
  const scrolled      = window.scrollY - articleTop + window.innerHeight * 0.15

  progress.value = Math.min(100, Math.max(0, (scrolled / articleHeight) * 100))
}

function onScroll() {
  calcProgress()
  showPill.value = window.scrollY > 200
}

onMounted(() => {
  calcProgress()
  window.addEventListener('scroll', onScroll, { passive: true })
})

onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
})
</script>
