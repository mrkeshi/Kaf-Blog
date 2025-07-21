<template>
         <form action="#" method="POST" class="mx-auto  w-full">
                    <div class="grid grid-cols-1 gap-x-8 gap-y-6 sm:grid-cols-2">
                      <div>
                        <label for="first-name" class="block text-base  text-black-400 font-bold text-right">نام شما: </label>
                        <div class="mt-2.5">
                          <input type="text" placeholder="لطفا نام خود را وارد نمایید" name="first-name" id="first-name" autocomplete="given-name" class="block w-full rounded-2xl  px-3.5 py-3.5 text-base text-black-300 outline-2 -outline-offset-1 outline-black-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-blue-600">
                        </div>
                      </div>
                      <div>
                        <label for="first-name" class="block text-base  text-black-400 font-bold text-right"> آدرس ایمیل شما :  </label>
                        <div class="mt-2.5">
                          <input type="text" placeholder="لطفا ایمیل خود را وارد نمایید" name="first-name" id="first-name" autocomplete="given-name" class="block w-full rounded-2xl  px-3.5 py-3.5 text-base text-black-300 outline-2 -outline-offset-1 outline-black-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-blue-600">
                        </div>
                      </div>
                 
                      <div class="sm:col-span-2">
                        <label for="first-name" class="block text-base  text-black-400 font-bold text-right"> پیغام شما: </label>
                        <div class="mt-2.5">
                          <textarea placeholder="هرچه دل تنگت میخواهد بنویس.." name="message" id="message" rows="6" class="block w-full rounded-2xl  px-3.5 py-3.5 text-base text-black-300 outline-2 -outline-offset-1 outline-black-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-blue-600"></textarea>
                        </div>
                      </div>
                    
                    </div>
                    <div class="my-6">
                      <button type="submit" class="block w-full rounded-xl cursor-pointer bg-black-400 px-3.5 py-3.5 text-center text-base font-semibold text-white shadow-xs hover:bg-blue-600 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600">ارسال کامنت</button>
                    </div>
                  </form> 
</template>

<script lang="ts" setup>

</script>

<style>

</style>