<template>
  <div >
     <TheHeader :title="mySettingStore.siteSettingData?.site_name"
      :description="mySettingStore.siteSettingData?.meta_description"
       :count="mySettingStore.siteSettingData?.count"></TheHeader>
    <slot />
      <TheFooter></TheFooter>

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

<style>

</style>