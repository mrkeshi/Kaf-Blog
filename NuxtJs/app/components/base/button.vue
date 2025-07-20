<!-- components/BaseButton.vue -->
<template>
  <button :type="type" :disabled="disabled" class="block w-full rounded-xl cursor-pointer px-3.5 py-3.5 text-center text-base font-semibold text-white shadow-xs
    focus-visible:outline-2 focus-visible:outline-offset-2
    transition duration-200
    disabled:opacity-50 disabled:cursor-not-allowed
    " :class="[
      color === 'primary' ? 'bg-black-400 hover:bg-blue-600 focus-visible:outline-blue-600' : '',
      color === 'secondary' ? 'bg-gray-600 hover:bg-gray-700 focus-visible:outline-gray-700' : '',
      customClass
    ]">
    <slot />
  </button>
</template>

<script setup lang="ts">
const props = defineProps({
  type: String as () => 'submit' | 'reset' | 'button' | undefined,
  color: { type: String, default: 'primary' },
  disabled: { type: Boolean, default: false },
  customClass: { type: String, default: '' }
})
</script>
