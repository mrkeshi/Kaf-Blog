
import { defineStore } from 'pinia'
import { ref, type Ref } from 'vue'
import type { PaginatedPostListResponseDTO, PostListDTO } from '~/models/Post/PostDTO'


export const usePostStore = defineStore('PostStore', () => {
  const postList: Ref<PaginatedPostListResponseDTO | null> = ref(null)
  const currentPage:Ref<number> = ref(1)
  const setData = (data: PaginatedPostListResponseDTO) => {
    postList.value = data
  }

  return {
    postList,
    setData,
    currentPage
  }
})
