<template>
  <div class="flex flex-col gap-1.5">
    <label :for="`${name}id`" class="block text-sm font-bold text-ink-soft">{{ label }}</label>
    <input
      :type="type"
      :placeholder="placeholder"
      :name="name"
      :id="`${name}id`"
      autocomplete="given-name"
      :disabled="disabled"
      @input="handle"
      :value="value"
      :aria-invalid="!!errorMessage"
      :aria-describedby="errorMessage ? `${name}-error` : undefined"
      :class="[
        'w-full rounded-2xl border bg-card-soft px-4 py-3 text-[15px] text-ink outline-none transition-all duration-200 placeholder:text-ink-faint focus:ring-4 focus:ring-brand/15',
        errorMessage ? 'border-bad focus:border-bad' : 'border-line focus:border-brand',
        disabled ? 'cursor-not-allowed opacity-50' : ''
      ]"
    />
    <span
      v-if="!ignoreErrorMessage && errorMessage"
      :id="`${name}-error`"
      class="block text-sm text-bad"
      role="alert"
    >
      {{ errorMessage }}
    </span>
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
