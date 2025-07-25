<template>
  <div>
         <NuxtLoadingIndicator color="#2b2929" :height="4" :throttle="0" />

   <nuxt-layout>
    <NuxtPage />
   </nuxt-layout>
  </div>
</template>
<script lang="ts" setup>
import { useCustomToastify } from './composable/useCustomToastify';

const {showInfo}=useCustomToastify()
if (process.client && 'serviceWorker' in navigator) {
  navigator.serviceWorker.addEventListener('message', event => {
    if (event.data && event.data.type === 'push') {
     showInfo({
message: `پست با عنوان "${event.data.title}" منتشر شد.`,
      title:"اعلان  "
     })
    }
  });
}
</script>
