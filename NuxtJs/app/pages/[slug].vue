<template>
  <div class="mx-auto max-w-3xl">
    <template v-if="pending || !data">
      <skeleton-simple class="mb-8 h-[420px] w-full rounded-3xl" />
      <skeleton-simple class="mx-auto mb-4 h-10 w-3/4 rounded-xl" />
      <skeleton-simple class="mx-auto mb-8 h-12 w-full max-w-md rounded-full" />
      <skeleton-simple :repeat="12" class="mb-3 h-5 w-full rounded-md" />
    </template>

    <article v-else>
      <PostSingle :post="data" />

      <div class="my-12 h-px bg-line-soft" aria-hidden="true"></div>

      <div id="comments" class="pb-8">
        <PostShowComment :comments="data.comments" :commentCount="data.comment_count" />
        <div class="my-10 h-px bg-line-soft" aria-hidden="true"></div>
        <PostSendComment v-if="data.id" :post="data.id" />
      </div>
    </article>
  </div>
</template>

<script lang="ts" setup>
import { getSinglePostService } from '~/services/Post.Service'
import { generateSeoMeta } from '~/utilities/seo'

const route = useRoute()
const { data, pending } = await useAsyncData(() =>
  getSinglePostService(route.params.slug as string)
)

if (!pending.value && !data.value) {
  throw createError({ statusCode: 404, statusMessage: 'Page Not Found', fatal: true })
}

const setting = useMySettingDataStore().siteSettingData

useHead(() => {
  if (!data.value || !setting) return {}

  return generateSeoMeta({
    title: `${setting.site_name} - ${data.value.title}`,
    description: data.value.seo_description || setting.meta_description,
    image: data.value.image || setting.site_logo || setting.site_icon,
    url: `${setting.site_url}${route.fullPath}`,
    keywords: data.value.seo_keywords?.split(',').map(k => k.trim())
      || setting.meta_keywords?.split(',').map(k => k.trim())
      || [],
    author: data.value.author || setting.meta_author,
    type: 'article'
  })
})
</script>
