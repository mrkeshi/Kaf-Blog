<template>
  <div class="flex flex-col gap-6">
    <SideBarMusicBox
      :music="musicData.music"
      :cover="musicData.cover"
      :music_title="musicData.music_title"
      :music_artist="musicData.music_artist"
    />
    <SideBarCateGory :data="MetaData?.categories" />
    <SideBarTags :data="MetaData?.tags" />
    <SideBarLinks :data="MetaData?.links" />
  </div>
</template>

<script lang="ts" setup>
import type { PropType } from 'vue'
import type { SidebarDataDTO } from '~/models/SideBarData/MetaDataDTO'

defineProps({
  MetaData: {
    type: Object as PropType<SidebarDataDTO>
  },
  musicData: {
    type: Object as PropType<{
      music?: string
      cover?: string
      music_artist?: string
      music_title?: string
    }>,
    default: () => ({})
  }
})
</script>
