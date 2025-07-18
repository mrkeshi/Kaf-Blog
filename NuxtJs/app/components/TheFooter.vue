<template>
  <div>
      <footer class="w-full bg-black-400">
    <div class="container mx-auto flex justify-between max-md:text-xs flex-wrap px-2 p-8 max-sm:p-6 max-md:justify-center max-md:flex-col-reverse">
      <p class="text-base max-md:mx-auto text-white max-md:mt-3">© اینا واژه‌ نیستن؛ تکه‌های دلمونه. بردنش آزاده، فراموشیِ اسممون نه.</p>
      <ul class="flex max-md:mx-auto">
        <li><NuxtLink :to="{name:'index'}" class="text-base max-md:text-sm-2 text-white hover:text-blue-600">خانه</NuxtLink></li>
        <li class="mx-2 text-base text-blue-600">|</li>
        <li><NuxtLink class="text-base max-md:text-sm-2 text-white hover:text-blue-600">تماس بامن</NuxtLink></li>
        <li class="mx-2 text-base text-blue-600">|</li>
        <li><NuxtLink :to="{name:'about'}" class="text-base max-md:text-sm-2 text-white hover:text-blue-600">درباره من</NuxtLink></li>
      </ul>
    </div>
  </footer>
  </div>
</template>

<script lang="ts" setup>

</script>

<style>

</style>