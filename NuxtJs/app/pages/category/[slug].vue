<template>
  <div class="flex flex-col">
    <div v-if="!pending && data" class="animate-fade-in mb-2">
      <div class="mb-3 inline-flex items-center gap-1.5 rounded-full border border-brand/40 bg-brand/10 px-3.5 py-1 text-xs font-bold text-brand">
        <svg width="14" height="14" viewBox="0 0 37 37" fill="currentColor" aria-hidden="true">
          <path d="M18.4999 3.08337L10.0208 16.9584H26.9791L18.4999 3.08337Z" />
          <path d="M26.9792 33.9166C30.8107 33.9166 33.9167 30.8106 33.9167 26.9791C33.9167 23.1477 30.8107 20.0416 26.9792 20.0416C23.1478 20.0416 20.0417 23.1477 20.0417 26.9791C20.0417 30.8106 23.1478 33.9166 26.9792 33.9166Z" />
          <path d="M4.625 20.8125H16.9583V33.1458H4.625V20.8125Z" />
        </svg>
        دسته‌بندی
      </div>
      <h1 class="mb-5 text-2xl font-extrabold text-ink md:text-[28px]">{{ categoryName }}</h1>
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
import { getPostListCategoryService } from '~/services/Post.Service'
import { useRoute, useRouter } from 'vue-router'
import { generateSeoMeta } from '~/utilities/seo'

const PAGE_SIZE = 8
const route = useRoute()
const router = useRouter()
const nuxt = useNuxtApp()
const currentPage = ref(Number(route.query.page) || 1)
const key = computed(() => `category-${currentPage.value}-${route.params.slug}`)

const { data, pending } = await useAsyncData(key, () =>
  getPostListCategoryService(currentPage.value, route.params.slug as string),
  { getCachedData: key => nuxt.payload.static?.[key] ?? nuxt.payload.data?.[key] }
)

if (!pending.value && !data.value) {
  throw createError({ statusCode: 404, statusMessage: 'Page Not Found', fatal: true })
}

const totalPages = computed(() =>
  !data.value?.count ? 1 : Math.ceil(data.value.count / PAGE_SIZE)
)
const categoryName = computed(() => data.value?.results[0]?.category?.name ?? route.params.slug)
const category = computed(() => data.value?.results[0]?.category)

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

  return {
    ...generateSeoMeta({
      title: `${setting.site_name} - ${category.value?.name}${pageSuffix}`,
      description: `${category.value?.meta_description || setting.meta_description}${pageSuffix}`,
      image: setting.site_logo || setting.site_icon,
      url: canonicalUrl,
      keywords: category.value?.name?.split(',').map(k => k.trim())
        || setting.meta_keywords?.split(',').map(k => k.trim()) || [],
      author: setting.meta_author,
      type: 'category'
    }),
    link: [{ rel: 'canonical', href: canonicalUrl }]
  }
})
</script>
