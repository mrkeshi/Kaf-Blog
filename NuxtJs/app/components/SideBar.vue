<template>
    <aside class="w-full lg:w-1/4  rounded-2xl  space-y-4">
        <SideBarMusicBox :music="musicData.music" :cover="musicData.cover" :music_title="musicData.music_title"
            :music_artist="musicData.music_artist"></SideBarMusicBox>

        <SideBarCateGory></SideBarCateGory>
        <SideBarTags></SideBarTags>
        <SideBarLinks></SideBarLinks>
    </aside>

</template>

<script lang="ts" setup>
import { type LinkDTO, type SidebarDataDTO, type TagDTO } from '~/models/SideBarData/MetaDataDTO';
import type { PropType } from 'vue';
defineProps({

    MetaData:{
        type:Object as PropType<SidebarDataDTO>
    },

//     Tag: {
//     type: Object as PropType<TagDTO>,
//     required: true,
//   },
//     Link: {
//     type: Object as PropType<LinkDTO>,
//     required: true,
//   },
//     CateGory: {
//     type: Object as PropType<CategoryDTO>,
//     required: true,
//   },

    musicData: {
        type: Object as PropType<{
            music?: string,
            cover?: string,
            music_artist?: string,
            music_title?: string,
        }>,
        default: () => ({})
    }
})
</script>

<style></style>