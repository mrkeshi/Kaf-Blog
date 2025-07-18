<template>

  <div>

    <Loading v-if="pending"></Loading>
    <div v-else class="container mx-auto mt-12 max-md:mt-6  px-6 flex flex-col lg:flex-row gap-36 max-xl:gap-12 max-2xl:gap-24  max-lg:gap-6  ">
    <section class="w-full text-center max-w-3xl mx-auto px-2">
        <h2 class="text-3xl sm:text-4xl font-extrabold text-black-500 border-b-4 border-black-200 inline-block pb-2 mb-10">
       
          {{ data.title }}
        </h2>
        <blockquote v-html="data.description" class="relative text-justify text-black-300 leading-loose text-base sm:text-lg font-normal italic pr-6 border-r-4 border-black-200">
 
        </blockquote>
      
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
import { useAsyncData } from '#app';
definePageMeta({
  layout:'simple-layout'
})
const nuxtApp = useNuxtApp();


const title=ref<String>("")
const description=ref<String>("")

const { data, error, pending } =useAsyncData('abouteme',  () => {

  return getAboutMe();
}, );

console.log(error.value)
  if (data.value) {
    console.log("🎯 دریافت شد:", data.value);
  } else {
    console.log("⏳ در انتظار داده...");
  }

</script>

<style>

</style>