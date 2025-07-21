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
    <SideBar v-if="!pending" :musicData="
    {
      music:mySettingStore.siteSettingData?.music,
      cover:mySettingStore.siteSettingData?.music_cover,
      music_artist:mySettingStore.siteSettingData?.music_artist,
      music_title:mySettingStore.siteSettingData?.music_title,
      
    }
    "
    :MetaData="data"
    ></SideBar> 
    <div v-else class="w-full lg:w-1/4"> 
    <skeleton-simple class="h-28 w-auto rounded-2xl mb-8" :repeat="7"  />
    </div>


  </div>

  <TheFooter></TheFooter>
  </div>
</template>

<script lang="ts" setup>
import { getSideBarDataService } from '~/services/MetaData.service'
import { getSettingDataService } from '~/services/SiteSetting.Service'
const mySettingStore = useMySettingDataStore()
const nuxt=useNuxtApp()
await callOnce(async () => {
  if (!mySettingStore.siteSettingData) {
    const res = await getSettingDataService()
    mySettingStore.setData(res)
  }
})

const {data,pending}=useAsyncData("sidebar-data",()=>getSideBarDataService(),{
   getCachedData: key => nuxt.payload.static?.[key] ?? nuxt.payload.data?.[key]
})

</script>
<style>

</style>