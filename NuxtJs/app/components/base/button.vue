<template>
  <button
    :type="type"
    :disabled="disabled"
    :class="[
      'inline-flex w-full items-center justify-center gap-2 rounded-full px-6 py-3 text-[15px] font-bold transition-all duration-300 focus-visible:ring-4 focus-visible:ring-brand/25 disabled:pointer-events-none disabled:opacity-40',
      color === 'secondary'
        ? 'border border-line bg-transparent text-ink hover:border-ink-faint hover:bg-card-soft'
        : 'bg-gradient-to-tr from-brand-strong to-brand text-white shadow-glow hover:-translate-y-0.5 hover:shadow-glow-lg active:translate-y-0',
      customClass
    ]"
  >
    <svg
      v-if="disabled"
      class="h-4 w-4 animate-spin-slow"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      aria-hidden="true"
    >
      <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83" stroke-linecap="round" />
    </svg>
    <slot />
  </button>
</template>

<script setup lang="ts">
defineProps({
  type: { type: String as () => 'submit' | 'reset' | 'button' | undefined },
  color: { type: String, default: 'primary' },
  disabled: { type: Boolean, default: false },
  customClass: { type: String, default: '' }
})
</script>
