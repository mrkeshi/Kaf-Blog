<template>
  <div class="flex flex-col items-start">
    <label :for="name + 'id'" class="text-base text-black-400 font-bold cursor-pointer flex items-center gap-2">
      <input
        type="checkbox"
        :id="name + 'id'"
        :name="name"
        :checked="value"
        :disabled="disabled"
        @change="handle"
        class="w-5 h-5 accent-blue-600 cursor-pointer rounded border-gray-300"
      />
      {{ label }}
    </label>
    <span
      v-if="!ignoreErrorMessage && errorMessage"
      class="text-red-500 text-base block text-right"
    >
      {{ errorMessage }}
    </span>
  </div>
</template>

<script lang="ts" setup>
import { useField } from 'vee-validate'

const props = defineProps({
  name: { type: String, required: true },
  modelValue: { type: Boolean, default: false },
  label: { type: String, default: '' },
  ignoreErrorMessage: { type: Boolean, default: false },
  disabled: { type: Boolean, default: false }
})

const emit = defineEmits(['update:modelValue'])

const { errorMessage, value, handleChange, setValue } = useField<boolean>(props.name, undefined, {
  initialValue: props.modelValue,
})

watch(() => props.modelValue, (val) => setValue(val))

function handle(e: Event) {
  const target = e.target as HTMLInputElement
  emit('update:modelValue', target.checked)
  handleChange(e)
}
</script>
