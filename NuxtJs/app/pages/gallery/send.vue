<template>
  <div class="min-h-screen">
    <div class="container mx-auto px-4">
      <section class="text-center py-12 lg:py-16">
        <h1 class="text-3xl md:text-4xl font-bold mb-3 text-black-500">ارسال تصویر به گالری</h1>
        <p class="text-black-300 max-w-2xl mx-auto leading-relaxed">
          می‌تونی تصویرت رو اینجا آپلود کنی.
        </p>
      </section>

      <div class="max-w-3xl mx-auto">
        <div class="p-6 md:p-8">
          <Form
            @submit="sendDataContact"
            :validation-schema="gallerySchema"
            :initial-values="initialValues"
            :validate-on-mount="false"
            v-slot="{ meta: formMeta }"
            class="space-y-6"
          >
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
              <BaseInput
                name="sender_name"
                label="نام شما"
                placeholder="نام شما"
                :disabled="loading"
                type="text"
                :ignore-error-message="true"
              />
              <ErrorMessage name="sender_name" v-slot="{ message }">
                <p v-if="formMeta.submitCount > 0" class="text-red-500 text-sm mt-1">{{ message }}</p>
              </ErrorMessage>

              <BaseInput
                name="location"
                label="عنوان یا موقعیت مکانی"
                placeholder="مثلاً: تهران / شیراز / ..."
                :disabled="loading"
                type="text"
                :ignore-error-message="true"
              />
              <ErrorMessage name="location" v-slot="{ message }">
                <p v-if="formMeta.submitCount > 0" class="text-red-500 text-sm mt-1">{{ message }}</p>
              </ErrorMessage>

              <div class="sm:col-span-2">
                <BaseInputFile
                  name="photo"
                  label="آپلود تصویر"
                  placeholder="یک تصویر انتخاب یا دراپ کنید"
                  :disabled="loading"
                  :max-size-m-b="15"
                  :ignore-error-message="true"
                />
                <ErrorMessage name="photo" v-slot="{ message }">
                  <p v-if="formMeta.submitCount > 0" class="text-red-500 text-sm mt-2 text-right">{{ message }}</p>
                </ErrorMessage>
              </div>
            </div>

            <div class="flex items-center justify-end gap-4 pt-2">
              <BaseButton
                type="submit"
                :disabled="loading || formMeta.pending || !formMeta.valid"
              >
                <span v-if="!loading">ارسال به گالری</span>
                <span v-else class="inline-flex items-center gap-2">
                  <svg class="w-4 h-4 animate-spin" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z" />
                  </svg>
                  در حال ارسال...
                </span>
              </BaseButton>
            </div>
          </Form>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
definePageMeta({ layout: 'simple-layout' })

import { ref } from 'vue'
import { Form, ErrorMessage } from 'vee-validate'
import * as yup from 'yup'
import { sendImageDataService } from '~/services/Gallery.service'
import { useCustomToastify } from '~/composable/useCustomToastify'
import { generateSeoMeta } from '~/utilities/seo';

const { showSuccess, showError, showInfo } = useCustomToastify()
const loading = ref(false)

const initialValues = {
  sender_name: '',
  location: '',
  photo: null as File | File[] | null
}

const gallerySchema = yup.object({
  sender_name: yup.string().required('نام الزامی است'),
  location: yup.string().required('موقعیت مکانی الزامی است'),
  photo: yup
    .mixed<File>()
    .required('انتخاب تصویر الزامی است')
    .test('file-required', 'یک فایل تصویر انتخاب کنید', (v) => !!v),
})

async function sendDataContact(values: typeof initialValues, actions: { resetForm: () => void }) {
  if (loading.value) return
  loading.value = true
  try {
    const fd = new FormData()
    fd.append('sender_name', values.sender_name || '')
    fd.append('location', values.location || '')
    const file = Array.isArray(values.photo) ? values.photo[0] : values.photo
    if (file) fd.append('photo', file as File)

    await sendImageDataService(fd)

    showSuccess({ title: 'موفق', message: 'تصویر شما با موفقیت ارسال شد', autoClose: 4000 })
    showInfo({ title: 'اطلاع', message: 'پس از تأیید، عکس شما به گالری اضافه خواهد شد', autoClose: 6000 })

    actions.resetForm()
  } catch (e) {
    showError({ title: 'ناموفق', message: 'لطفاً دوباره تلاش کنید', autoClose: 4000 })
    console.error(e)
  } finally {
    loading.value = false
  }
}
const route = useRoute()
const setting = useMySettingDataStore()

watchEffect(() => {
  if (setting.siteSettingData) {
    const seo = generateSeoMeta({
      title: `${setting.siteSettingData.site_name} - ارسال به گالری من`,
      description: 'در این صفحه می‌توانید تصاویر خود را برای گالری من ارسال کنید.',
      image: setting.siteSettingData.site_logo || setting.siteSettingData.site_icon,
      url: `${setting.siteSettingData.site_url}${route.fullPath}`,
      keywords: [
        'ارسال تصویر',
        'آپلود گالری',
        `${setting.siteSettingData.site_name}`,
        'ارسال به گالری من'
      ],
      author: setting.siteSettingData.meta_author,
      type: 'article'
    })

    useHead(seo)
  }
})

</script>

<style scoped>
.container { direction: rtl; }
:deep(.error-input) {
  box-shadow: 0 0 0 2px rgba(239, 68, 68, 0.35) inset;
  border-color: rgba(239, 68, 68, 0.75) !important;
}
h1 { letter-spacing: -0.015em; }
</style>
