<template>
  <div>
     <TheHeader :title="mySettingStore.siteSettingData?.site_name" 
     :description="mySettingStore.siteSettingData?.meta_description"
     :count="mySettingStore.siteSettingData?.count"
     ></TheHeader>
     <div class="container mx-auto mt-10 max-md:mt-4  px-6 flex flex-col lg:flex-row gap-36 max-xl:gap-12 max-2xl:gap-24  max-lg:gap-6  min-h-screen">

    <!-- Main content -->
    <main class="w-full lg:w-3/4 flex-1 max-md:mt-2">
       <slot />
    </main>
  
    <!-- Sidebar -->
    <SideBar :musicData="
    {
      music:mySettingStore.siteSettingData?.music,
      cover:mySettingStore.siteSettingData?.music_cover,
      music_artist:mySettingStore.siteSettingData?.music_artist,
      music_title:mySettingStore.siteSettingData?.music_title,
      
    }
    "></SideBar>
  </div>

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