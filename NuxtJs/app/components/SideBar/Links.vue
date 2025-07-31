<template>
 <div class=" rounded-xl my-8 max-md:my-6  ">
        <div class="header-aside-box flex items-center">
            <svg width="36" height="36" viewBox="0 0 39 39" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g clip-path="url(#clip0_62_413)">
                <path d="M6.3375 19.5C6.3375 16.7213 8.59625 14.4625 11.375 14.4625H17.875V11.375H11.375C6.89 11.375 3.25 15.015 3.25 19.5C3.25 23.985 6.89 27.625 11.375 27.625H17.875V24.5375H11.375C8.59625 24.5375 6.3375 22.2787 6.3375 19.5ZM13 21.125H26V17.875H13V21.125ZM27.625 11.375H21.125V14.4625H27.625C30.4037 14.4625 32.6625 16.7213 32.6625 19.5C32.6625 22.2787 30.4037 24.5375 27.625 24.5375H21.125V27.625H27.625C32.11 27.625 35.75 23.985 35.75 19.5C35.75 15.015 32.11 11.375 27.625 11.375Z" fill="#323232"/>
                </g>
                <defs>
                <clipPath id="clip0_62_413">
                <rect width="39" height="39" fill="white"/>
                </clipPath>
                </defs>
                </svg>
                
                
                <span class="mx-1">
                    <svg width="3" height="35" viewBox="0 0 4 41" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect x="-2.48486" width="6.21212" height="41" fill="#323232"/>
                        </svg>
                        
                </span>
                <h4 class="text-[17px] max-md:text-base text-black-300 font-black" > پیوندها</h4>
        </div>
       <div class="BodyCardCateGory mt-4">
        <ul class="flex flex-col ">

            <li v-for="item in data" class="bluew-auto flex justify-between my-1.5 ">
                <a :href="item.link" rel="nofollow " target="_blank" class="text-base font-bold flex items-center text-black-400 transition hover:text-blue-600 max-md:text-sm-2">
                    <svg width="24" height="24" viewBox="0 0 24 24" class="ml-1.5 mb-1 fill-blue-600"  xmlns="http://www.w3.org/2000/svg">
                        <g clip-path="url(#clip0_62_402)">
                        <path d="M12 12C14.21 12 16 10.21 16 8C16 5.79 14.21 4 12 4C9.79 4 8 5.79 8 8C8 10.21 9.79 12 12 12ZM12 14C9.33 14 4 15.34 4 18V20H20V18C20 15.34 14.67 14 12 14Z" />
                        </g>
                        <defs>
                        <clipPath id="clip0_62_402">
                        <rect width="24" height="24" fill="white"/>
                        </clipPath>
                        </defs>
                        </svg>
                        
                    {{item.title}}
                </a>
            </li>
        </ul>
       </div>
            
      </div>
</template>

<script lang="ts" setup>
import type { LinkDTO } from '~/models/SideBarData/MetaDataDTO';

defineProps({
    data:{
        type:Object as PropType<LinkDTO[]>
    }
})
</script>

<style>

</style>