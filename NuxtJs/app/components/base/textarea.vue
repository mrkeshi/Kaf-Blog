<template>
  <div class="sm:col-span-2">
    <label :for="name" class="block text-base text-black-400 font-bold text-right">
      {{ label }}
    </label>
    <div class="mt-2.5">
      <textarea
        :id="name"
        :name="name"
        :placeholder="placeholder"
        :rows="rows"
        :value="inputValue"
        @input="handleInputChange"
        :disabled="disabled"
        :class="[
          'block w-full rounded-2xl px-3.5 py-3.5 text-base text-black-300 outline-2 -outline-offset-1 outline-black-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-blue-600',
          { 'error-input': errorMessage },
          { 'cursor-not-allowed bg-gray-100 text-gray-400': disabled }
        ]"
      ></textarea>
      <span v-if="!ignoreErrorMessage && errorMessage" class="text-red-500 text-base mt-2 -mb-4 block text-right">
        {{ errorMessage }}
      </span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useField } from 'vee-validate'

const props = defineProps({
  name: { type: String, required: true },
  modelValue: { default: '' },
  label: { type: String, default: '' },
  placeholder: { type: String, default: '' },
  rows: { type: Number, default: 6 },
  ignoreErrorMessage: { type: Boolean, default: false },
  disabled: { type: Boolean, default: false }
})

const emit = defineEmits(['update:modelValue'])

const {
  errorMessage,
  value: inputValue,
  handleChange,
  setValue,
} = useField(props.name, undefined, {
  initialValue: props.modelValue,
})

watch(
  () => props.modelValue,
  (val) => {
    setValue(val)
  }
)

function handleInputChange(e: Event) {
  const value = (e.target as HTMLTextAreaElement).value
  emit('update:modelValue', value)
  handleChange(e)
}
</script>
