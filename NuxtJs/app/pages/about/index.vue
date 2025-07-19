<template>

  <div>

    <div class="container mx-auto mt-12 max-md:mt-6  px-6 flex flex-col lg:flex-row gap-36 max-xl:gap-12 max-2xl:gap-24  max-lg:gap-6  ">
    <section class="w-full text-center max-w-3xl mx-auto px-2">
        <h2 v-if="!pending" class="text-3xl sm:text-4xl font-extrabold text-black-500 border-b-4 border-black-200 inline-block pb-2 mt-5 mb-10">
       
       {{ data.title }}
        </h2>

        <skeleton-simple v-else class="w-full h-12 rounded-2xl mb-8"  />

        <blockquote v-if="!pending" v-html="data.description" class="relative text-justify text-black-300 leading-loose text-base sm:text-lg font-normal italic pr-6 border-r-4 border-black-200">
 
        </blockquote>
      <skeleton-simple v-else  :repeat="15" class="w-full h-6 rounded-lg " />
        <div class="my-12">
          <a href="#" class="inline-block px-6 py-3 text-base font-bold text-white bg-black-400 border border-black-400 rounded-full transition-all duration-300 hover:bg-black-150 hover:text-black-400">
            تماس با من
          </a>
        </div>
      </section>
      
      

    </div> 
  </div>

</template>

<script lang="ts" setup>
import { getAboutMe } from '~/services/About.Service';

const nuxt=useNuxtApp()

definePageMeta({
  layout:'simple-layout'
})

const {data,pending} = useAsyncData('about-me',() => getAboutMe(),{
  getCachedData: key => nuxt.payload.static?.[key] ?? nuxt.payload.data?.[key]
});

</script>

<style>
.ali{
  font-family: Mahoor;
}
</style>