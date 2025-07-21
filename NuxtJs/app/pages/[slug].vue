<template>
  <div class="articles flex flex-col">
    <article>
      <PostSingle></PostSingle>
      <div class="h-0.5 w-full bg-black-100 my-8 max-md:my-4"></div>
      <div class="comments flex flex-col">
        <PostShowComment></PostShowComment>
        <PostSendComment class="mb-8"></PostSendComment>
      </div>
    </article>


  </div>
</template>

<script lang="ts" setup>


</script>

<style></style>