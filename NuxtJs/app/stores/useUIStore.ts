// stores/ui.ts
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUIStore = defineStore('ui', () => {
  const isSearchOpen = ref(false)
  const isSearchClosing = ref(false)
  const searchQuery = ref<string>('')

  const openSearch = () => {
    isSearchOpen.value = true
    isSearchClosing.value = false
  }

  const closeSearch = () => {
    isSearchClosing.value = true
    setTimeout(() => {
      isSearchOpen.value = false
      isSearchClosing.value = false
      searchQuery.value = ''
    }, 400)
  }

  const setSearchQuery = (val: string) => {
    searchQuery.value = val
  }

  return {
    isSearchOpen,
    isSearchClosing,
    searchQuery,
    openSearch,
    closeSearch,
    setSearchQuery
  }
})
