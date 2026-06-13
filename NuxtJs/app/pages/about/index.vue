<template>
  <div class="mx-auto max-w-3xl">
    <template v-if="pending || !data">
      <skeleton-simple class="mx-auto mb-10 h-10 w-64 rounded-xl" />
      <skeleton-simple :repeat="18" class="mb-3 h-5 w-full rounded-md" />
      <skeleton-simple class="mx-auto mt-10 h-12 w-40 rounded-full" />
    </template>

    <article v-else class="animate-fade-in relative overflow-hidden rounded-4xl border border-line bg-card p-8 text-center shadow-card md:p-14">
      <div class="pointer-events-none absolute -top-16 left-1/2 h-72 w-72 -translate-x-1/2 rounded-full bg-brand/15 blur-3xl" aria-hidden="true"></div>

      <div class="relative z-10">
        <div class="mx-auto mb-5 flex h-16 w-16 items-center justify-center rounded-full border border-brand bg-brand/10 text-brand">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
          </svg>
        </div>

        <h1 class="mb-6 text-2xl font-extrabold leading-relaxed text-ink md:text-3xl">{{ data.title }}</h1>

        <div class="mx-auto mb-8 flex max-w-[200px] items-center gap-3" aria-hidden="true">
          <div class="h-px flex-1 bg-gradient-to-l from-transparent to-line"></div>
          <div class="h-1.5 w-1.5 shrink-0 rounded-full bg-brand shadow-[0_0_8px_var(--color-brand)]"></div>
          <div class="h-px flex-1 bg-gradient-to-r from-transparent to-line"></div>
        </div>

        <div
          class="mb-10 text-justify text-[16px] leading-8 text-ink-soft
                 [&_p]:mb-4 [&_a]:font-bold [&_a]:text-brand [&_a]:underline [&_a]:decoration-transparent [&_a:hover]:decoration-brand
                 [&_strong]:text-ink [&_h2]:mb-3 [&_h2]:mt-7 [&_h2]:text-xl [&_h2]:font-extrabold [&_h2]:text-ink
                 [&_ul]:mb-4 [&_ul]:ps-6 [&_li]:mb-2"
          v-html="data.description"
        ></div>

        <div class="flex flex-wrap items-center justify-center gap-3.5">
          <NuxtLink :to="{ name: 'contact' }" class="inline-flex items-center justify-center gap-2 rounded-full bg-gradient-to-tr from-brand-strong to-brand px-8 py-3.5 text-base font-bold text-white shadow-glow transition-all duration-300 hover:-translate-y-0.5 hover:shadow-glow-lg">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" />
            </svg>
            تماس با من
          </NuxtLink>
          <NuxtLink :to="{ name: 'index' }" class="inline-flex items-center justify-center rounded-full border border-line px-8 py-3.5 text-base font-bold text-ink transition-all duration-300 hover:border-ink-faint hover:bg-card-soft">
            مطالب وبلاگ
          </NuxtLink>
        </div>
      </div>
    </article>
  </div>
</template>

<script lang="ts" setup>
import { getAboutMe } from '~/services/About.Service'
import { generateSeoMeta } from '~/utilities/seo'

definePageMeta({ layout: 'simple-layout' })

const nuxt = useNuxtApp()
const { data, pending } = await useAsyncData('about-me', () => getAboutMe(), {
  getCachedData: key => nuxt.payload.static?.[key] ?? nuxt.payload.data?.[key]
})

const route = useRoute()
const setting = useMySettingDataStore().siteSettingData

useHead(() => {
  if (!setting) return {}

  return generateSeoMeta({
    title: `${setting.site_name} - درباره من`,
    description: 'در این صفحه با من و اهدافم آشنا شوید',
    image: setting.site_logo || setting.site_icon,
    url: `${setting.site_url}${route.fullPath}`,
    keywords: ['درباره ما', 'درباره من', setting.site_name, 'معرفی'],
    author: setting.meta_author,
    type: 'about'
  })
})
</script>
