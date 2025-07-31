<template>

  <Form @submit="sendComment" :validation-schema="CommentSchema" v-slot="{ meta, resetForm }" class="mt-1">
    <div class="grid grid-cols-1 gap-x-8 gap-y-6 sm:grid-cols-2">
      <base-input v-model="CommentData.name" :disabled="loading" type="text" name="name"
        placeholder="لطفا نام خود را وارد نمایید. " label="نام شما"></base-input>

      <base-input v-model="CommentData.email" type="email" name="email" placeholder="لطفا ایمیل خود را وارد نمایید. "
        :disabled="loading" label=" آدرس ایمیل شما"></base-input>


      <base-textarea v-model="CommentData.message" :disabled="loading" name="message" label="پیغام شما"
        placeholder="هرچه دل تنگت می‌خواهد بنویس..." />

      <BaseCheckbox name="privte" v-model="CommentData.privte" label="نظر به صورت خصوصی ارسال شود." />



    </div>
    <base-button class="my-6 " :disabled="loading">
      ارسال پیغام شما
    </base-button>
  </Form>
</template>

<script lang="ts" setup>
import { Form } from 'vee-validate';
import * as Yup from 'yup'
import { useCustomToastify } from '~/composable/useCustomToastify';
import { type CommentDTO } from '~/models/Post/CommentDTO';
import { sendCommentDataService } from '~/services/Post.Service';

const loading = ref(false)

const CommentSchema = Yup.object().shape({
  name: Yup.string().required("وارد کردن  نام ضروری هست.").min(1, "حداقل باید یک کاراکتر وارد کنید."),
  email: Yup.string()
    .required("وارد کردن ایمیل الزامی‌ست.")
    .email("ایمیل وارد شده معتبر نیست"),

  message: Yup.string()
    .required("نوشتن پیام الزامی است.")
    .min(5, "پیام باید حداقل ۵ کاراکتر داشته باشد."),
})

const { post } = defineProps({
  post: {
    required: true,
    type: Number
  }
})
const { showSuccess } = useCustomToastify()

const CommentData: CommentDTO = reactive({
  name: "",
  email: '',
  message: '',
  post: post,
  privte: false
})

const sendComment = async (_: unknown, { resetForm }: any) => {
  loading.value = true
  await sendCommentDataService(CommentData).then((res) => {
    resetForm()
    showSuccess({
      title: "موفقیت",
      message: "کامنت شما با موفقیت ارسال شد.",
      autoClose: 4000
    })
  }).finally(() => {
    loading.value = false
  })
}
</script>

<style></style>