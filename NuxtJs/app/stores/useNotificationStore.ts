import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import type { NotificationDTO } from '~/models/Notification/NotificationDTO'

export const useNotificationStore = defineStore('notifications', () => {
  const notifications = ref<NotificationDTO[]>([])
  const lastSeenId = ref<number>(0)

  // clientToken: stable UUID per browser stored in localStorage
  const clientToken = ref<string>('')

  const unreadCount = computed(() => notifications.value.length)
  const hasUnread = computed(() => unreadCount.value > 0)

  function initToken() {
    if (!process.client) return
    let token = localStorage.getItem('notif_token')
    if (!token) {
      token = crypto.randomUUID()
      localStorage.setItem('notif_token', token)
    }
    clientToken.value = token

    const storedLastId = localStorage.getItem('notif_last_id')
    if (storedLastId) lastSeenId.value = parseInt(storedLastId, 10)
  }

  function addNotifications(items: NotificationDTO[]) {
    // Prepend new ones, avoid duplicates
    const existingIds = new Set(notifications.value.map(n => n.id))
    const fresh = items.filter(n => !existingIds.has(n.id))
    if (fresh.length) {
      notifications.value = [...fresh, ...notifications.value]
      // Track max seen id for future polling
      const maxId = Math.max(...items.map(n => n.id))
      if (maxId > lastSeenId.value) {
        lastSeenId.value = maxId
        if (process.client) localStorage.setItem('notif_last_id', String(maxId))
      }
    }
  }

  async function markAllRead() {
    if (!notifications.value.length || !clientToken.value) return
    const ids = notifications.value.map(n => n.id)
    const config = useRuntimeConfig()
    try {
      await $fetch(`${config.public.baseURL}notifications/mark-read/`, {
        method: 'POST',
        body: { token: clientToken.value, ids }
      })
    } catch (_) { /* silent */ }
    notifications.value = []
  }

  async function dismissOne(id: number) {
    if (!clientToken.value) return
    try {
      const config = useRuntimeConfig()
      await $fetch(`${config.public.baseURL}notifications/mark-read/`, {
        method: 'POST',
        body: { token: clientToken.value, ids: [id] }
      })
    } catch (_) { /* silent */ }
    notifications.value = notifications.value.filter(n => n.id !== id)
  }

  return {
    notifications,
    unreadCount,
    hasUnread,
    clientToken,
    lastSeenId,
    initToken,
    addNotifications,
    markAllRead,
    dismissOne,
  }
})
