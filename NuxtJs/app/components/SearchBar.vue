<template>
    <div class="flex items-center">
        <a href="#"
            class="bg-black-400 border-2 border-black-400 rounded-full max-md:p-2 max-md:text-sm-2 px-3 py-2 transition hover:bg-black-150 hover:text-black-400 h-12 text-center text-white">دنبال
            کردن</a>

        <svg @click="OpenSearch" class="mr-2.5 hover:opacity-80 cursor-pointer" width="24" height="24"
            viewBox="0 0 23 23" fill="#2B2929" xmlns="http://www.w3.org/2000/svg">
            <path
                d="M16.375 14.5H15.3875L15.0375 14.1625C16.2625 12.7375 17 10.8875 17 8.875C17 4.3875 13.3625 0.75 8.875 0.75C4.3875 0.75 0.75 4.3875 0.75 8.875C0.75 13.3625 4.3875 17 8.875 17C10.8875 17 12.7375 16.2625 14.1625 15.0375L14.5 15.3875V16.375L20.75 22.6125L22.6125 20.75L16.375 14.5ZM8.875 14.5C5.7625 14.5 3.25 11.9875 3.25 8.875C3.25 5.7625 5.7625 3.25 8.875 3.25C11.9875 3.25 14.5 5.7625 14.5 8.875C14.5 11.9875 11.9875 14.5 8.875 14.5Z"
                fill="#323232" />
        </svg>

        <div ref="searchBar"
            class="fixed top-0 right-0 left-0 bg-black-100 border-b border-black-200 z-50 p-4 shadow-xl rounded-b-lg"
            :class="{'hidden':!isSearchOpen,'animate-slide-in':isSearchOpen,'animate-slide-out':isSearchColse}"
            >
            <div class="flex flex-col sm:flex-row items-center justify-between gap-2">
                <input type="text" v-model="searchQuery" ref="searchInput" @keydown.enter="SubmitSearch"
                    placeholder="جستجو..."
                    class="w-full sm:flex-1 p-3 text-black-400 border-[2px] border-black-200 rounded-lg shadow-inner focus:outline-none focus:ring-1 focus:ring-black-400 transition" />
                <div class="flex items-center gap-2 mt-2 sm:mt-0">
                    <button @click="SubmitSearch"
                        class="px-4 py-2 bg-black-400 hover:bg-black-150 border-black-400 border-1  text-white hover:text-black-400 rounded-lg text-sm font-medium transition">
                        جستجو
                    </button>
                    <button @click="CloseSearch"
                        class="px-3 py-2 border border-black-200 text-black-400 rounded-lg hover:bg-red-100 hover:text-red-600 font-medium transition text-sm">
                        بستن
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">

const isSearchOpen = ref<boolean>(false)
const isSearchColse = ref<boolean>(false)
const searchQuery = ref<String>('')
const searchBar = ref<HTMLDivElement>()
const searchInput = ref<HTMLInputElement>()

const OpenSearch = () => {
    isSearchOpen.value = true
    isSearchColse.value = false
    searchBar.value?.focus()
}

const CloseSearch = () => {
    isSearchColse.value = true
    setTimeout(() => {
        isSearchOpen.value = false
        isSearchColse.value = false
        searchQuery.value = ""
    }, 400)
}


const SubmitSearch = () => {
    searchQuery.value = searchQuery.value.trim();
    if (searchQuery.value) alert(`در حال جستجو برای: ${searchQuery.value}`);
};



</script>