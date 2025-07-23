<template>
  <div class="articles flex flex-col">
    <skeleton-simple v-if="pending || !data" class="w-full h-44 rounded-2xl mb-8" :repeat="10" />
    <template v-else>
      <article class="mt-2">
          <h2 class="text-2xl text-black-400 font-black max-md:text-[20px] mb-4">{{ data?.results[0]?.category.name }}</h2>
          <div class="w-full h-[1px] bg-black-100 mt-3 rounded-2xl"></div>
          <div class="BodyArticle my-4">
         
          </div>
        </article>
      <post-card v-for="item in data?.results" :key="item.id" :post="item"></post-card>
    </template>

    <div  dir="ltr" class="flex items-center justify-center gap-2 my-12 max-md:mb-4 select-none text-black-400" 
      v-if="data && data?.count > 8">
      <!-- Previous Button -->
      <button @click="goToPage(currentPage - 1)" :disabled="currentPage <= 1" :class="[
        'cursor-pointer hover:text-blue-600 p-2 rounded',
        currentPage <= 1 ? 'text-gray-400 cursor-not-allowed' : 'text-black'
      ]">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
          <path d="M15 19l-7-7 7-7" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
      </button>

      <button v-for="page in totalPages" :key="page" @click="goToPage(page)" :class="[
        'text-black font-bold cursor-pointer hover:text-blue-600 px-3 py-1 rounded',
        currentPage === page ? 'text-blue-600  ' : ''
      ]" v-persian-number="page"></button>

      <!-- Next Button -->
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
import { ref, computed, watch } from 'vue'
import { getPostListCategoryService } from '~/services/Post.Service'
import { useRoute, useRouter } from 'vue-router'

const pageSize = 8
const route = useRoute()
const router = useRouter()
const nuxt = useNuxtApp()
const currentPage = ref(Number(route.query.page) || 1)
const key = computed(() => `post-list-${currentPage.value}-${route.params.slug}`)

const { data, pending, refresh,error } = useAsyncData(key, () => {
  return getPostListCategoryService(currentPage.value, route.params.slug as string)
}, {
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

watchEffect(() => {
  if (!pending.value && !data.value) {
    throw createError({ statusCode: 404, statusMessage: 'Page Not Found', fatal: true })
  }
})
</script>
