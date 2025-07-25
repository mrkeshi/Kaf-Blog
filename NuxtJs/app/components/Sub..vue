<template>

      <div class="flex items-center mt-2">
              <svg class="ml-1 -mb-1" width="24" height="24" viewBox="0 0 24 24" fill="#2B2929"
                xmlns="http://www.w3.org/2000/svg">
                <g clip-path="url(#clip0_62_188)">
                  <path opacity="0.3"
                    d="M9 10C9.82843 10 10.5 9.32843 10.5 8.5C10.5 7.67157 9.82843 7 9 7C8.17157 7 7.5 7.67157 7.5 8.5C7.5 9.32843 8.17157 10 9 10Z"
                    fill="#323232" />
                  <path opacity="0.3"
                    d="M4.34009 17H13.6601C12.8201 16.42 10.7901 15.75 9.00009 15.75C7.21009 15.75 5.18009 16.42 4.34009 17Z"
                    fill="#323232" />
                  <path
                    d="M9 6C10.93 6 12.5 4.43 12.5 2.5C12.5 0.57 10.93 -1 9 -1C7.07 -1 5.5 0.57 5.5 2.5C5.5 4.43 7.07 6 9 6ZM9 1C9.83 1 10.5 1.67 10.5 2.5C10.5 3.33 9.83 4 9 4C8.17 4 7.5 3.33 7.5 2.5C7.5 1.67 8.17 1 9 1ZM9 7.75C6.66 7.75 2 8.92 2 11.25V13H16V11.25C16 8.92 11.34 7.75 9 7.75ZM4.34 11C5.18 10.42 7.21 9.75 9 9.75C10.79 9.75 12.82 10.42 13.66 11H4.34ZM16.04 7.81C17.2 8.65 18 9.77 18 11.25V13H22V11.25C22 9.23 18.5 8.08 16.04 7.81ZM15 6C16.93 6 18.5 4.43 18.5 2.5C18.5 0.57 16.93 -1 15 -1C14.46 -1 13.96 -0.87 13.5 -0.65C14.13 0.24 14.5 1.33 14.5 2.5C14.5 3.67 14.13 4.76 13.5 5.65C13.96 5.87 14.46 6 15 6Z"
                    fill="#323232" />
                </g>
                <defs>
                  <clipPath id="clip0_62_188">
                    <rect width="24" height="24" fill="white" />
                  </clipPath>
                </defs>
              </svg>
              <span class="text-xs text-black-200"><span v-persian-number="count"></span> دنبال کننده</span>
            </div>

</template>

<script lang="ts" setup>
import { number } from 'yup';


defineProps({
  count:{
    type:number,
    default:0,
  }
})

</script>

<style>

</style>