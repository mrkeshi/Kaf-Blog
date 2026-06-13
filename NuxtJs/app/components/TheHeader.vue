<template>
  <header
    v-if="title"
    role="banner"
    class="sticky top-0 z-50 border-b border-line bg-base/80 backdrop-blur-xl backdrop-saturate-150 transition-colors duration-300"
  >
    <div class="mx-auto flex h-16 w-full max-w-[1440px] items-center justify-between gap-4 px-4 md:h-[68px] md:px-6 lg:px-8">

      <div class="flex min-w-0 flex-col gap-0.5">
        <NuxtLink :to="{ name: 'index' }" class="group flex items-center gap-2.5 text-lg font-extrabold text-ink transition-colors duration-200 hover:text-brand md:text-xl" aria-label="برگشت به خانه">
          <span class="h-2 w-2 shrink-0 rounded-full bg-brand shadow-[0_0_12px_var(--color-brand)] transition-transform duration-300 group-hover:scale-125" aria-hidden="true"></span>
          <span class="truncate">{{ title }}</span>
        </NuxtLink>
        <p class="hidden truncate text-xs text-ink-faint sm:block">{{ description }}</p>
      </div>

      <div class="flex shrink-0 items-center gap-2">

        <div
          v-if="count > 0"
          class="hidden items-center gap-1.5 rounded-full border border-line bg-card-soft px-3.5 py-1.5 text-xs font-semibold text-ink-soft sm:flex"
          :aria-label="`${count} دنبال‌کننده`"
        >
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" class="text-brand" aria-hidden="true">
            <path d="M16.04 7.81C17.2 8.65 18 9.77 18 11.25V13H22V11.25C22 9.23 18.5 8.08 16.04 7.81ZM15 6C16.93 6 18.5 4.43 18.5 2.5C18.5 0.57 16.93-1 15-1C14.46-1 13.96-.87 13.5-.65C14.13.24 14.5 1.33 14.5 2.5C14.5 3.67 14.13 4.76 13.5 5.65C13.96 5.87 14.46 6 15 6ZM9 6C10.93 6 12.5 4.43 12.5 2.5C12.5.57 10.93-1 9-1C7.07-1 5.5.57 5.5 2.5C5.5 4.43 7.07 6 9 6ZM9 7.75C6.66 7.75 2 8.92 2 11.25V13H16V11.25C16 8.92 11.34 7.75 9 7.75Z" />
          </svg>
          <span v-persian-number="count"></span>
          <span>دنبال‌کننده</span>
        </div>

        <button
          @click="ui.openSearch"
          class="flex h-10 w-10 items-center justify-center rounded-xl border border-line bg-card-soft text-ink-soft transition-all duration-200 hover:border-brand/40 hover:text-brand"
          aria-label="جستجو"
          title="جستجو (Ctrl+K)"
        >
          <svg width="18" height="18" viewBox="0 0 23 23" fill="currentColor" aria-hidden="true">
            <path d="M16.375 14.5H15.3875L15.0375 14.1625C16.2625 12.7375 17 10.8875 17 8.875C17 4.3875 13.3625.75 8.875.75C4.3875.75.75 4.3875.75 8.875C.75 13.3625 4.3875 17 8.875 17C10.8875 17 12.7375 16.2625 14.1625 15.0375L14.5 15.3875V16.375L20.75 22.6125L22.6125 20.75L16.375 14.5ZM8.875 14.5C5.7625 14.5 3.25 11.9875 3.25 8.875C3.25 5.7625 5.7625 3.25 8.875 3.25C11.9875 3.25 14.5 5.7625 14.5 8.875C14.5 11.9875 11.9875 14.5 8.875 14.5Z" />
          </svg>
        </button>

        <button
          @click="toggleTheme"
          class="flex h-10 w-10 items-center justify-center rounded-xl border border-line bg-card-soft text-ink-soft transition-all duration-200 hover:border-brand/40 hover:text-brand"
          :aria-label="isDark ? 'تغییر به حالت روشن' : 'تغییر به حالت تاریک'"
          :title="isDark ? 'حالت روشن' : 'حالت تاریک'"
        >
          <svg v-if="isDark" width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M12 7C9.24 7 7 9.24 7 12s2.24 5 5 5 5-2.24 5-5-2.24-5-5-5zM2 13h2c.55 0 1-.45 1-1s-.45-1-1-1H2c-.55 0-1 .45-1 1s.45 1 1 1zm18 0h2c.55 0 1-.45 1-1s-.45-1-1-1h-2c-.55 0-1 .45-1 1s.45 1 1 1zM11 2v2c0 .55.45 1 1 1s1-.45 1-1V2c0-.55-.45-1-1-1s-1 .45-1 1zm0 18v2c0 .55.45 1 1 1s1-.45 1-1v-2c0-.55-.45-1-1-1s-1 .45-1 1zM5.99 4.58a.996.996 0 00-1.41 0 .996.996 0 000 1.41l1.06 1.06c.39.39 1.03.39 1.41 0s.39-1.03 0-1.41L5.99 4.58zm12.37 12.37a.996.996 0 00-1.41 0 .996.996 0 000 1.41l1.06 1.06c.39.39 1.03.39 1.41 0 .39-.39.39-1.03 0-1.41l-1.06-1.06zm1.06-12.37l-1.06 1.06c-.39.39-.39 1.03 0 1.41s1.03.39 1.41 0l1.06-1.06c.39-.39.39-1.03 0-1.41s-1.03-.39-1.41 0zM7.05 18.36l-1.06 1.06c-.39.39-.39 1.03 0 1.41s1.03.39 1.41 0l1.06-1.06c.39-.39.39-1.03 0-1.41s-1.03-.39-1.41 0z" />
          </svg>
          <svg v-else width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M12 3a9 9 0 109 9c0-.46-.04-.92-.1-1.36a5.389 5.389 0 01-4.4 2.26 5.403 5.403 0 01-3.14-9.8c-.44-.06-.9-.1-1.36-.1z" />
          </svg>
        </button>

        <search-bar />
      </div>
    </div>

    <div
      v-show="ui.isSearchOpen || ui.isSearchClosing"
      :class="[
        'border-t border-line bg-base/95 px-4 py-4 backdrop-blur-xl md:px-6',
        ui.isSearchClosing ? 'animate-slide-up' : 'animate-slide-down'
      ]"
      role="search"
    >
      <div class="mx-auto flex max-w-2xl items-center gap-2.5">
        <input
          v-model="ui.searchQuery"
          @keydown.enter="submitSearch"
          @keydown.escape="ui.closeSearch"
          type="search"
          placeholder="جستجو در مطالب..."
          autocomplete="off"
          aria-label="جستجو"
          ref="searchInputRef"
          class="flex-1 rounded-2xl border border-line bg-card-soft px-4 py-3 text-base text-ink outline-none transition-all duration-200 placeholder:text-ink-faint focus:border-brand focus:ring-4 focus:ring-brand/15"
        />
        <button
          @click="submitSearch"
          class="shrink-0 rounded-full bg-gradient-to-tr from-brand-strong to-brand px-5 py-2.5 text-sm font-bold text-white shadow-glow transition-transform duration-200 hover:-translate-y-0.5"
        >
          جستجو
        </button>
        <button
          @click="ui.closeSearch"
          class="shrink-0 rounded-full border border-line px-5 py-2.5 text-sm font-bold text-ink-soft transition-colors duration-200 hover:bg-card-soft"
        >
          بستن
        </button>
      </div>
    </div>
  </header>
</template>

<script lang="ts" setup>
import { ref, watch, nextTick, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUIStore } from '~/stores/useUIStore'

const props = defineProps({
  icon: { type: String, default: '' },
  title: { type: String, default: 'کافه بیگانه' },
  description: { type: String, default: 'نوشته‌های یک کافه‌بیگانه' },
  count: { type: Number, default: 0 }
})

const ui = useUIStore()
const router = useRouter()
const searchInputRef = ref<HTMLInputElement | null>(null)
const isDark = ref(true)

onMounted(() => {
  const saved = localStorage.getItem('theme')
  isDark.value = saved ? saved === 'dark' : true
  applyTheme(isDark.value)
})

function applyTheme(dark: boolean) {
  document.documentElement.setAttribute('data-theme', dark ? 'dark' : 'light')
}

function toggleTheme() {
  isDark.value = !isDark.value
  applyTheme(isDark.value)
  localStorage.setItem('theme', isDark.value ? 'dark' : 'light')
}

watch(() => ui.isSearchOpen, (open) => {
  if (open) nextTick(() => searchInputRef.value?.focus())
})

function submitSearch() {
  const q = ui.searchQuery.trim()
  if (q) {
    router.push({ name: 'search', query: { q } })
    ui.closeSearch()
  }
}

function handleKeydown(e: KeyboardEvent) {
  if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
    e.preventDefault()
    ui.openSearch()
  }
}

onMounted(() => window.addEventListener('keydown', handleKeydown))
onUnmounted(() => window.removeEventListener('keydown', handleKeydown))

useHead(() => ({
  link: [{ rel: 'icon', type: 'image/png', sizes: '64x64', href: props.icon || '/images/l192.png' }]
}))
</script>
