<template>
  <article class="animate-fade-in border-b border-line-soft py-7 last:border-b-0" :aria-labelledby="`post-title-${post.id}`">
    <NuxtLink
      :to="{ name: 'slug', params: { slug: post.slug } }"
      :id="`post-title-${post.id}`"
      class="block text-xl font-extrabold leading-snug text-ink transition-colors duration-200 hover:text-brand md:text-[22px]"
    >
      {{ post.title }}
    </NuxtLink>

    <div role="list" class="mt-2.5 flex flex-wrap items-center gap-3 text-xs text-ink-faint">
      <div role="listitem" class="flex items-center gap-1.5">
        <!-- Calendar icon – teal -->
        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" class="text-teal" aria-hidden="true">
          <path opacity="0.3" d="M5 8H19V6H5V8Z" />
          <path d="M19 4H18V2H16V4H8V2H6V4H5C3.89 4 3.01 4.9 3.01 6L3 20C3 21.1 3.89 22 5 22H19C20.1 22 21 21.1 21 20V6C21 4.9 20.1 4 19 4ZM19 20H5V10H19V20ZM19 8H5V6H19V8Z" />
        </svg>
        <time v-persian-number="post.created_at"></time>
      </div>

      <span aria-hidden="true" class="text-line">·</span>

      <NuxtLink
        :to="{ name: 'category-slug', params: { slug: post.category.slug } }"
        role="listitem"
        class="font-bold text-brand transition-opacity duration-200 hover:opacity-75"
      >
        <span aria-hidden="true">#</span>{{ post.category.name }}
      </NuxtLink>

      <span aria-hidden="true" class="text-line">·</span>

      <div role="listitem" class="flex items-center gap-1.5" :aria-label="`${post.views} بازدید`">
        <!-- Flame icon – rose -->
        <svg width="14" height="14" viewBox="0 0 16 16" fill="currentColor" class="text-rose" aria-hidden="true">
          <path d="M12.9866 8.23335C11.94 5.51335 8.21329 5.36668 9.11329 1.41335C9.17996 1.12001 8.86663 0.893346 8.61329 1.04668C6.19329 2.47335 4.45329 5.33335 5.91329 9.08001C6.03329 9.38668 5.67329 9.67335 5.41329 9.47335C4.20663 8.56001 4.07996 7.24668 4.18663 6.30668C4.22663 5.96001 3.77329 5.79335 3.57996 6.08001C3.12663 6.77335 2.66663 7.89335 2.66663 9.58001C2.91996 13.3133 6.07329 14.46 7.20663 14.6067C8.82663 14.8133 10.58 14.5133 11.84 13.36C13.2266 12.0733 13.7333 10.02 12.9866 8.23335Z" />
        </svg>
        <span v-persian-number="post.views"></span>
        <span>بازدید</span>
      </div>

      <span aria-hidden="true" class="text-line">·</span>

      <div role="listitem" class="flex items-center gap-1.5" :aria-label="`${post.comment_count} نظر`">
        <!-- Chat icon – ok/green -->
        <svg width="14" height="14" viewBox="0 0 18 18" fill="currentColor" class="text-ok" aria-hidden="true">
          <path d="M16.4925 1.5H1.5V13.5H13.5L16.5 16.5L16.4925 1.5ZM13.5 10.5H4.5V9H13.5V10.5ZM13.5 8.25H4.5V6.75H13.5V8.25ZM13.5 6H4.5V4.5H13.5V6Z" />
        </svg>
        <span v-persian-number="post.comment_count"></span>
        <span>نظر</span>
      </div>

      <span aria-hidden="true" class="text-line">·</span>

      <!-- Reading time – amber -->
      <div role="listitem" class="flex items-center gap-1.5 text-amber" :aria-label="`${readingTime} دقیقه مطالعه`">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67V7z"/>
        </svg>
        <span v-persian-number="readingTime"></span>
        <span>دقیقه</span>
      </div>
    </div>

    <p class="my-4 text-justify text-[15px] leading-8 text-ink-soft">{{ truncatedContent }}</p>

    <div class="flex justify-end">
      <NuxtLink
        :to="{ name: 'slug', params: { slug: post.slug } }"
        :aria-label="`ادامه مطلب: ${post.title}`"
        class="group inline-flex items-center gap-1.5 rounded-full border border-brand/40 px-4 py-1.5 text-sm font-bold text-brand transition-all duration-300 hover:bg-brand hover:text-white hover:shadow-glow"
      >
        <span>ادامه مطلب</span>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" class="transition-transform duration-300 group-hover:-translate-x-1" aria-hidden="true">
          <path d="M19 12H5M12 5l-7 7 7 7" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
      </NuxtLink>
    </div>
  </article>
</template>

<script lang="ts" setup>
import { computed } from 'vue'
import type { PostListDTO } from '~/models/Post/PostDTO'
import decodeHtml from '~/utilities/decodeHtml'

const props = defineProps<{ post: PostListDTO }>()

const truncatedContent = computed(() => {
  if (!props.post.content) return ''
  const maxLength = 400
  const noTags = props.post.content.replace(/<[^>]+>/g, '')
  const plainText = decodeHtml(noTags)
  return plainText.length <= maxLength ? plainText : plainText.slice(0, maxLength) + '…'
})

// Task 5: estimate reading time from post content
const WORDS_PER_MINUTE = 200
const readingTime = computed(() => {
  if (!props.post.content) return 1
  const text = props.post.content.replace(/<[^>]+>/g, ' ')
  const words = text.trim().split(/\s+/).filter(Boolean).length
  return Math.max(1, Math.ceil(words / WORDS_PER_MINUTE))
})
</script>
