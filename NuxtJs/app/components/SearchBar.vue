<template>
  <div class="flex items-center">
    <button
      v-if="!subscribed"
      @click="handleSubscribe"
      :disabled="loading"
      class="inline-flex items-center gap-1.5 rounded-full border border-line px-4 py-2 text-xs font-bold text-ink-soft transition-all duration-200 hover:border-brand hover:bg-brand/10 hover:text-brand disabled:opacity-40"
      :aria-label="loading ? 'در حال پردازش...' : 'دنبال کردن'"
    >
      <svg v-if="!loading" width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm5 11h-4v4h-2v-4H7v-2h4V7h2v4h4v2z" />
      </svg>
      <span v-else class="inline-block animate-spin-slow" aria-hidden="true">⟳</span>
      دنبال کردن
    </button>

    <button
      v-else
      @click="handleUnsubscribe"
      :disabled="loading"
      class="inline-flex items-center gap-1.5 rounded-full px-4 py-2 text-xs font-bold text-ink-soft transition-all duration-200 hover:bg-card-soft hover:text-ink disabled:opacity-40"
      aria-label="لغو اشتراک"
    >
      <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm5 11H7v-2h10v2z" />
      </svg>
      لغو اشتراک
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { usePushNotification } from '~/composable/usePushNotification'

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
  if (success) subscribed.value = false
  loading.value = false
}
</script>
