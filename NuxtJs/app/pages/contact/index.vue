<template>
  <div>
    <div class="container mx-auto text-center py-12 max-md:py-12 h-auto">
      <h1 class="text-4xl font-bold mb-4 text-black-400">ارتباط با من</h1>
      <p class="text-lg text-black-300 mb-8 px-4 max-md:text-base"> هم می&zwnj;توانی پیام&zwnj;ات را به آدرس ایمیل
        me@mr-keshi.ir بفرستی و هم اینجا،</p>

      <div class="isolate px-6 py-2 sm:py-8 lg:px-6">

        <form action="#" method="POST" class="mx-auto  max-w-2xl">
          <div class="grid grid-cols-1 gap-x-8 gap-y-6 sm:grid-cols-2">
            <base-input type="text" name="name" placeholder="لطفا نام خود را وارد نمایید. "
              label="نام شما"></base-input>

            <base-input type="email" name="email" placeholder="لطفا ایمیل خود را وارد نمایید. "
              label=" آدرس ایمیل شما"></base-input>


            <base-textarea name="message" label="پیغام شما" placeholder="هرچه دل تنگت می‌خواهد بنویس..." />

          </div>
          <base-button class="mt-10">
            ارسال پیغام شما
          </base-button>
        </form>
      </div>

    </div>
  </div>
</template>

<script lang="ts" setup>
definePageMeta({
  layout: 'simple-layout'
})
</script>

<style></style>