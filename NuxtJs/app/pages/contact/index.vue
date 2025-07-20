<template>
  <div>
    <div class="container mx-auto text-center py-12 max-md:py-12 h-auto">
      <h1 class="text-4xl font-bold mb-4 text-black-400">ارتباط با من</h1>
      <p class="text-lg text-black-300 mb-8 px-4 max-md:text-base"> هم می&zwnj;توانی پیام&zwnj;ات را به آدرس ایمیل
        me@mr-keshi.ir بفرستی و هم اینجا،</p>

      <div class="isolate px-6 py-2 sm:py-8 lg:px-6">

        <Form @submit="sendDataContact" :validation-schema="contactSchema" v-slot="{meta}" class="mx-auto  max-w-2xl">
          <div class="grid grid-cols-1 gap-x-8 gap-y-6 sm:grid-cols-2">
            <base-input v-model="contactData.name" :disabled="loading" type="text" name="name" placeholder="لطفا نام خود را وارد نمایید. "
              label="نام شما"></base-input>

            <base-input v-model="contactData.email" type="email" name="email"
              placeholder="لطفا ایمیل خود را وارد نمایید. " :disabled="loading" label=" آدرس ایمیل شما"></base-input>


            <base-textarea v-model="contactData.message" :disabled="loading" name="message" label="پیغام شما"
              placeholder="هرچه دل تنگت می‌خواهد بنویس..." />

          </div>
          <base-button class="mt-10" :disabled="loading">
            ارسال پیغام شما
          </base-button>
        </Form>
      </div>

    </div>
  </div>
</template>

<script lang="ts" setup>
import { Form } from 'vee-validate';
import * as Yup from 'yup'
import { useCustomToastify } from '~/composable/useCustomToastify';
import type { ContactDTO } from '~/models/Contact/ContactDTO';
import { sendContactDataService } from '~/services/Contact.Service';

definePageMeta({
  layout: 'simple-layout'
})

const loading = ref(false)

const contactSchema = Yup.object().shape({
  name: Yup.string().required("وارد کردن  نام ضروری هست.").min(1, "حداقل باید یک کاراکتر وارد کنید."),
  email: Yup.string()
    .required("وارد کردن ایمیل الزامی‌ست.")
    .email("ایمیل وارد شده معتبر نیست"),

  message: Yup.string()
    .required("نوشتن پیام الزامی است.")
    .min(5, "پیام باید حداقل ۵ کاراکتر داشته باشد."),
})

const contactData: ContactDTO = reactive({
  name: "",
  email: '',
  message: ''

})

const {showSuccess}=useCustomToastify()
const sendDataContact =async () => {
 loading.value=true
 await sendContactDataService(contactData).then((res)=>{
  contactData.name = ''
  contactData.email = ''
  contactData.message = ''
  showSuccess({
    title:"موفقیت",
    message:"پیغام شما با موفقیت ارسال شد.",
    autoClose:4000
  })
 }).finally(()=>{
  loading.value=false
 })
}
</script>

<style></style>