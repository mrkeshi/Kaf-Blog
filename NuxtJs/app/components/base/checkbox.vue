<template>
  <div class="flex flex-col gap-1.5">
    <label :for="name + 'id'" class="inline-flex select-none items-center gap-2.5" :class="disabled ? 'cursor-not-allowed opacity-50' : 'cursor-pointer'">
      <span
        class="flex h-5 w-5 shrink-0 items-center justify-center rounded-md border-[1.5px] text-white transition-all duration-200"
        :class="value ? 'border-brand bg-brand shadow-[0_0_0_3px_rgb(124_107_255_/_0.18)]' : 'border-line bg-card-soft'"
        aria-hidden="true"
      >
        <svg v-if="value" width="12" height="12" viewBox="0 0 12 12" fill="none" aria-hidden="true">
          <path d="M2 6l3 3 5-5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
      </span>

      <input
        type="checkbox"
        :id="name + 'id'"
        :name="name"
        :checked="value"
        :disabled="disabled"
        @change="handle"
        class="sr-only"
        :aria-describedby="errorMessage ? `${name}-error` : undefined"
      />

      <span class="text-sm font-semibold text-ink-soft">{{ label }}</span>
    </label>

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
  modelValue: { type: Boolean, default: false },
  label: { type: String, default: '' },
  ignoreErrorMessage: { type: Boolean, default: false },
  disabled: { type: Boolean, default: false }
})

const emit = defineEmits(['update:modelValue'])

const { errorMessage, value, handleChange, setValue } = useField<boolean>(
  props.name, undefined, { initialValue: props.modelValue }
)

watch(() => props.modelValue, (val) => setValue(val))

function handle(e: Event) {
  const checked = (e.target as HTMLInputElement).checked
  emit('update:modelValue', checked)
  handleChange(e)
}
</script>
