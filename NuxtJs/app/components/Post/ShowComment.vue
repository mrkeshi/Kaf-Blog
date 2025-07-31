<template>
  <div>
      <h3 class="text-xl max-md:text-[17px] mt-2 font-bold text-black-400">
                    <b class="text-blue-600 font-black" v-persian-number="commentCount"></b>
                     کامنت ثبت شده است. 
                  </h3>
                  <div class="comments-box flex my-4 flex-col gap-y-8">

                    <div class="comment w-full p-6 max-md:p-3 border-2 rounded-3xl border-black-100" v-for="comment in comments">
                      <div class="flex justify-between">
                          <div class="user">
                            <li class="bluew-auto flex items-center justify-between font-bold">
                              <a href="#" class="text-base ml-1 font-bold flex items-center text-blue-600 transition  hover:text-blue-600 max-md:text-sm-2">
                                  <svg width="22" height="22" viewBox="0 0 24 24" class=" mb-1 fill-blue-600" xmlns="http://www.w3.org/2000/svg">
                                      <g clip-path="url(#clip0_62_402)">
                                      <path d="M12 12C14.21 12 16 10.21 16 8C16 5.79 14.21 4 12 4C9.79 4 8 5.79 8 8C8 10.21 9.79 12 12 12ZM12 14C9.33 14 4 15.34 4 18V20H20V18C20 15.34 14.67 14 12 14Z"></path>
                                      </g>
                                      <defs>
                                      <clipPath id="clip0_62_402">
                                      <rect width="24" height="24" fill="white"></rect>
                                      </clipPath>
                                      </defs>
                                      </svg>
                                      
                                  {{comment.name}} 
                              </a>
                              گفته:
                          </li>
                          </div>
                            <div class="date text-black-200 text-sm-2 max-md:text-sm" v-persian-number="comment.created_at">
                              
                            </div>
                      </div>
                      <p class="text-black-300 my-2 mr-1 max-md:text-sm">
                        {{comment.message}}
                      </p>
                      <div class="flex items-center max-md:text-sm flex-wrap">
                        <b class="text-blue-600" v-if="comment.answer">پاسخ :</b>
                        <p class="text-black-300 my-2 mr-1" v-if="comment.answer">
                         {{comment.answer}}
                        </p>
                      </div>
                    </div>
                    
                  </div>
  </div>
</template>

<script lang="ts" setup>
import type { Prop, PropType } from 'vue';
import { number } from 'yup';
import type { CommentDTO } from '~/models/Post/PostDTO';


defineProps({
  commentCount:{
    type:Number,
    default:0
  },
  comments:{
    type:Object as PropType<CommentDTO[]>
  }
})


</script>

<style>

</style>