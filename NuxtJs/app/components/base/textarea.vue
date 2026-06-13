<template>
  <div :class="['flex flex-col gap-1.5', fullWidth ? 'col-span-full' : '']">
    <label :for="name" class="block text-sm font-bold text-ink-soft">{{ label }}</label>

    <div class="relative">
      <textarea
        :id="name"
        :name="name"
        :placeholder="placeholder"
        :rows="rows"
        :value="inputValue"
        @input="handleInputChange"
        :disabled="disabled"
        :aria-invalid="!!errorMessage"
        :aria-describedby="errorMessage ? `${name}-error` : undefined"
        :class="[
          'min-h-[140px] w-full resize-y rounded-2xl border bg-card-soft px-4 py-3 text-[15px] leading-7 text-ink outline-none transition-all duration-200 placeholder:text-ink-faint focus:ring-4 focus:ring-brand/15',
          errorMessage ? 'border-bad focus:border-bad' : 'border-line focus:border-brand',
          disabled ? 'cursor-not-allowed opacity-50' : ''
        ]"
      ></textarea>

      <div
        v-if="maxLength"
        :class="[
          'pointer-events-none absolute bottom-2.5 end-3.5 text-xs',
          charCount > maxLength ? 'text-bad' : 'text-ink-faint'
        ]"
      >
        <span v-persian-number="charCount"></span>/<span v-persian-number="maxLength"></span>
      </div>
    </div>

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

<script setup lang="ts">
import { computed } from 'vue'
import { useField } from 'vee-validate'

const props = defineProps({
  name: { type: String, required: true },
  modelValue: { default: '' },
  label: { type: String, default: '' },
  placeholder: { type: String, default: '' },
  rows: { type: Number, default: 6 },
  ignoreErrorMessage: { type: Boolean, default: false },
  disabled: { type: Boolean, default: false },
  fullWidth: { type: Boolean, default: true },
  maxLength: { type: Number, default: 0 }
})

const emit = defineEmits(['update:modelValue'])

const {
  errorMessage,
  value: inputValue,
  handleChange,
  setValue,
} = useField(props.name, undefined, { initialValue: props.modelValue })

watch(() => props.modelValue, (val) => setValue(val))

const charCount = computed(() =>
  typeof inputValue.value === 'string' ? inputValue.value.length : 0
)

function handleInputChange(e: Event) {
  const value = (e.target as HTMLTextAreaElement).value
  emit('update:modelValue', value)
  handleChange(e)
}
</script>
