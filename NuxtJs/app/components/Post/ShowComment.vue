<template>
  <section aria-labelledby="comments-heading">
    <h3 id="comments-heading" class="mb-6 flex items-center gap-2 text-xl font-extrabold text-ink">
      <span class="font-extrabold text-brand" v-persian-number="commentCount"></span>
      نظر ثبت شده
    </h3>

    <div v-if="comments?.length" role="list" class="flex flex-col gap-4">
      <article
        v-for="comment in comments"
        :key="comment.id ?? comment.name"
        role="listitem"
        class="animate-fade-in rounded-3xl border border-line bg-card p-6 shadow-card transition-colors duration-200 hover:border-brand/30"
      >
        <div class="mb-3 flex items-start justify-between gap-3">
          <div class="flex items-center gap-2.5">
            <div class="flex h-9 w-9 shrink-0 items-center justify-center rounded-full border border-brand bg-brand/10 text-base font-extrabold uppercase text-brand" aria-hidden="true">
              {{ comment.name?.charAt(0) || '؟' }}
            </div>
            <div class="flex flex-wrap items-center gap-1.5">
              <span class="text-[15px] font-bold text-brand">{{ comment.name }}</span>
              <span class="text-sm text-ink-soft">گفته:</span>
            </div>
          </div>

          <time class="shrink-0 whitespace-nowrap text-xs text-ink-faint" v-persian-number="comment.created_at" :datetime="comment.created_at"></time>
        </div>

        <div class="text-[15px] leading-7 text-ink-soft" v-html="comment.message"></div>

        <div v-if="comment.answer" role="note" aria-label="پاسخ مدیر" class="mt-3.5 rounded-2xl border border-line border-e-[3px] border-e-brand bg-card-soft p-3.5">
          <div class="mb-1.5 flex items-center gap-1.5 text-sm font-bold text-brand">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path d="M10 9V5l-7 7 7 7v-4.1c5 0 8.5 1.6 11 5.1-1-5-4-10-11-11z" />
            </svg>
            پاسخ:
          </div>
          <div class="text-sm leading-7 text-ink-soft" v-html="comment.answer"></div>
        </div>
      </article>
    </div>

    <div v-else role="status" aria-live="polite" class="flex flex-col items-center py-12 text-center text-ink-faint">
      <svg width="40" height="40" viewBox="0 0 24 24" fill="currentColor" class="mb-3 opacity-20" aria-hidden="true">
        <path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2z" />
      </svg>
      <p class="text-[15px]">هنوز نظری ثبت نشده. اولین نفر باشید!</p>
    </div>
  </section>
</template>

<script lang="ts" setup>
import type { PropType } from 'vue'
import type { CommentDTO } from '~/models/Post/PostDTO'

defineProps({
  commentCount: { type: Number, default: 0 },
  comments: { type: Object as PropType<CommentDTO[]> }
})
</script>
