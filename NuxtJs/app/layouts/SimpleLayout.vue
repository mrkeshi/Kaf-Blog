<template>
  <div class="flex min-h-dvh flex-col bg-base text-ink">
    <TheHeader
      :title="mySettingStore.siteSettingData?.site_name"
      :description="mySettingStore.siteSettingData?.meta_description"
      :icon="mySettingStore.siteSettingData?.site_icon"
      :count="mySettingStore.siteSettingData?.count"
    />

    <RadialFabMenu />

    <main id="main-content" role="main" class="mx-auto w-full max-w-[1440px] flex-1 px-4 py-10 md:px-6 lg:px-8 lg:py-14">
      <slot />
    </main>

    <TheFooter />
  </div>
</template>

<script lang="ts" setup>
import { getSettingDataService } from '~/services/SiteSetting.Service'

const mySettingStore = useMySettingDataStore()

await callOnce(async () => {
  if (!mySettingStore.siteSettingData) {
    const res = await getSettingDataService()
    mySettingStore.setData(res)
  }
})
</script>
