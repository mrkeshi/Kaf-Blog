<template>
  <div>
    <TheHeader></TheHeader>
     <div class="container mx-auto mt-10 max-md:mt-4  px-6 flex flex-col lg:flex-row gap-36 max-xl:gap-12 max-2xl:gap-24  max-lg:gap-6  min-h-screen">

    <!-- Main content -->
    <main class="w-full lg:w-3/4 flex-1 max-md:mt-2">
       <slot />
    </main>
  
    <!-- Sidebar -->
    <SideBar></SideBar>
  </div>

  <TheFooter></TheFooter>
  </div>
</template>

<script lang="ts" setup>


</script>

<style>

</style>