<template>
  <div>
    <NuxtLoadingIndicator color="#7c6bff" :height="3" :throttle="0" />
    <nuxt-layout>
      <NuxtPage />
    </nuxt-layout>
  </div>
</template>

<script lang="ts" setup>
import { useCustomToastify } from './composable/useCustomToastify'

const { showInfo } = useCustomToastify()

useHead({
  htmlAttrs: { lang: 'fa', dir: 'rtl' }
})

if (process.client) {
  const saved = localStorage.getItem('theme') ?? 'dark'
  document.documentElement.setAttribute('data-theme', saved)
}

if (process.client && 'serviceWorker' in navigator) {
  navigator.serviceWorker.addEventListener('message', event => {
    if (event.data?.type === 'push') {
      showInfo({
        message: `پست با عنوان "${event.data.title}" منتشر شد.`,
        title: 'اعلان'
      })
    }
  })
}
</script>
