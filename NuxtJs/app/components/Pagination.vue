<template>
  <nav v-if="totalPages > 1" dir="ltr" role="navigation" aria-label="صفحه‌بندی" class="flex items-center justify-center gap-1.5">
    <button
      @click="$emit('change', currentPage - 1)"
      :disabled="currentPage <= 1"
      aria-label="صفحه قبلی"
      class="flex h-10 w-10 items-center justify-center rounded-xl border border-line bg-card text-ink-soft transition-all duration-200 hover:border-brand/40 hover:text-brand disabled:opacity-35 disabled:hover:border-line disabled:hover:text-ink-soft"
    >
      <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true">
        <path d="M15 19l-7-7 7-7" stroke-linecap="round" stroke-linejoin="round" />
      </svg>
    </button>

    <template v-for="page in visiblePages" :key="page">
      <span v-if="page === '...'" aria-hidden="true" class="flex h-10 w-10 items-center justify-center text-ink-faint">…</span>
      <button
        v-else
        @click="$emit('change', Number(page))"
        :aria-label="`صفحه ${page}`"
        :aria-current="currentPage === Number(page) ? 'page' : undefined"
        :class="[
          'flex h-10 w-10 items-center justify-center rounded-xl border text-[15px] font-bold transition-all duration-200',
          currentPage === Number(page)
            ? 'border-brand bg-gradient-to-tr from-brand-strong to-brand text-white shadow-glow'
            : 'border-line bg-card text-ink-soft hover:border-brand/40 hover:text-brand'
        ]"
        v-persian-number="page"
      ></button>
    </template>

    <button
      @click="$emit('change', currentPage + 1)"
      :disabled="currentPage >= totalPages"
      aria-label="صفحه بعدی"
      class="flex h-10 w-10 items-center justify-center rounded-xl border border-line bg-card text-ink-soft transition-all duration-200 hover:border-brand/40 hover:text-brand disabled:opacity-35 disabled:hover:border-line disabled:hover:text-ink-soft"
    >
      <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true">
        <path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round" />
      </svg>
    </button>
  </nav>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
  currentPage: { type: Number, required: true },
  totalPages: { type: Number, required: true }
})

defineEmits<{ change: [page: number] }>()

const visiblePages = computed(() => {
  const { currentPage: cur, totalPages: total } = props
  if (total <= 7) return Array.from({ length: total }, (_, i) => i + 1)

  const pages: (number | '...')[] = []

  if (cur <= 4) {
    pages.push(1, 2, 3, 4, 5, '...', total)
  } else if (cur >= total - 3) {
    pages.push(1, '...', total - 4, total - 3, total - 2, total - 1, total)
  } else {
    pages.push(1, '...', cur - 1, cur, cur + 1, '...', total)
  }

  return pages
})
</script>
