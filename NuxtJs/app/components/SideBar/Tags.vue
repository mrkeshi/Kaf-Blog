<template>
    <div class=" rounded-xl my-8   ">
        <div class="header-aside-box flex items-center">
            <svg width="36" height="36" viewBox="0 0 41 41" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M34.1666 17.0834V13.6667H27.3333V6.83337H23.9166V13.6667H17.0833V6.83337H13.6666V13.6667H6.83325V17.0834H13.6666V23.9167H6.83325V27.3334H13.6666V34.1667H17.0833V27.3334H23.9166V34.1667H27.3333V27.3334H34.1666V23.9167H27.3333V17.0834H34.1666ZM23.9166 23.9167H17.0833V17.0834H23.9166V23.9167Z" fill="#323232"/>
                </svg>
                
                <span class="mx-1">
                    <svg width="3" height="35" viewBox="0 0 4 41" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect x="-2.48486" width="6.21212" height="41" fill="#323232"/>
                        </svg>
                        
                </span>
                <h4 class="text-[17px] max-md:text-base text-black-300 font-black" >برچسپ ها</h4>
        </div>
       <div class="BodyCardCateGory mt-4">
        <ul class="flex gap-2 flex-wrap ">
            <li v-for="item in data" class="bluew-auto flex justify-between my-1 ">
                <NuxtLink :to="{name:'tag-slug',params:{slug:item.slug}}" class="text-black-400 border-1 border-black-400 px-2.5 py-1.5 text-center rounded-3xl  hover:text-white transition hover:bg-black-400 text-sm max-md:text-sm-2 font-medium">{{ item.name }}</NuxtLink>
            </li>
        
 
        </ul>
       </div>
            
      </div>
</template>

<script lang="ts" setup>
import type { TagDTO } from '~/models/SideBarData/MetaDataDTO';

defineProps({
    data:{
        type:Object as PropType<TagDTO[]>
    }
})
</script>

<style>

</style>