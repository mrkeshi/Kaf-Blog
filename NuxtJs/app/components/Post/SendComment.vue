<template>
  <section aria-labelledby="send-comment-heading">
    <h3 id="send-comment-heading" class="mb-6 text-xl font-extrabold text-ink">نظر خود را بنویسید</h3>

    <Form
      @submit="sendComment"
      :validation-schema="CommentSchema"
      v-slot="{ meta }"
      class="rounded-3xl border border-line bg-card p-6 shadow-card"
      novalidate
    >
      <div class="grid grid-cols-1 gap-5 sm:grid-cols-2">
        <base-input
          v-model="CommentData.name"
          :disabled="loading"
          type="text"
          name="name"
          placeholder="نام شما"
          label="نام"
        />
        <base-input
          v-model="CommentData.email"
          :disabled="loading"
          type="email"
          name="email"
          placeholder="ایمیل (اختیاری)"
          label="ایمیل"
        />
        <div class="col-span-full">
          <base-textarea
            v-model="CommentData.message"
            :disabled="loading"
            name="message"
            label="پیام"
            placeholder="هرچه دل تنگت می‌خواهد بنویس..."
          />
        </div>
        <div class="col-span-full">
          <BaseCheckbox
            name="privte"
            v-model="CommentData.privte"
            label="نظر به صورت خصوصی ارسال شود."
          />
        </div>
      </div>

      <div class="mt-5">
        <base-button :disabled="loading" type="submit">
          {{ loading ? 'در حال ارسال...' : 'ارسال نظر' }}
        </base-button>
      </div>
    </Form>
  </section>
</template>

<script lang="ts" setup>
import { Form } from 'vee-validate'
import * as Yup from 'yup'
import { useCustomToastify } from '~/composable/useCustomToastify'
import type { CommentDTO } from '~/models/Post/CommentDTO'
import { sendCommentDataService } from '~/services/Post.Service'

const loading = ref(false)

const CommentSchema = Yup.object().shape({
  name: Yup.string().required('وارد کردن نام ضروری است.').min(1, 'حداقل یک کاراکتر وارد کنید.'),
  email: Yup.string().email('ایمیل وارد شده معتبر نیست'),
  message: Yup.string().required('نوشتن پیام الزامی است.').min(5, 'پیام باید حداقل ۵ کاراکتر داشته باشد.'),
})

const { post } = defineProps({ post: { required: true, type: Number } })
const { showSuccess } = useCustomToastify()

const CommentData: CommentDTO = reactive({
  name: '',
  email: '',
  message: '',
  post,
  privte: false
})

const sendComment = async (_: unknown, { resetForm }: any) => {
  loading.value = true
  await sendCommentDataService(CommentData)
    .then(() => {
      resetForm()
      showSuccess({ title: 'موفقیت', message: 'نظر شما با موفقیت ارسال شد.', autoClose: 4000 })
    })
    .finally(() => { loading.value = false })
}
</script>
