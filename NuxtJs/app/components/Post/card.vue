<template>
   <article class="mt-2">
            <h2 class="text-2xl text-black-400 font-black max-md:text-[20px] mb-4">
                <NuxtLink :to="{name:'slug',params:{slug:post.slug}}">{{ post.title }}</NuxtLink>

            </h2>
            <div class="flex items-center my-2 ">
                <div class="flex items-center flex-wrap">
                    <svg width="22" height="22" class="fill-blue-600" viewBox="0 0 24 24"   stroke="none" xmlns="http://www.w3.org/2000/svg">
                        <g clip-path="url(#clip0_62_202)">
                        <path opacity="0.3" d="M5 8H19V6H5V8Z" />
                        <path d="M7 11H9V13H7V11ZM19 4H18V2H16V4H8V2H6V4H5C3.89 4 3.01 4.9 3.01 6L3 20C3 21.1 3.89 22 5 22H19C20.1 22 21 21.1 21 20V6C21 4.9 20.1 4 19 4ZM19 20H5V10H19V20ZM19 8H5V6H19V8ZM15 11H17V13H15V11ZM11 11H13V13H11V11Z" />
                        </g>
                        <defs>
                        <clipPath id="clip0_62_202">
                        <rect width="24" height="24" fill="white"/>
                        </clipPath>
                        </defs>
                        </svg>
                        <span class="text-sm-2  mr-1 max-md:text-xs  text-black-300 font-light" v-persian-number="post.created_at"></span>
                        
                </div>
                <span class="text-sm-2 mx-1.5"> | </span>
                <NuxtLink :to="{name:'category-slug',params:{slug:post.category.slug}}" class="text-sm-2 max-md:text-xs  text-black-300 font-light"> <i class="text-blue-600 font-black">#</i> {{post.category.name}}</NuxtLink>
                <span class="text-sm-2 mx-1.5"> | </span>
                <div class="flex items-center">
                    <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <g clip-path="url(#clip0_62_199)">
                        <path d="M12.9866 8.23335C11.94 5.51335 8.21329 5.36668 9.11329 1.41335C9.17996 1.12001 8.86663 0.893346 8.61329 1.04668C6.19329 2.47335 4.45329 5.33335 5.91329 9.08001C6.03329 9.38668 5.67329 9.67335 5.41329 9.47335C4.20663 8.56001 4.07996 7.24668 4.18663 6.30668C4.22663 5.96001 3.77329 5.79335 3.57996 6.08001C3.12663 6.77335 2.66663 7.89335 2.66663 9.58001C2.91996 13.3133 6.07329 14.46 7.20663 14.6067C8.82663 14.8133 10.58 14.5133 11.84 13.36C13.2266 12.0733 13.7333 10.02 12.9866 8.23335ZM6.79996 11.5867C7.75996 11.3533 8.25329 10.66 8.38663 10.0467C8.60663 9.09335 7.74663 8.16001 8.32663 6.65335C8.54663 7.90001 10.5066 8.68001 10.5066 10.04C10.56 11.7267 8.73329 13.1733 6.79996 11.5867Z" class="fill-blue-600"/>
                        </g>
                        <defs>
                        <clipPath id="clip0_62_199">
                        <rect width="16" height="16" fill="white"/>
                        </clipPath>
                        </defs>
                        </svg>
                        <span class="text-sm-2 max-md:text-xs  text-black-300 font-light"><span v-persian-number="post.views"></span> بازدید</span>

                        
                </div>
                <span class="text-sm-2 mx-1.5"> | </span>
                <div class="flex items-center">
                    <svg width="17" height="17" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <g clip-path="url(#clip0_62_196)">
                        <path d="M16.4925 1.5H1.5V13.5H13.5L16.5 16.5L16.4925 1.5ZM13.5 10.5H4.5V9H13.5V10.5ZM13.5 8.25H4.5V6.75H13.5V8.25ZM13.5 6H4.5V4.5H13.5V6Z" class="fill-blue-600"/>
                        </g>
                        <defs>
                        <clipPath id="clip0_62_196">
                        <rect width="18" height="18" fill="white"/>
                        </clipPath>
                        </defs>
                        </svg>
                        
                        <span class="text-sm-2 max-md:text-xs mr-1  text-black-300 font-light"><span v-persian-number="post.comment_count"></span> نظر</span>

                        
                </div>
              
            </div>
            <div class="w-full h-[1px] bg-black-100 mt-3 rounded-2xl"></div>
            <div class="BodyArticle my-2">
                <p class="text-base max-md:text-sm-2 text-black-300 font-medium leading-7 text-justify" v-text="truncatedContent" ></p>

            </div>
            <div class="FooterArticle">
                <NuxtLink :to="{name:'slug',params:{slug:post.slug}}"  class="inline-block float-left px-4 py-1.5 text-sm font-semibold text-black-400 border border-black-400 rounded-full transition-all duration-300 hover:bg-blue-600 hover:text-white">
                    ادامه مطلب
                  </NuxtLink>
                              </div>
        </article>
</template>

<script lang="ts" setup>
import { type PostListDTO } from '~/models/Post/PostDTO';
import { computed } from 'vue';
import type Slug from '~/pages/[slug].vue';
import decodeHtml from '~/utilities/decodeHtml';
const props=defineProps<{post:PostListDTO}>()

const truncatedContent = computed(() => {
  if (!props.post.content) return ''

  const maxLength = 450
  const noTags = props.post.content.replace(/<[^>]+>/g, '')
  const plainText = decodeHtml(noTags)

  return plainText.length <= maxLength
    ? plainText
    : plainText.slice(0, maxLength) + '...'
})
</script>

<style>

</style>