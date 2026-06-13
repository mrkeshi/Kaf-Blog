<template>
  <div class="mx-auto max-w-2xl">
    <div class="animate-fade-in flex flex-col gap-8">
      <div class="text-center">
        <div class="mx-auto mb-4 flex h-16 w-16 items-center justify-center rounded-full border border-brand bg-brand/10 text-brand">
          <svg width="30" height="30" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" />
          </svg>
        </div>
        <h1 class="mb-2.5 text-2xl font-extrabold text-ink md:text-3xl">ارتباط با من</h1>
        <p class="text-[15px] leading-8 text-ink-soft">
          هم می‌توانی پیامت را به آدرس ایمیل
          <a
            v-if="setting.siteSettingData?.email_admin"
            :href="`mailto:${setting.siteSettingData.email_admin}`"
            dir="ltr"
            class="inline-block font-bold text-brand transition-opacity duration-200 hover:opacity-75"
          >{{ setting.siteSettingData.email_admin }}</a>
          بفرستی و هم اینجا پیام بگذاری.
        </p>
      </div>

      <div class="rounded-4xl border border-line bg-card p-6 shadow-card md:p-9">
        <Form
          @submit="sendDataContact"
          :validation-schema="contactSchema"
          v-slot="{ meta }"
          novalidate
          class="flex flex-col gap-5"
        >
          <div class="grid grid-cols-1 gap-5 sm:grid-cols-2">
            <base-input
              v-model="contactData.name"
              :disabled="loading"
              type="text"
              name="name"
              placeholder="نام شما"
              label="نام"
            />
            <base-input
              v-model="contactData.email"
              type="email"
              name="email"
              placeholder="آدرس ایمیل"
              :disabled="loading"
              label="ایمیل"
            />
            <div class="col-span-full">
              <base-textarea
                v-model="contactData.message"
                :disabled="loading"
                name="message"
                label="پیام"
                placeholder="هرچه دل تنگت می‌خواهد بنویس..."
              />
            </div>
          </div>

          <div>
            <base-button :disabled="loading" type="submit">
              <svg v-if="!loading" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z" />
              </svg>
              {{ loading ? 'در حال ارسال...' : 'ارسال پیام' }}
            </base-button>
          </div>
        </Form>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { Form } from 'vee-validate'
import * as Yup from 'yup'
import { useCustomToastify } from '~/composable/useCustomToastify'
import type { ContactDTO } from '~/models/Contact/ContactDTO'
import { sendContactDataService } from '~/services/Contact.Service'
import { generateSeoMeta } from '~/utilities/seo'

definePageMeta({ layout: 'simple-layout' })

const setting = useMySettingDataStore()
const loading = ref(false)

const contactSchema = Yup.object().shape({
  name: Yup.string().required('وارد کردن نام ضروری است.').min(1, 'حداقل یک کاراکتر وارد کنید.'),
  email: Yup.string().required('وارد کردن ایمیل الزامی است.').email('ایمیل وارد شده معتبر نیست'),
  message: Yup.string().required('نوشتن پیام الزامی است.').min(5, 'پیام باید حداقل ۵ کاراکتر داشته باشد.'),
})

const contactData: ContactDTO = reactive({
  name: '', email: '', message: ''
})

const { showSuccess } = useCustomToastify()

const sendDataContact = async () => {
  loading.value = true
  await sendContactDataService(contactData)
    .then(() => {
      contactData.name = ''
      contactData.email = ''
      contactData.message = ''
      showSuccess({ title: 'موفقیت', message: 'پیام شما با موفقیت ارسال شد.', autoClose: 4000 })
    })
    .finally(() => { loading.value = false })
}

const route = useRoute()

useHead(() => {
  if (!setting.siteSettingData) return {}

  return generateSeoMeta({
    title: `${setting.siteSettingData.site_name} - تماس با من`,
    description: 'از طریق این صفحه می‌توانید با من در ارتباط باشید.',
    image: setting.siteSettingData.site_logo || setting.siteSettingData.site_icon,
    url: `${setting.siteSettingData.site_url}${route.fullPath}`,
    keywords: ['تماس', 'ارتباط', 'ایمیل', 'فرم تماس'],
    author: setting.siteSettingData.meta_author,
    type: 'contact'
  })
})
</script>
