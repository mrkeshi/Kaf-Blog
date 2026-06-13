<template>
  <div v-if="count > 0" class="inline-flex items-center gap-1.5 text-xs font-semibold text-ink-faint" :aria-label="`${count} دنبال‌کننده`">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" class="shrink-0 text-brand" aria-hidden="true">
      <path d="M16.04 7.81C17.2 8.65 18 9.77 18 11.25V13H22V11.25C22 9.23 18.5 8.08 16.04 7.81ZM15 6C16.93 6 18.5 4.43 18.5 2.5C18.5 0.57 16.93-1 15-1C14.46-1 13.96-.87 13.5-.65C14.13.24 14.5 1.33 14.5 2.5C14.5 3.67 14.13 4.76 13.5 5.65C13.96 5.87 14.46 6 15 6ZM9 6C10.93 6 12.5 4.43 12.5 2.5C12.5.57 10.93-1 9-1C7.07-1 5.5.57 5.5 2.5C5.5 4.43 7.07 6 9 6ZM9 7.75C6.66 7.75 2 8.92 2 11.25V13H16V11.25C16 8.92 11.34 7.75 9 7.75Z" />
    </svg>
    <span v-persian-number="count"></span>
    <span>دنبال‌کننده</span>
  </div>
</template>

<script lang="ts" setup>
defineProps({
  count: { type: Number, default: 0 }
})
</script>
