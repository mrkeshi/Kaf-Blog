<template>
  <div class="flex flex-col">
    <template v-if="pending">
      <div v-for="i in 5" :key="i" class="border-b border-line-soft py-7 last:border-b-0">
        <skeleton-simple class="mb-3 h-7 w-3/4 rounded-lg" />
        <skeleton-simple class="mb-4 h-4 w-1/2 rounded-md" />
        <skeleton-simple :repeat="3" class="mb-2 h-4 w-full rounded-md" />
        <skeleton-simple class="mt-4 h-9 w-28 rounded-full" />
      </div>
    </template>

    <template v-else>
      <post-card v-for="item in data?.results" :key="item.id" :post="item" />
    </template>

    <div v-if="!pending" class="mb-6 mt-12 flex justify-center">
      <Pagination :current-page="currentPage" :total-pages="totalPages" @change="goToPage" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { getPostListService } from '~/services/Post.Service'
import { useRoute, useRouter } from 'vue-router'
import { generateSeoMeta } from '~/utilities/seo'

const PAGE_SIZE = 8
const route = useRoute()
const router = useRouter()
const nuxt = useNuxtApp()
const currentPage = ref(Number(route.query.page) || 1)
const key = computed(() => `post-list-${currentPage.value}`)

const { data, pending } = await useAsyncData(key, () =>
  getPostListService(currentPage.value),
  { getCachedData: key => nuxt.payload.static?.[key] ?? nuxt.payload.data?.[key] }
)

const totalPages = computed(() =>
  !data.value?.count ? 1 : Math.ceil(data.value.count / PAGE_SIZE)
)

function goToPage(page: number) {
  if (page < 1 || page > totalPages.value) return
  currentPage.value = page
  router.replace({ query: { ...route.query, page: page === 1 ? undefined : page } })
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

watch(route, (newRoute) => {
  const p = Number(newRoute.query.page) || 1
  if (p !== currentPage.value) currentPage.value = p
})

const setting = useMySettingDataStore().siteSettingData

useHead(() => {
  if (!setting) return {}

  const pageSuffix = currentPage.value > 1 ? ` (صفحه ${currentPage.value})` : ''
  const base = `${setting.site_url}${route.path}`
  const canonicalUrl = currentPage.value > 1 ? `${base}?page=${currentPage.value}` : base
  const prevUrl = currentPage.value > 1
    ? (currentPage.value - 1 > 1 ? `${base}?page=${currentPage.value - 1}` : base)
    : null
  const nextUrl = currentPage.value < totalPages.value
    ? `${base}?page=${currentPage.value + 1}`
    : null

  const seo = generateSeoMeta({
    title: `${setting.site_name}${pageSuffix}`,
    description: `${setting.meta_description}${pageSuffix}`,
    image: setting.site_logo || setting.site_icon,
    url: canonicalUrl,
    keywords: setting.meta_keywords?.split(',').map(k => k.trim()) || [],
    author: setting.meta_author,
    type: 'website'
  })

  return {
    ...seo,
    link: [
      { rel: 'canonical', href: canonicalUrl },
      ...(prevUrl ? [{ rel: 'prev', href: prevUrl }] : []),
      ...(nextUrl ? [{ rel: 'next', href: nextUrl }] : []),
    ]
  }
})
</script>
