<template>
  <div class="min-h-screen flex flex-col items-center justify-center px-6 font-mahoor">
    <div class="max-w-3xl text-center w-full">
      <h1 class="text-2xl md:text-4xl font-extrabold tracking-tight mb-4 text-black-500">
        گالری جذاب ما 
      </h1>
      <div class="w-28 h-[3px] mx-auto mb-4  rounded-full bg-blue-500"></div>
      <p class="text-md md:text-lg text-black-300 leading-relaxed max-md:mb-4 mb-6">
        در این قسمت شما میتونید عکس‌های ارسالی توسط خودم و کاربران رو مشاهده کنید.
      </p>
      <div class="flex justify-center">
  <NuxtLink :to="{name:'gallery-send'}"
    class="flex items-center justify-center gap-2 px-6 py-2 rounded-full bg-blue-500 text-white font-semibold text-lg max-md:text-base border-2 border-blue-500
           transition-all duration-300 hover:bg-transparent hover:text-blue-500"
  >
    <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 md:w-7 mb-2 md:h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
      <path stroke-linecap="round" stroke-linejoin="round" d="M4 16v2a2 2 0 002 2h12a2 2 0 002-2v-2M16 12l-4-4m0 0l-4 4m4-4v12" />
    </svg>
    <span class="leading-none">ارسال عکس</span>
  </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { NuxtLink } from '#components';
import { generateSeoMeta } from '~/utilities/seo';

const nuxt = useNuxtApp()

definePageMeta({
  layout: 'simple-layout'
})

// const { data, pending } =await useAsyncData('about-me', () => getAboutMe(), {
//   getCachedData: key => nuxt.payload.static?.[key] ?? nuxt.payload.data?.[key]
// });
const route = useRoute()
const setting = useMySettingDataStore()
watchEffect(() => {
  if (setting.siteSettingData) {
    const seo = generateSeoMeta({
      title: `${setting.siteSettingData.site_name} - گالری من`,
      description: 'در این صفحه گالری و تصاویر ارسالی از من و کاربران رو مشاهده می کنید',
      image: setting.siteSettingData.site_logo || setting.siteSettingData.site_icon,
      url: `${setting.siteSettingData.site_url}${route.fullPath}`,
      keywords: ['گالری آقای کاف', 'گالری ما', `${setting.siteSettingData.site_name}`, 'گالری من'],
      author: setting.siteSettingData.meta_author,
      type: 'about'
    })

    useHead(seo)
  }
})

</script>

<style>

</style>