<template>
  <div class="articles flex flex-col">

    <div v-if="data && route.query.q" class="mb-6 border-b pb-4">
      <p class="text-lg font-semibold">
        نتیجه جستجو برای
        <span class="text-blue-600">"{{ route.query.q }}"</span> -
        <span class="text-blue-600 text-xl" v-persian-number="data.count"></span>
        پست یافت شد.
      </p>
    </div>

    <skeleton-simple v-if="pending" class="w-full h-44 rounded-2xl mb-8" :repeat="10" />
    
    <template v-else>
      <post-card v-for="item in data?.results" :key="item.id" :post="item" />
    </template>

    <div dir="ltr" class="flex items-center justify-center gap-2 my-12 max-md:mb-4 select-none text-black-400" v-if="data && data?.count > 8">
      <!-- Prev -->
      <button @click="goToPage(currentPage - 1)" :disabled="currentPage <= 1" :class="[
        'cursor-pointer hover:text-blue-600 p-2 rounded',
        currentPage <= 1 ? 'text-gray-400 cursor-not-allowed' : 'text-black'
      ]">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
          <path d="M15 19l-7-7 7-7" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
      </button>

      <!-- Pages -->
      <button v-for="page in totalPages" :key="page" @click="goToPage(page)" :class="[
        'text-black font-bold cursor-pointer hover:text-blue-600 px-3 py-1 rounded',
        currentPage === page ? 'text-blue-600' : ''
      ]" v-persian-number="page"></button>

      <!-- Next -->
      <button @click="goToPage(currentPage + 1)" :disabled="currentPage >= totalPages" :class="[
        'cursor-pointer hover:text-blue-600 p-2 rounded',
        currentPage >= totalPages ? 'text-gray-400 cursor-not-allowed' : 'text-black'
      ]">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
          <path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
      </button>
    </div>

  </div>
</template>


<script setup lang="ts">
const ui = useUIStore()

import { ref, computed, watch } from 'vue'
import { getSearchedPostListServices } from '~/services/Post.Service'
import { useRoute, useRouter } from 'vue-router'
import { generateSeoMeta } from '~/utilities/seo'

const pageSize = 8
const route = useRoute()
const router = useRouter()
const nuxt=useNuxtApp()
const currentPage = ref(Number(route.query.page) || 1)
const key = computed(() => `post-list-${currentPage.value}-${route.query.q}`)

const { data, pending, refresh } =  useAsyncData(key, () => {
   ui.closeSearch()

  return getSearchedPostListServices(route.query.q,currentPage.value)
},{
   getCachedData: key => nuxt.payload.static?.[key] ?? nuxt.payload.data?.[key]
})

const totalPages = computed(() => {
  if (!data.value?.count) return 1
  return Math.ceil(data.value.count / pageSize)
})

function goToPage(page: number) {
  if (page < 1 || page > totalPages.value) return
  currentPage.value = page
}



watch(route, (newRoute) => {
  const pageFromQuery = Number(newRoute.query.page) || 1
  if (pageFromQuery !== currentPage.value) {
    currentPage.value = pageFromQuery
  }
})
const setting=useMySettingDataStore().siteSettingData
watchEffect(() => {
  if (!pending.value && data.value && setting) {
    const keywords = route.query.q
      ? route.query.q.split(',').map(k => k.trim())
      : setting.meta_keywords
        ? setting.meta_keywords.split(',').map(k => k.trim())
        : []

    const seo = generateSeoMeta({
      title: `${setting.site_name} - ${route.query.q || 'جستجو'}`,
      description: route.query.q
        ? `نتیجه جستجو برای "${route.query.q}"`
        : setting.meta_description,
      image: setting.site_logo || setting.site_icon,
      url: `${setting.site_url}${route.fullPath}`,
      keywords,
      author: setting.meta_author,
      type: 'search'
    })

    useHead(seo)
  }
})

</script>


