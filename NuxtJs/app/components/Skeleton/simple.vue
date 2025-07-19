<template>
  <div class="flex flex-col gap-2 h-auto">
    <div
      v-for="i in repeat"
      :key="i"
      :class="[
        ...customClasses,
        'bg-black-100',
        'relative',
        'overflow-hidden',
        'animate-shimmer'
      ]"
    >
      <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/50 to-transparent"></div>
    </div>
  </div>
</template>

<script setup>
import { toRefs, computed, useAttrs } from 'vue'

const props = defineProps({
  repeat: {
    type: Number,
    default: 1
  }
})

const { repeat } = toRefs(props)
const attrs = useAttrs()

const customClasses = computed(() => {
  if (!attrs.class) return []
  if (typeof attrs.class === 'string') return attrs.class.trim().split(/\s+/)
  if (Array.isArray(attrs.class)) return attrs.class
  return []
})
</script>

<style>
@keyframes shimmer {
  0% {
    background-position: -200% 0;
  }
  100% {
    background-position: 200% 0;
  }
}
.animate-shimmer {
  background: linear-gradient(
    90deg,
    #d9d9d9 25%,
    #eeeeee 50%,
    #d9d9d9 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}
</style>
