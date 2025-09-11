<template>
  <div class="w-full">
    <label :for="name + 'id'" class="block text-right font-bold text-[length:var(--text-sm-2)] md:text-base text-[color:var(--color-black-400)]">
      {{ label }} :
    </label>

    <div class="mt-2.5">
      <div
        class="relative group"
        @dragover.prevent="dragOver = true"
        @dragleave.prevent="dragOver = false"
        @drop.prevent="onDrop"
      >
        <button
          type="button"
          :disabled="disabled"
          @click="fileRef?.click()"
          :class="[
            'w-full rounded-2xl text-right transition-all duration-300 px-3.5 py-3.5 md:px-5 md:py-5',
            'flex flex-col sm:flex-row items-center justify-between gap-3 md:gap-4 text-center sm:text-right',
            disabled
              ? 'bg-[color:var(--color-black-100)] text-[color:var(--color-black-200)] cursor-not-allowed'
              : (gradient
                  ? 'gradient-surface text-[color:var(--color-black-500)]'
                  : 'bg-[color:var(--color-black-100)]/70 backdrop-blur border border-[color:var(--color-black-150)] text-[color:var(--color-black-300)] hover:bg-[color:var(--color-black-100)]'),
            dragOver && !disabled
              ? 'ring-4 ring-offset-0 ring-[color:var(--color-blue-500)]/40'
              : 'hover:shadow-md',
            errorMessage ? 'error-input' : ''
          ]"
        >
          <div class="flex items-center gap-3 justify-center sm:justify-start">
            <div :class="[
              'w-11 h-11 md:w-12 md:h-12 rounded-xl grid place-items-center transition-all duration-300',
              dragOver ? 'bg-white/90 text-[color:var(--color-blue-500)] scale-105 shadow-md' : 'bg-white/80 text-[color:var(--color-blue-500)] shadow'
            ]">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4 16v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-2M16 12l-4-4m0 0l-4 4m4-4v12"/>
              </svg>
            </div>

            <div class="flex flex-col">
              <span class="font-semibold leading-6 text-[color:var(--color-black-300)] text-sm md:text-base">یک تصویر انتخاب یا دراپ کنید</span>
              <span class="text-[10px] md:text-xs text-[color:var(--color-black-200)] mt-0.5">JPG · PNG · WEBP · GIF · HEIC/HEIF — حداکثر {{ maxSizeMB }}MB</span>
            </div>
          </div>

          <div class="flex items-center justify-center sm:justify-end gap-2 md:gap-3 w-full sm:w-auto mt-3 sm:mt-0">
            <span class="hidden sm:inline text-[color:var(--color-black-500)]/80 font-semibold">انتخاب فایل</span>
            <span class="inline-flex items-center justify-center gap-1 text-[10px] md:text-xs px-2 py-1 rounded-full bg-white/70 text-[color:var(--color-black-200)] shadow min-w-[90px]">
              Drag & Drop
            </span>
          </div>

          <input
            :id="name + 'id'"
            :name="name"
            type="file"
            accept="image/*,.heic,.heif"
            :disabled="disabled"
            class="hidden"
            ref="fileRef"
            @change="onFilePicked"
          />
        </button>

        <transition name="fade">
          <div v-if="previewUrl" class="mt-3 md:mt-4">
            <div :class="[
              'rounded-2xl p-[2px]',
              gradient ? 'animated-border' : 'bg-[color:var(--color-black-150)]/70'
            ]">
              <div class="rounded-[14px] overflow-hidden gradient-preview shadow-lg">
                <div class="w-full h-40 sm:h-56 md:h-64">
                  <img :src="previewUrl" alt="preview" class="w-full h-full object-contain" />
                </div>
                <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2 px-2 py-2">
                  <div class="text-[10px] md:text-xs px-2 py-1 rounded-lg bg-white/90 text-[color:var(--color-black-200)] shadow self-start">
                    {{ fileName }} <span v-if="fileSizeKB">· {{ humanSize }}</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <button
                      type="button"
                      class="text-xs px-2 py-1 rounded-lg bg-white/90 text-[color:var(--color-blue-500)] shadow hover:bg-white"
                      :disabled="disabled"
                      @click="fileRef?.click()"
                    >تعویض</button>
                    <button
                      type="button"
                      class="text-xs px-2 py-1 rounded-lg bg-white/90 text-red-600 shadow hover:bg-white"
                      :disabled="disabled"
                      @click="clearFile"
                    >حذف</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </transition>
      </div>

      <span v-if="!ignoreErrorMessage && errorMessage" class="text-red-500 text-[length:var(--text-sm-2)] mt-2 -mb-4 block text-right">
        {{ errorMessage }}
      </span>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, watch, onBeforeUnmount, computed } from 'vue'
import { useField } from 'vee-validate'

const props = defineProps({
  name: { type: String, required: true },
  modelValue: { default: null },
  label: { type: String, default: '' },
  placeholder: { type: String, default: '' },
  ignoreErrorMessage: { type: Boolean, default: true },
  disabled: { type: Boolean, default: false },
  maxSizeMB: { type: Number, default: 15 },
  gradient: { type: Boolean, default: true }
})

const emit = defineEmits(['update:modelValue'])

const fileRef = ref<HTMLInputElement | null>(null)
const dragOver = ref(false)
const previewUrl = ref<string | null>(null)
const fileName = ref<string>('')
const fileSizeKB = ref<number | null>(null)

const ALLOWED_MIME = [
  'image/jpeg','image/png','image/webp','image/gif',
  'image/heic','image/heif'
]

function fileValidator(file: File | null) {
  if (!file) return true
  const validType = ALLOWED_MIME.includes(file.type) || /\.(heic|heif|jpe?g|png|webp|gif)$/i.test(file.name)
  if (!validType) return 'فقط فرمت‌های تصویر مجاز است (JPEG/PNG/WebP/GIF/HEIC/HEIF).'
  const okSize = file.size <= props.maxSizeMB * 1024 * 1024
  if (!okSize) return `حجم فایل نباید بیش از ${props.maxSizeMB} مگابایت باشد.`
  return true
}

const { errorMessage, value, setValue, validate } = useField<File | null>(
  props.name,
  (val) => fileValidator(val as File | null),
  { initialValue: props.modelValue as File | null }
)

watch(() => props.modelValue, (val) => setValue(val as File | null))

watch(value, (val) => {
  revokePreview()
  if (val instanceof File) {
    previewUrl.value = URL.createObjectURL(val)
    fileName.value = val.name
    fileSizeKB.value = Math.round(val.size / 1024)
  } else {
    previewUrl.value = null
    fileName.value = ''
    fileSizeKB.value = null
  }
})

const humanSize = computed(() => {
  if (!fileSizeKB.value) return ''
  const kb = fileSizeKB.value
  if (kb < 1024) return kb + ' KB'
  const mb = (kb / 1024).toFixed(1)
  return mb + ' MB'
})

function onFilePicked(e: Event) {
  const target = e.target as HTMLInputElement
  const file = target.files && target.files[0] ? target.files[0] : null
  updateFile(file)
}

function onDrop(e: DragEvent) {
  dragOver.value = false
  const file = e.dataTransfer?.files && e.dataTransfer.files[0] ? e.dataTransfer.files[0] : null
  updateFile(file)
}

function updateFile(file: File | null) {
  emit('update:modelValue', file)
  setValue(file as File | null)
  validate()
}

function clearFile() {
  emit('update:modelValue', null)
  setValue(null)
  validate()
}

function revokePreview() {
  if (previewUrl.value) {
    URL.revokeObjectURL(previewUrl.value)
    previewUrl.value = null
  }
}

onBeforeUnmount(() => revokePreview())
</script>

<style scoped>
.error-input {
  box-shadow: 0 0 0 2px rgba(239, 68, 68, 0.35) inset;
  border-color: rgba(239, 68, 68, 0.75) !important;
}

.fade-enter-active, .fade-leave-active { transition: opacity .2s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

.gradient-surface {
  background: linear-gradient(120deg, #a1c4fd, #c2e9fb, #fbc2eb, #a6c0fe, #f68084);
  background-size: 300% 300%;
  animation: gradientShift 8s ease infinite;
}

.animated-border {
  background: linear-gradient(120deg, #60a5fa, #a78bfa, #f472b6, #34d399, #60a5fa);
  background-size: 300% 300%;
  animation: gradientShift 10s linear infinite;
}

.gradient-preview {
  background: linear-gradient(135deg, rgba(255,255,255,0.8), rgba(240,240,255,0.9));
}

@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
</style>
