<template>
  <div>
    <div id="loadingOverlay" class="fixed inset-0 z-50 bg-black-100/70 backdrop-blur-md flex flex-col items-center justify-center transition-opacity duration-500 opacity-100">
    <svg class="animate-spin-slow w-24 h-24 text-blue-600 mb-6" viewBox="0 0 100 100" fill="none">
      <circle cx="50" cy="50" r="40" stroke="currentColor" stroke-width="10" stroke-linecap="round" stroke-dasharray="180" stroke-dashoffset="60">
        <animate attributeName="stroke-dashoffset" values="60;0;60" dur="1.5s" repeatCount="indefinite"></animate>
      </circle>
    </svg>
  
    <p class="text-xl max-sm:text-base text-black-300 font-extrabold animate-pulse tracking-wider">
      در حال بارگذاری...
    </p>
  </div>
  </div>
</template>

<script lang="ts" setup>
</script>

<style>

</style>