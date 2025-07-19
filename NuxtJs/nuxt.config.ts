// https://nuxt.com/docs/api/configuration/nuxt-config

import tailwindcss from "@tailwindcss/vite";

export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  devtools: { enabled: true },
  css: ["@/assets/css/main.css"],
  
  modules: ['nuxt-toastify'],
   toastify: {
     autoClose: 2000,
     position: 'top-right',
     theme: 'auto',
     rtl:true,
    
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