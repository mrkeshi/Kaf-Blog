<template>
  <div class="flex flex-col">
    <div v-if="!pending && route.query.q" class="mb-6">
      <div role="status" aria-live="polite" class="inline-flex items-center gap-2.5 rounded-full border border-line bg-card-soft px-5 py-2.5 text-sm text-ink-soft">
        <svg width="18" height="18" viewBox="0 0 23 23" fill="currentColor" class="opacity-60" aria-hidden="true">
          <path d="M16.375 14.5H15.3875L15.0375 14.1625C16.2625 12.7375 17 10.8875 17 8.875C17 4.3875 13.3625.75 8.875.75C4.3875.75.75 4.3875.75 8.875C.75 13.3625 4.3875 17 8.875 17C10.8875 17 12.7375 16.2625 14.1625 15.0375L14.5 15.3875V16.375L20.75 22.6125L22.6125 20.75L16.375 14.5ZM8.875 14.5C5.7625 14.5 3.25 11.9875 3.25 8.875C3.25 5.7625 5.7625 3.25 8.875 3.25C11.9875 3.25 14.5 5.7625 14.5 8.875C14.5 11.9875 11.9875 14.5 8.875 14.5Z" />
        </svg>
        <span>
          نتایج جستجو برای
          <strong class="font-extrabold text-brand">«{{ route.query.q }}»</strong>
          —
          <span v-persian-number="data?.count ?? 0"></span>
          مطلب یافت شد
        </span>
      </div>
    </div>

    <template v-if="pending">
      <div v-for="i in 5" :key="i" class="border-b border-line-soft py-7 last:border-b-0">
        <skeleton-simple class="mb-3 h-7 w-3/4 rounded-lg" />
        <skeleton-simple class="mb-4 h-4 w-1/2 rounded-md" />
        <skeleton-simple :repeat="3" class="mb-2 h-4 w-full rounded-md" />
      </div>
    </template>

    <template v-else-if="data?.results?.length">
      <post-card v-for="item in data.results" :key="item.id" :post="item" />
    </template>

    <div v-else-if="!pending" role="status" aria-live="polite" class="flex flex-col items-center gap-3 px-6 py-16 text-center">
      <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor" class="text-ink-faint" aria-hidden="true">
        <path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0016 9.5 6.5 6.5 0 109.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z" />
      </svg>
      <h2 class="text-xl font-extrabold text-ink">نتیجه‌ای یافت نشد</h2>
      <p class="max-w-sm text-[15px] text-ink-soft">برای «{{ route.query.q }}» نتیجه‌ای موجود نیست. کلمه دیگری جستجو کنید.</p>
      <NuxtLink :to="{ name: 'index' }" class="mt-2 inline-flex items-center justify-center rounded-full border border-line px-6 py-3 text-[15px] font-bold text-ink transition-all duration-300 hover:border-ink-faint hover:bg-card-soft">
        بازگشت به خانه
      </NuxtLink>
    </div>

    <div v-if="!pending && (data?.count ?? 0) > PAGE_SIZE" class="mb-4 mt-12 flex justify-center">
      <Pagination :current-page="currentPage" :total-pages="totalPages" @change="goToPage" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { getSearchedPostListServices } from '~/services/Post.Service'
import { useRoute, useRouter } from 'vue-router'
import { generateSeoMeta } from '~/utilities/seo'

const PAGE_SIZE = 8
const route = useRoute()
const router = useRouter()
const nuxt = useNuxtApp()
const ui = useUIStore()
const currentPage = ref(Number(route.query.page) || 1)
const key = computed(() => `search-${currentPage.value}-${route.query.q}`)

const { data, pending } = await useAsyncData(key, () => {
  ui.closeSearch()
  return getSearchedPostListServices(route.query.q, currentPage.value)
}, { getCachedData: key => nuxt.payload.static?.[key] ?? nuxt.payload.data?.[key] })

const totalPages = computed(() =>
  !data.value?.count ? 1 : Math.ceil(data.value.count / PAGE_SIZE)
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
  if (!setting) return {}

  const pageSuffix = currentPage.value > 1 ? ` (صفحه ${currentPage.value})` : ''
  const base = `${setting.site_url}${route.path}`
  const q = route.query.q ? `?q=${encodeURIComponent(String(route.query.q))}` : ''
  const canonicalUrl = currentPage.value > 1
    ? `${base}${q}${q ? '&' : '?'}page=${currentPage.value}`
    : `${base}${q}`

  return {
    ...generateSeoMeta({
      title: `${setting.site_name} - ${route.query.q || 'جستجو'}${pageSuffix}`,
      description: route.query.q ? `نتیجه جستجو برای "${route.query.q}"` : setting.meta_description,
      image: setting.site_logo || setting.site_icon,
      url: canonicalUrl,
      keywords: route.query.q
        ? String(route.query.q).split(',').map(k => k.trim())
        : setting.meta_keywords?.split(',').map(k => k.trim()) || [],
      author: setting.meta_author,
      type: 'search'
    }),
    link: [{ rel: 'canonical', href: canonicalUrl }]
  }
})
</script>
