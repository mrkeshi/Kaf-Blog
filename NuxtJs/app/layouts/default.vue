<template>
  <div class="flex min-h-dvh flex-col bg-base text-ink">
    <TheHeader
      :title="store.siteSettingData?.site_name"
      :description="store.siteSettingData?.meta_description"
      :count="store.siteSettingData?.count"
      :icon="store.siteSettingData?.site_icon"
    />

    <div class="mx-auto flex w-full max-w-[1440px] flex-1 flex-col gap-10 px-4 py-8 md:px-6 lg:flex-row lg:items-start lg:gap-12 lg:px-8 lg:py-12">
      <main id="main-content" role="main" class="min-w-0 flex-1">
        <RadialFabMenu />
        <slot />
      </main>

      <aside aria-label="ستون کناری" class="w-full shrink-0 lg:sticky lg:top-24 lg:w-[380px] xl:w-[400px]">
        <SideBar
          v-if="!pending"
          :musicData="{
            music: store.siteSettingData?.music,
            cover: store.siteSettingData?.music_cover,
            music_artist: store.siteSettingData?.music_artist,
            music_title: store.siteSettingData?.music_title,
          }"
          :MetaData="sidebarData"
        />

        <div v-else class="flex flex-col gap-6">
          <div v-for="i in 4" :key="i" class="rounded-3xl border border-line bg-card p-6 shadow-card">
            <skeleton-simple class="mb-4 h-6 w-32 rounded-md" />
            <skeleton-simple :repeat="4" class="mb-3 h-5 w-full rounded-md" />
          </div>
        </div>
      </aside>
    </div>

    <TheFooter />
  </div>
</template>

<script lang="ts" setup>
import { getSideBarDataService } from '~/services/MetaData.service'
import { getSettingDataService } from '~/services/SiteSetting.Service'

const store = useMySettingDataStore()
const nuxt = useNuxtApp()

await callOnce(async () => {
  if (!store.siteSettingData) {
    const res = await getSettingDataService()
    store.setData(res)
  }
})

const { data: sidebarData, pending } = useAsyncData(
  'sidebar-data',
  () => getSideBarDataService(),
  { getCachedData: key => nuxt.payload.static?.[key] ?? nuxt.payload.data?.[key] }
)
</script>
