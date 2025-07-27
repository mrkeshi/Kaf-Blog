// https://nuxt.com/docs/api/configuration/nuxt-config

import tailwindcss from "@tailwindcss/vite";

export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  devtools: { enabled: true },
  css: ["@/assets/css/main.css"],
  
  modules: [
   'nuxt-toastify',
   "@pinia/nuxt",
   '@vite-pwa/nuxt',
   'nuxt-schema-org'
  ],
   toastify: {
     autoClose: 2000,
     position: 'top-right',
     theme: 'auto',
     rtl:true,
    
   },

  schemaOrg: {
    host: 'https://penvis.ir',
    canonicalHost: 'https://penvis.ir',
  },
 pwa: {
    registerType: 'autoUpdate',
    manifest: {
      name: 'کاف بیگانه',
      short_name: 'کاف بیگانه ',
      description: 'نوشته های یک کافه بیگانه',
      theme_color: '#edecea',
      background_color: '#edecea',
      display: 'standalone',
      start_url: '/',
      icons: [
        {
          src: 'images/l192.png',
          sizes: '192x192',
          type: 'image/png',
        },
        {
          src: 'images/l512.png',
          sizes: '512x512',
          type: 'image/png',
        },
      ],
    },
    workbox: {

    },
  },

  vite: {
    plugins: [tailwindcss()],
  },
  runtimeConfig:{
    public:{
      baseURL:process.env.NUXT_BASE_URL
    }
  }

});