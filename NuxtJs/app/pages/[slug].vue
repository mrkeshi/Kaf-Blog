<template>
  <div class="articles flex flex-col" v-if="!pending && data">
    <article class="mt-2" >
      <PostSingle v-if="data?.id" :post="data"></PostSingle>
      <div class="h-0.5 w-full bg-black-100 my-8 max-md:my-4"></div>
      <div class="comments flex flex-col">
        <PostShowComment :comments="data?.comments" :commentCount="data?.comment_count"></PostShowComment>
        <PostSendComment v-if="data?.id" :post="data?.id" class="mb-8"></PostSendComment>
      </div>
    </article>


  </div>
  <div v-else>
          <skeleton-simple :repeat="1" class="w-full h-96 rounded-3xl mb-6" />
          <skeleton-simple :repeat="1" class="w-full h-20 rounded-lg mb-6 " />
          <skeleton-simple :repeat="10" class="w-full h-8 rounded-lg mb-2 " />

  </div>
</template>

<script lang="ts" setup>


import { getSinglePostService } from '~/services/Post.Service';
import { generateSeoMeta } from '~/utilities/seo';

const route=useRoute()
const { data , pending } = await useAsyncData(() =>
  getSinglePostService(route.params.slug as string)
)



watchEffect(() => {
  if (!pending.value && !data.value) {
    throw createError({ statusCode: 404, statusMessage: 'Page Not Found', fatal: true })
  }
})
const setting=useMySettingDataStore().siteSettingData

watchEffect(() => {
  if (!pending.value && data.value && setting) {
    const seo = generateSeoMeta({
       title: `${setting.site_name} - ${data.value.title}`,   
      description: data.value.seo_description || setting.meta_description,
      image: data.value.image || setting.site_logo || setting.site_icon,
      url: `${setting.site_url}${route.fullPath}`,
      keywords:data.value.seo_keywords?.split(',').map(k => k.trim()) || setting.meta_keywords?.split(',').map(k => k.trim()) || [],
      author: data.value.author || setting.meta_author,
      type: 'article'
    }) 
    useHead(seo)
  }
})


</script>

<style></style>