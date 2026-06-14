<template>
  <div class="fixed bottom-5 left-5 z-40 flex items-center gap-2.5">
    <div
      v-show="visible"
      role="menu"
      aria-label="منوی کشویی"
      class="origin-left"
      :class="closing ? 'animate-slide-up' : open ? 'animate-fade-in' : ''"
      @animationend="onAnimEnd"
    >
      <div class="flex overflow-hidden rounded-full border border-line bg-card/90 shadow-pop backdrop-blur-xl">
        <NuxtLink
          to="/"
          role="menuitem"
          aria-label="خانه"
          @click="closeWithAnim"
          class="flex items-center justify-center px-5 py-3 text-ink-soft transition-colors duration-200 hover:bg-brand/10 hover:text-brand"
        >
          <!-- Home – brand color on hover, otherwise muted -->
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z" />
          </svg>
        </NuxtLink>

        <div class="w-px self-stretch bg-line" aria-hidden="true"></div>

        <NuxtLink
          to="/gallery"
          role="menuitem"
          aria-label="گالری"
          @click="closeWithAnim"
          class="flex items-center justify-center px-5 py-3 text-ink-soft transition-colors duration-200 hover:bg-teal/10 hover:text-teal"
        >
          <!-- Gallery – teal accent -->
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M21 3H3c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM5 17l3.5-4.5 2.5 3.01L14.5 11l4.5 6H5z" />
          </svg>
        </NuxtLink>

        <div class="w-px self-stretch bg-line" aria-hidden="true"></div>

        <NuxtLink
          to="/about"
          role="menuitem"
          aria-label="درباره من"
          @click="closeWithAnim"
          class="flex items-center justify-center px-5 py-3 text-ink-soft transition-colors duration-200 hover:bg-rose/10 hover:text-rose"
        >
          <!-- About – rose accent -->
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
          </svg>
        </NuxtLink>
      </div>
    </div>

    <button
      @click="toggleMenu"
      :aria-expanded="open"
      aria-label="منوی سریع"
      class="flex h-13 w-13 shrink-0 items-center justify-center rounded-full bg-gradient-to-tr from-brand-strong to-brand text-white shadow-glow transition-transform duration-300 hover:scale-105 animate-glow-pulse"
    >
      <svg v-if="!open" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true">
        <path d="M3 12h18M3 6h18M3 18h18" stroke-linecap="round" />
      </svg>
      <svg v-else width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true">
        <path d="M6 6l12 12M18 6L6 18" stroke-linecap="round" />
      </svg>
    </button>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const open    = ref(false)
const visible = ref(false)
const closing = ref(false)

function toggleMenu() {
  if (open.value) {
    closeWithAnim()
  } else {
    open.value    = true
    visible.value = true
    closing.value = false
  }
}

function closeWithAnim() {
  closing.value = true
  open.value    = false
}

function onAnimEnd() {
  if (closing.value) {
    visible.value = false
    closing.value = false
  }
}
</script>
