<template>
  <div class="relative" ref="bellRef">
    <button
      @click="togglePanel"
      :aria-expanded="panelOpen"
      aria-label="اعلان‌ها"
      class="relative flex h-10 w-10 items-center justify-center rounded-xl border border-line bg-card-soft text-ink-soft transition-all duration-200 hover:border-brand/40 hover:text-brand"
      :class="store.hasUnread ? 'border-brand/30 text-brand' : ''"
    >
      <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M12 22c1.1 0 2-.9 2-2h-4a2 2 0 002 2zm6-6V11c0-3.07-1.64-5.64-4.5-6.32V4a1.5 1.5 0 00-3 0v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z"/>
      </svg>
      <span
        v-if="store.hasUnread"
        class="absolute -right-1 -top-1 flex h-5 min-w-5 items-center justify-center rounded-full bg-rose px-1 text-[10px] font-bold text-white shadow-sm"
        :aria-label="`${store.unreadCount} اعلان`"
      >
        {{ store.unreadCount > 9 ? '۹+' : store.unreadCount }}
      </span>
    </button>

    <Transition
      enter-active-class="animate-notification-in"
      leave-active-class="animate-notification-out"
    >
      <div
        v-if="panelOpen"
        role="dialog"
        aria-label="پنل اعلان‌ها"
        class="absolute left-0 top-12 z-50 w-80 overflow-hidden rounded-2xl border border-line bg-card shadow-pop"
      >
        <div class="flex items-center justify-between border-b border-line px-4 py-3">
          <h3 class="text-sm font-extrabold text-ink">اعلان‌ها</h3>
          <button
            v-if="store.hasUnread"
            @click="store.markAllRead"
            class="text-xs font-bold text-brand transition-opacity duration-200 hover:opacity-70"
          >
            همه را خواندم
          </button>
        </div>

        <div class="max-h-80 overflow-y-auto">
          <TransitionGroup name="notif-item" tag="ul" role="list">
            <li
              v-for="notif in store.notifications"
              :key="notif.id"
              class="group relative border-b border-line-soft last:border-b-0"
            >
              <component
                :is="notif.link ? 'a' : 'div'"
                :href="notif.link || undefined"
                :target="notif.link?.startsWith('http') ? '_blank' : undefined"
                class="flex items-start gap-3 px-4 py-3.5 transition-colors duration-150 hover:bg-card-soft"
                :class="notif.link ? 'cursor-pointer' : ''"
                @click="notif.link ? store.dismissOne(notif.id) : undefined"
              >
                <span
                  class="mt-0.5 flex h-7 w-7 shrink-0 items-center justify-center rounded-full text-white text-xs"
                  :class="typeColors[notif.type]"
                  aria-hidden="true"
                >
                  <svg v-if="notif.type === 'post'" width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/>
                  </svg>
                  <svg v-else-if="notif.type === 'success'" width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z"/>
                  </svg>
                  <svg v-else-if="notif.type === 'warning'" width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z"/>
                  </svg>
                  <svg v-else-if="notif.type === 'error'" width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12 19 6.41z"/>
                  </svg>
                  <svg v-else width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/>
                  </svg>
                </span>

                <div class="min-w-0 flex-1">
                  <p class="text-[13px] font-bold leading-snug text-ink">{{ notif.title }}</p>
                  <p class="mt-0.5 text-xs leading-relaxed text-ink-soft line-clamp-2">{{ notif.message }}</p>
                </div>

                <button
                  @click.prevent.stop="store.dismissOne(notif.id)"
                  aria-label="بستن اعلان"
                  class="mt-0.5 shrink-0 opacity-0 transition-opacity duration-150 group-hover:opacity-60 hover:!opacity-100"
                >
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" class="text-ink-faint">
                    <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12 19 6.41z"/>
                  </svg>
                </button>
              </component>
            </li>
          </TransitionGroup>

          <div v-if="!store.hasUnread" class="flex flex-col items-center py-10 text-center" role="status">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor" class="mb-2 text-ink-faint opacity-30" aria-hidden="true">
              <path d="M12 22c1.1 0 2-.9 2-2h-4a2 2 0 002 2zm6-6V11c0-3.07-1.64-5.64-4.5-6.32V4a1.5 1.5 0 00-3 0v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z"/>
            </svg>
            <p class="text-[13px] text-ink-faint">اعلان جدیدی ندارید</p>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, onUnmounted } from 'vue'

const store = useNotificationStore()
const panelOpen = ref(false)
const bellRef = ref<HTMLElement | null>(null)

const typeColors: Record<string, string> = {
  info:    'bg-brand',
  success: 'bg-ok',
  warning: 'bg-amber',
  error:   'bg-rose',
  post:    'bg-teal',
}

function togglePanel() {
  panelOpen.value = !panelOpen.value
}

function handleOutsideClick(e: MouseEvent) {
  if (bellRef.value && !bellRef.value.contains(e.target as Node)) {
    panelOpen.value = false
  }
}

onMounted(() => document.addEventListener('click', handleOutsideClick, { passive: true }))
onUnmounted(() => document.removeEventListener('click', handleOutsideClick))
</script>

<style scoped>
.notif-item-enter-active { transition: all 0.25s ease; }
.notif-item-leave-active { transition: all 0.2s ease; }
.notif-item-enter-from  { opacity: 0; transform: translateX(8px); }
.notif-item-leave-to    { opacity: 0; transform: translateX(8px); }
</style>
