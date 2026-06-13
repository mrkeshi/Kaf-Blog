<template>
  <div class="flex flex-col">
    <div v-if="!pending && data" class="animate-fade-in mb-2">
      <div dir="ltr" class="mb-3 inline-flex items-center gap-1.5 rounded-full border border-brand/40 bg-brand/10 px-3.5 py-1 text-xs font-bold text-brand">
        <svg width="14" height="14" viewBox="0 0 41 41" fill="currentColor" aria-hidden="true">
          <path d="M34.1666 17.0834V13.6667H27.3333V6.83337H23.9166V13.6667H17.0833V6.83337H13.6666V13.6667H6.83325V17.0834H13.6666V23.9167H6.83325V27.3334H13.6666V34.1667H17.0833V27.3334H23.9166V34.1667H27.3333V27.3334H34.1666V23.9167H27.3333V17.0834H34.1666ZM23.9166 23.9167H17.0833V17.0834H23.9166V23.9167Z" />
        </svg>
        #{{ route.params.slug }}
      </div>
      <h1 class="mb-5 text-2xl font-extrabold text-ink md:text-[28px]">{{ tag?.name || route.params.slug }}</h1>
      <div class="mb-2 h-px bg-line-soft" aria-hidden="true"></div>
    </div>

    <template v-if="pending">
      <div v-for="i in 5" :key="i" class="border-b border-line-soft py-7 last:border-b-0">
        <skeleton-simple class="mb-3 h-7 w-3/4 rounded-lg" />
        <skeleton-simple class="mb-4 h-4 w-1/2 rounded-md" />
        <skeleton-simple :repeat="3" class="mb-2 h-4 w-full rounded-md" />
      </div>
    </template>

    <template v-else>
      <post-card v-for="item in data?.results" :key="item.id" :post="item" />
    </template>

    <div v-if="!pending && (data?.count ?? 0) > PAGE_SIZE" class="mb-4 mt-12 flex justify-center">
      <Pagination :current-page="currentPage" :total-pages="totalPages" @change="goToPage" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { getPostListTagService } from '~/services/Post.Service'
import { useRoute, useRouter } from 'vue-router'
import { generateSeoMeta } from '~/utilities/seo'

const PAGE_SIZE = 8
const route = useRoute()
const router = useRouter()
const nuxt = useNuxtApp()
const currentPage = ref(Number(route.query.page) || 1)
const key = computed(() => `post-list-${currentPage.value}-${route.params.slug}`)

const { data, pending } = await useAsyncData(key, () =>
  getPostListTagService(currentPage.value, route.params.slug as string),
  { getCachedData: key => nuxt.payload.static?.[key] ?? nuxt.payload.data?.[key] }
)

if (!pending.value && !data.value) {
  throw createError({ statusCode: 404, statusMessage: 'Page Not Found', fatal: true })
}

const totalPages = computed(() =>
  !data.value?.count ? 1 : Math.ceil(data.value.count / PAGE_SIZE)
)

const tag = computed(() =>
  data.value?.results[0]?.tags?.find(t => t.slug === route.params.slug)
)

function goToPage(page: number) {
  if (page < 1 || page > totalPages.value) return
  currentPage.value = page
  router.replace({ query: { ...route.query, page: page === 1 ? undefined : page } })
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

watch(route, (r) => {
  const p = Number(r.query.page) || 1
  if (p !== currentPage.value) currentPage.value = p
})

const setting = useMySettingDataStore().siteSettingData

useHead(() => {
  if (!data.value || !setting) return {}

  const pageSuffix = currentPage.value > 1 ? ` (صفحه ${currentPage.value})` : ''
  const base = `${setting.site_url}${route.path}`
  const canonicalUrl = currentPage.value > 1 ? `${base}?page=${currentPage.value}` : base
  const prevUrl = currentPage.value > 1
    ? (currentPage.value - 1 > 1 ? `${base}?page=${currentPage.value - 1}` : base)
    : null
  const nextUrl = currentPage.value < totalPages.value
    ? `${base}?page=${currentPage.value + 1}`
    : null

  return {
    ...generateSeoMeta({
      title: `${setting.site_name} - ${tag.value?.name || route.params.slug}${pageSuffix}`,
      description: `${tag.value?.meta_description || setting.meta_description}${pageSuffix}`,
      image: setting.site_logo || setting.site_icon,
      url: canonicalUrl,
      keywords: tag.value?.name?.split(',').map(k => k.trim())
        || setting.meta_keywords?.split(',').map(k => k.trim()) || [],
      author: setting.meta_author,
      type: 'tag'
    }),
    link: [
      { rel: 'canonical', href: canonicalUrl },
      ...(prevUrl ? [{ rel: 'prev', href: prevUrl }] : []),
      ...(nextUrl ? [{ rel: 'next', href: nextUrl }] : []),
    ]
  }
})
</script>
