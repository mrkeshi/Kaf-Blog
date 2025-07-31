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
      host: process.env.NUXT_PUBLIC_HOST,
      canonicalHost: process.env.NUXT_PUBLIC_HOST,
    },
  pwa: {

        registerType: 'autoUpdate',
        strategies: 'injectManifest', 
        srcDir: '', 
        filename: 'service-worker.js',
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
  runtimeConfig: {
    public: {
      baseURL: process.env.NUXT_PUBLIC_BASE_URL || "http://127.0.0.1:8000/api/",
      vapidKey: process.env.NUXT_PUBLIC_VAPID_KEY || 'BAv9jq1Ff_uckKKEIuOCqVUTXQuTftPfdUILI97PvF5UvdcWsf72tk4N-1SCur4tlSV_9J8Xg_NzWVxOCCQSyq8',
      isProduction: process.env.NUXT_PUBLIC_NODE_ENV === 'production'
    }
  }


  });