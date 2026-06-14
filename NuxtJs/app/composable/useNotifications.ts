/**
 * Polls the backend every 60 seconds for new notifications.
 * Uses a stable client token stored in localStorage.
 * Call once from the default layout.
 */
import { onMounted, onUnmounted } from 'vue'
import type { NotificationDTO } from '~/models/Notification/NotificationDTO'

export function useNotifications() {
  const store = useNotificationStore()
  const config = useRuntimeConfig()
  let timer: ReturnType<typeof setInterval> | null = null

  async function fetchNotifications() {
    if (!store.clientToken) return
    try {
      const params = new URLSearchParams({ token: store.clientToken })
      if (store.lastSeenId > 0) params.set('since', String(store.lastSeenId))

      const data = await $fetch<NotificationDTO[]>(
        `${config.public.baseURL}notifications/?${params.toString()}`
      )
      if (Array.isArray(data) && data.length) {
        store.addNotifications(data)
      }
    } catch (_) { /* network errors are silent */ }
  }

  onMounted(() => {
    store.initToken()
    fetchNotifications()
    // Poll every 60 seconds
    timer = setInterval(fetchNotifications, 60_000)
  })

  onUnmounted(() => {
    if (timer) clearInterval(timer)
  })

  return { fetchNotifications }
}
