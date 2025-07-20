
import { defineStore } from 'pinia'
import { ref, type Ref } from 'vue'
import type { SiteSettingDTO } from '~/models/SiteSettingDTO'
import { getSettingDataService } from '~/services/SiteSetting.Service'
export const useMySettingDataStore = defineStore('mySettingDataStore', () => {
  const siteSettingData: Ref<SiteSettingDTO | null> = ref(null)

  const setData = (data: SiteSettingDTO) => {
    siteSettingData.value = data
  }

  return {
    siteSettingData,
    setData,
  }
})
