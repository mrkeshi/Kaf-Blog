<template>
  <div>
    <label :for="name + 'id'" class="block text-base text-black-400 font-bold text-right">{{ label }} :</label>
    <div class="mt-2.5">
      <input
        :type="type"
        :placeholder="placeholder"
        :name="name"
        :id="name + 'id'"
        autocomplete="given-name"
        :disabled="disabled"
        @input="handle"
        :value="value"
        :class="[
          'block w-full rounded-2xl px-3.5 py-3.5 text-base text-black-300 outline-2 -outline-offset-1 outline-black-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-blue-600',
          { 'error-input': errorMessage },
          { 'cursor-not-allowed bg-gray-100 text-gray-400': disabled }
        ]"
      />
      <span v-if="!ignoreErrorMessage && errorMessage" class="text-red-500 text-base mt-2 -mb-4 block text-right">
        {{ errorMessage }}
      </span>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { useField } from 'vee-validate'

const props = defineProps({
  name: { type: String, required: true },
  modelValue: { default: '' },
  label: { type: String, default: '' },
  placeholder: { type: String, default: '' },
  type: { type: String, default: 'text' },
  ignoreErrorMessage: { type: Boolean, default: false },
  disabled: { type: Boolean, default: false }
})

const { errorMessage, value, handleChange, setValue } = useField(props.name, undefined, {
  initialValue: props.modelValue,
})
const emit = defineEmits(['update:modelValue'])

watch(() => props.modelValue, (val) => setValue(val))

const handle = (e: any) => {
  emit('update:modelValue', e.target.value)
  handleChange(e)
}
</script>
