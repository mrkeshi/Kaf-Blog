<template>
  <div class="flex items-center gap-3">
    <!-- دکمه دنبال کردن / لغو اشتراک -->
    <button
      v-if="!subscribed"
      @click="handleSubscribe"
      :disabled="loading"
      class="border-2 rounded-full max-md:p-2 max-md:text-sm-2 px-3 py-2 h-12 text-center transition
        cursor-pointer
        bg-black-400 border-black-400 text-white
        hover:bg-black-150 hover:text-black-400
        disabled:cursor-not-allowed disabled:bg-black-200 disabled:text-gray-400"
    >
      دنبال کردن
    </button>

    <button
      v-else
      @click="handleUnsubscribe"
      :disabled="loading"
      class="border-2 cursor-pointer w-32 border-black-400 text-sm rounded-full max-md:p-2 max-md:text-sm-2 px-3 py-2 transition h-12 text-center
        bg-transparent text-black-400
        hover:bg-black-150 hover:text-black-400
        disabled:cursor-not-allowed disabled:bg-black-200 disabled:text-gray-400"
    >
      لغو اشتراک
    </button>

    <!-- آیکون جستجو -->
    <svg @click="ui.openSearch"
         class="mr-2.5 hover:opacity-80 cursor-pointer"
         width="24" height="24" viewBox="0 0 23 23" fill="#2B2929"
         xmlns="http://www.w3.org/2000/svg">
      <path d="M16.375 14.5H15.3875L15.0375 14.1625C16.2625 12.7375 17 10.8875 17 8.875C17 4.3875 13.3625 0.75 8.875 0.75C4.3875 0.75 0.75 4.3875 0.75 8.875C0.75 13.3625 4.3875 17 8.875 17C10.8875 17 12.7375 16.2625 14.1625 15.0375L14.5 15.3875V16.375L20.75 22.6125L22.6125 20.75L16.375 14.5ZM8.875 14.5C5.7625 14.5 3.25 11.9875 3.25 8.875C3.25 5.7625 5.7625 3.25 8.875 3.25C11.9875 3.25 14.5 5.7625 14.5 8.875C14.5 11.9875 11.9875 14.5 8.875 14.5Z" />
    </svg>

    <!-- نوار جستجو -->
    <div class="fixed top-0 right-0 left-0 bg-black-100 border-b border-black-200 z-50 p-4 shadow-xl rounded-b-lg"
         :class="{
           hidden: !ui.isSearchOpen,
           'animate-slide-in': ui.isSearchOpen,
           'animate-slide-out': ui.isSearchClosing
         }"
    >
      <div class="flex flex-col sm:flex-row items-center justify-between gap-2">
        <input type="text"
               v-model="ui.searchQuery"
               @keydown.enter="SubmitSearch"
               placeholder="جستجو..."
               class="w-full sm:flex-1 p-3 text-black-400 border-[2px] border-black-200 rounded-lg shadow-inner focus:outline-none focus:ring-1 focus:ring-black-400 transition"
        />
        <div class="flex items-center gap-2 mt-2 sm:mt-0">
          <button @click="SubmitSearch"
                  class="px-4 py-2 bg-black-400 cursor-pointer hover:bg-black-150 border-black-400 border-1 text-white hover:text-black-400 rounded-lg text-sm font-medium transition">
            جستجو
          </button>
          <button @click="CloseSearch"
                  class="px-3 py-2 border cursor-pointer border-black-200 text-black-400 rounded-lg hover:bg-red-100 hover:text-red-600 font-medium transition text-sm">
            بستن
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUIStore } from '../stores/useUIStore'
import { usePushNotification } from '~/composable/usePushNotification'

const ui = useUIStore()
const router = useRouter()

const { subscribeUserToPush, unsubscribeUserFromPush, isUserSubscribed } = usePushNotification()

const subscribed = ref(false)
const loading = ref(false)

onMounted(async () => {
  subscribed.value = await isUserSubscribed()
})

const handleSubscribe = async () => {
  loading.value = true
  await subscribeUserToPush()
  subscribed.value = await isUserSubscribed()
  loading.value = false
}

const handleUnsubscribe = async () => {
  loading.value = true
  const success = await unsubscribeUserFromPush()
  if (success) {
    subscribed.value = false
  }
  loading.value = false
}

const SubmitSearch = () => {
  ui.searchQuery = ui.searchQuery.trim()
  if (ui.searchQuery) {
    router.push({
      name: 'search',
      query: { q: ui.searchQuery }
    })
    ui.closeSearch()
  }
}

const CloseSearch = () => {
  ui.closeSearch()
}
</script>
