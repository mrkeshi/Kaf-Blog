<template>
  <div class="animate-fade-in">
    <div v-if="post?.image" class="mb-8 overflow-hidden rounded-3xl shadow-pop">
      <img
        :src="post.image"
        :alt="post.title"
        loading="eager"
        fetchpriority="high"
        class="block h-auto max-h-[480px] w-full object-cover md:max-h-[520px]"
      />
    </div>

    <h1 class="mb-6 text-center text-2xl font-extrabold leading-relaxed text-ink md:text-[32px]">
      {{ post?.title }}
    </h1>

    <div role="list" aria-label="اطلاعات مقاله" class="mx-auto mb-8 flex max-w-fit flex-wrap items-center justify-center gap-4 rounded-full border border-line bg-card-soft px-6 py-3 text-sm text-ink-faint shadow-soft">
      <div role="listitem" class="flex items-center gap-1.5">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" class="opacity-60" aria-hidden="true">
          <path opacity="0.3" d="M5 8H19V6H5V8Z" />
          <path d="M19 4H18V2H16V4H8V2H6V4H5C3.89 4 3.01 4.9 3.01 6L3 20C3 21.1 3.89 22 5 22H19C20.1 22 21 21.1 21 20V6C21 4.9 20.1 4 19 4ZM19 20H5V10H19V20ZM19 8H5V6H19V8Z" />
        </svg>
        <time v-persian-number="post?.created_at"></time>
      </div>

      <span aria-hidden="true" class="text-line">·</span>

      <NuxtLink :to="{ name: 'category-slug', params: { slug: post.category.slug } }" role="listitem" class="font-bold text-brand transition-opacity duration-200 hover:opacity-75">
        #{{ post?.category.name }}
      </NuxtLink>

      <span aria-hidden="true" class="text-line">·</span>

      <div role="listitem" class="flex items-center gap-1.5" :aria-label="`${post?.views + 1} بازدید`">
        <svg width="14" height="14" viewBox="0 0 16 16" fill="currentColor" class="opacity-60" aria-hidden="true">
          <path d="M12.9866 8.23335C11.94 5.51335 8.21329 5.36668 9.11329 1.41335C9.17996 1.12001 8.86663 0.893346 8.61329 1.04668C6.19329 2.47335 4.45329 5.33335 5.91329 9.08001C6.03329 9.38668 5.67329 9.67335 5.41329 9.47335C4.20663 8.56001 4.07996 7.24668 4.18663 6.30668C4.22663 5.96001 3.77329 5.79335 3.57996 6.08001C3.12663 6.77335 2.66663 7.89335 2.66663 9.58001C2.91996 13.3133 6.07329 14.46 7.20663 14.6067C8.82663 14.8133 10.58 14.5133 11.84 13.36C13.2266 12.0733 13.7333 10.02 12.9866 8.23335Z" />
        </svg>
        <span v-persian-number="post?.views + 1"></span>
        <span>بازدید</span>
      </div>

      <span aria-hidden="true" class="text-line">·</span>

      <div role="listitem" class="flex items-center gap-1.5" :aria-label="`${post?.comment_count} نظر`">
        <svg width="14" height="14" viewBox="0 0 18 18" fill="currentColor" class="opacity-60" aria-hidden="true">
          <path d="M16.4925 1.5H1.5V13.5H13.5L16.5 16.5L16.4925 1.5ZM13.5 10.5H4.5V9H13.5V10.5ZM13.5 8.25H4.5V6.75H13.5V8.25ZM13.5 6H4.5V4.5H13.5V6Z" />
        </svg>
        <span v-persian-number="post?.comment_count"></span>
        <span>نظر</span>
      </div>
    </div>

    <div
      class="max-w-none text-justify text-[17px] leading-8 text-ink-soft
             [&_h1]:mt-9 [&_h1]:mb-3 [&_h1]:text-2xl [&_h1]:font-extrabold [&_h1]:leading-snug [&_h1]:text-ink
             [&_h2]:mt-9 [&_h2]:mb-3 [&_h2]:text-2xl [&_h2]:font-extrabold [&_h2]:leading-snug [&_h2]:text-ink
             [&_h3]:mt-9 [&_h3]:mb-3 [&_h3]:text-xl [&_h3]:font-extrabold [&_h3]:leading-snug [&_h3]:text-ink
             [&_h4]:mt-9 [&_h4]:mb-3 [&_h4]:text-lg [&_h4]:font-extrabold [&_h4]:leading-snug [&_h4]:text-ink
             [&_p]:mb-5
             [&_a]:font-bold [&_a]:text-brand [&_a]:underline [&_a]:decoration-transparent [&_a]:transition-colors [&_a]:duration-200 [&_a:hover]:decoration-brand
             [&_img]:my-6 [&_img]:rounded-2xl [&_img]:max-w-full
             [&_blockquote]:my-6 [&_blockquote]:rounded-e-2xl [&_blockquote]:border-e-[3px] [&_blockquote]:border-brand [&_blockquote]:bg-card-soft [&_blockquote]:px-5 [&_blockquote]:py-4 [&_blockquote]:italic [&_blockquote]:text-ink-soft
             [&_code]:inline-block [&_code]:rounded-md [&_code]:border [&_code]:border-line [&_code]:bg-card-soft [&_code]:px-2 [&_code]:py-0.5 [&_code]:text-sm [&_code]:[direction:ltr]
             [&_pre]:my-6 [&_pre]:overflow-x-auto [&_pre]:rounded-2xl [&_pre]:border [&_pre]:border-line [&_pre]:bg-base [&_pre]:p-5 [&_pre]:[direction:ltr]
             [&_pre_code]:border-0 [&_pre_code]:bg-transparent [&_pre_code]:p-0
             [&_ul]:mb-5 [&_ul]:ps-6 [&_ol]:mb-5 [&_ol]:ps-6 [&_li]:mb-2
             [&_table]:my-6 [&_table]:w-full [&_table]:overflow-hidden [&_table]:rounded-2xl [&_table]:border [&_table]:border-line [&_table]:border-collapse
             [&_th]:border-b [&_th]:border-line [&_th]:bg-card-soft [&_th]:px-4 [&_th]:py-3 [&_th]:text-start [&_th]:font-extrabold
             [&_td]:border-b [&_td]:border-line-soft [&_td]:px-4 [&_td]:py-3 [&_tr:last-child_td]:border-b-0
             [&_hr]:my-9 [&_hr]:border-line"
      v-html="post?.content"
      role="article"
    ></div>

    <div v-if="post?.tags?.length" aria-label="برچسب‌ها" class="mt-9 flex flex-wrap items-center gap-3">
      <span class="text-sm font-bold text-ink-soft">برچسب‌ها:</span>
      <ul role="list" class="flex flex-wrap gap-2">
        <li v-for="item in post.tags" :key="item.slug" role="listitem">
          <NuxtLink
            :to="{ name: 'tag-slug', params: { slug: item.slug } }"
            class="inline-flex items-center rounded-full border border-line bg-card-soft px-3 py-1 text-xs font-bold text-ink-soft transition-all duration-200 hover:border-brand/40 hover:bg-brand/10 hover:text-brand"
          >
            {{ item.name }}
          </NuxtLink>
        </li>
      </ul>
    </div>

    <div class="my-8 h-px bg-line-soft" aria-hidden="true"></div>

    <div role="group" aria-label="عملیات مقاله" class="flex flex-wrap items-center justify-between gap-4">
      <button
        @click="toggleLike"
        :aria-pressed="liked"
        :aria-label="liked ? 'لغو لایک' : 'لایک کردن'"
        :class="[
          'inline-flex items-center gap-2 rounded-full border px-5 py-2.5 text-sm font-bold transition-all duration-200',
          liked ? 'border-brand bg-brand/10 text-brand' : 'border-line bg-card-soft text-ink-soft hover:border-brand/40 hover:bg-brand/10 hover:text-brand'
        ]"
      >
        <svg
          width="20" height="20" viewBox="0 0 28 28"
          :fill="liked ? 'currentColor' : 'none'"
          stroke="currentColor"
          stroke-width="1.5"
          class="transition-transform duration-300"
          :class="liked ? 'scale-110' : ''"
          aria-hidden="true"
        >
          <path d="M14.373 3.02051C17.377-0.33962 22.2217-0.339604 25.2256 3.02051C28.2582 6.41322 28.2585 11.9346 25.2256 15.3271L14.5938 27.2188C14.2587 27.5935 13.7413 27.5935 13.4062 27.2188L2.77441 15.3271C-0.258493 11.9346-0.258263 6.41324 2.77441 3.02051C5.77835-0.33962 10.623-0.339604 13.627 3.02051L14 3.4375L14.373 3.02051Z" />
        </svg>
        <span><span v-persian-number="post?.like_count"></span> لایک</span>
      </button>

      <button
        @click="sharePost"
        :disabled="isSharing"
        aria-label="اشتراک‌گذاری"
        class="inline-flex items-center gap-2 rounded-full border border-line bg-card-soft px-5 py-2.5 text-sm font-bold text-ink-soft transition-all duration-200 hover:border-brand/40 hover:bg-brand/10 hover:text-brand disabled:opacity-50"
      >
        <svg width="18" height="18" viewBox="0 0 28 28" fill="currentColor" aria-hidden="true">
          <path d="M21 18.76C20.1133 18.76 19.32 19.11 18.7133 19.6584L10.395 14.8167C10.4533 14.5484 10.5 14.28 10.5 14C10.5 13.72 10.4533 13.4517 10.395 13.1834L18.62 8.38837C19.25 8.97171 20.0783 9.33337 21 9.33337C22.9367 9.33337 24.5 7.77004 24.5 5.83337C24.5 3.89671 22.9367 2.33337 21 2.33337C19.0633 2.33337 17.5 3.89671 17.5 5.83337C17.5 6.11337 17.5467 6.38171 17.605 6.65004L9.38 11.445C8.75 10.8617 7.92167 10.5 7 10.5C5.06333 10.5 3.5 12.0634 3.5 14C3.5 15.9367 5.06333 17.5 7 17.5C7.92167 17.5 8.75 17.1384 9.38 16.555L17.6867 21.4084C17.6283 21.6534 17.5933 21.91 17.5933 22.1667C17.5933 24.045 19.1217 25.5734 21 25.5734C22.8783 25.5734 24.4067 24.045 24.4067 22.1667C24.4067 20.2884 22.8783 18.76 21 18.76Z" />
        </svg>
        <span>اشتراک‌گذاری</span>
      </button>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { useCustomToastify } from '~/composable/useCustomToastify'
import type { PostDetailDTO } from '~/models/Post/PostDTO'
import { checkingLikePostService, toggleLikeService } from '~/services/Post.Service'

const { post } = defineProps<{ post: PostDetailDTO }>()
const { showSuccess } = useCustomToastify()

const liked = ref(false)
const isSharing = ref(false)

onMounted(async () => {
  const data = await checkingLikePostService(post.id)
  liked.value = data.liked
})

const toggleLike = () => {
  toggleLikeService(post.id).then((res) => {
    if (res.code === 1) { liked.value = true; post.like_count++ }
    if (res.code === 2) { liked.value = false; post.like_count-- }
  })
}

function sharePost() {
  if (isSharing.value) return
  isSharing.value = true

  const title = post?.title || 'مشاهده مطلب'
  const url = window.location.href
  const text = `این مطلب رو ببین: ${title}`

  if (navigator.share) {
    navigator.share({ title, text, url })
      .catch(() => {})
      .finally(() => { isSharing.value = false })
  } else {
    copyToClipboard(url)
    showSuccess({ title: 'موفقیت', message: 'لینک مطلب در کلیپ‌بورد کپی شد.', autoClose: 4000 })
    isSharing.value = false
  }
}

function copyToClipboard(text: string) {
  if (navigator.clipboard) {
    navigator.clipboard.writeText(text).catch(() => legacyCopy(text))
  } else {
    legacyCopy(text)
  }
}

function legacyCopy(text: string) {
  const ta = document.createElement('textarea')
  ta.value = text
  ta.readOnly = true
  ta.style.position = 'absolute'
  ta.style.left = '-9999px'
  document.body.appendChild(ta)
  ta.select()
  document.execCommand('copy')
  document.body.removeChild(ta)
}
</script>
