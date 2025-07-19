<template>
  <div class="flex gap-2">
    <div
      v-for="i in repeat"
      :key="i"
      :class="[
        widthClass,
        heightClass,
        radiusClass,
        'bg-gray-300',
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
import { computed } from 'vue'

const props = defineProps({
  repeat: {
    type: Number,
    default: 1
  },
  width: {
    type: String,
    default: '10'  
  },
  height: {
    type: String,
    default: '6'   
  },
  radius: {
    type: String,
    default: 'lg'  
  }
})

const widthClass = computed(() => `w-${props.width}`)
const heightClass = computed(() => `h-${props.height}`)
const radiusClass = computed(() => `rounded-${props.radius}`)
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
    #d1d5db 25%,  /* خاکستری-300 */
    #f3f4f6 50%,  /* خاکستری-100 */
    #d1d5db 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}
</style>
