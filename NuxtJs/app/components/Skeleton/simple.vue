<template>
  <div
    v-for="i in repeat"
    :key="i"
    role="status"
    aria-label="در حال بارگذاری..."
    :class="['animate-pulse bg-card-soft', attrClass]"
  ></div>
</template>

<script setup lang="ts">
import { computed, useAttrs } from 'vue'

defineOptions({ inheritAttrs: false })

const props = defineProps({
  repeat: { type: Number, default: 1 }
})

const attrs = useAttrs()
const attrClass = computed(() => attrs.class as string | undefined)
</script>
