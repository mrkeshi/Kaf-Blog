<template>
  <div>
         <NuxtLoadingIndicator color="#2b2929" :height="4" :throttle="0" />

   <nuxt-layout>
    <NuxtPage />
   </nuxt-layout>
  </div>
</template>
<script lang="ts" setup>
useHead({
  link: [
    {
      rel: 'manifest',
      href: '/manifest.webmanifest'
    }
  ]
});
</script>