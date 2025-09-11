<template>
  <div class="fixed z-50 left-3 bottom-3 md:left-6 md:bottom-6 select-none">
    <div class="relative">
      <div
        v-show="visible"
        class="strip-shell absolute top-1/2 z-0 left-[calc(3rem+10px)] md:left-[calc(3.5rem+10px)]
               h-12 md:h-14
               w-[clamp(180px,calc(100vw-112px),260px)]
               md:w-[clamp(240px,calc(100vw-120px),360px)]"
        :class="{
          'is-open': open && !closing,
          'is-closing': closing,
          'shadow-[0_20px_50px_rgba(0,0,0,0.45)]': open && !closing
        }"
        role="menu"
        aria-label="منوی کشویی"
        @animationend="onAnimEnd"
      >
        <div class="h-full w-full bg-[rgba(12,16,24,0.92)] text-white/90 shadow-2xl rounded-full overflow-hidden backdrop-blur-[2px]">
          <div dir="ltr" class="h-full grid items-stretch gap-0 divide-x divide-white/10" :style="{ gridTemplateColumns: 'repeat(3, 1fr)' }">
            <component
              :is="linkTag" :to="isNuxt ? '/about' : undefined" :href="!isNuxt ? '/about' : undefined"
              class="menu-item px-3 md:px-5 flex items-center justify-center hover:bg-blue-600 active:bg-blue-700 hover:text-white active:text-white transition-transform duration-300 ease-[cubic-bezier(.2,.8,.2,1)]"
              role="menuitem" aria-label="درباره من" @click="closeWithAnim"
            >
              <span class="sr-only">درباره من</span>
              <UserIcon class="w-5 h-5 md:w-6 md:h-6 opacity-95" />
            </component>

            <component
              :is="linkTag" :to="isNuxt ? '/gallery' : undefined" :href="!isNuxt ? '/gallery' : undefined"
              class="menu-item px-3 md:px-5 flex items-center justify-center hover:bg-blue-600 active:bg-blue-700 hover:text-white active:text-white transition-transform duration-300 ease-[cubic-bezier(.2,.8,.2,1)]"
              role="menuitem" aria-label="گالری" @click="closeWithAnim"
            >
              <span class="sr-only">گالری</span>
              <GalleryIcon class="w-5 h-5 md:w-6 md:h-6 opacity-95" />
            </component>

            <component
              :is="linkTag" :to="isNuxt ? '/' : undefined" :href="!isNuxt ? '/' : undefined"
              class="menu-item px-3 md:px-5 flex items-center justify-center hover:bg-blue-600 active:bg-blue-700 hover:text-white active:text-white transition-transform duration-300 ease-[cubic-bezier(.2,.8,.2,1)]"
              role="menuitem" aria-label="خانه" @click="closeWithAnim"
            >
              <span class="sr-only">خانه</span>
              <HomeIcon class="w-5 h-5 md:w-6 md:h-6 opacity-95" />
            </component>
          </div>
        </div>
      </div>

      <button
        ref="triggerRef"
        class="relative z-10 w-12 h-12 md:w-14 md:h-14 grid place-items-center rounded-full text-white shadow-2xl cursor-pointer transition-colors duration-200 ease-[cubic-bezier(.2,.8,.2,1)] overflow-visible outline-none focus:outline-none"
        :class="open ? 'bg-blue-600 hover:bg-blue-700' : 'bg-black/90 hover:bg-black'"
        :aria-expanded="open ? 'true' : 'false'"
        :aria-label="open ? 'بستن منو' : 'باز کردن منو'"
        :disabled="animating"
        @click="toggle"
      >
        <BarsIcon v-if="!open" class="w-6 h-6" />
        <CloseIcon v-else class="w-6 h-6" />
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, h, resolveComponent } from 'vue'

const open = ref(false)
const visible = ref(false)
const closing = ref(false)
const animating = ref(false)

let maybeNuxt: any = null
try { maybeNuxt = resolveComponent('NuxtLink') } catch (_) { maybeNuxt = null }
const isNuxt = computed(() => !!maybeNuxt)
const linkTag = computed(() => (maybeNuxt as any) || 'a')

function toggle() {
  if (animating.value) return
  if (!open.value) {
    visible.value = true
    closing.value = false
    animating.value = true
    requestAnimationFrame(() => { open.value = true })
  } else {
    closeWithAnim()
  }
}

function closeWithAnim() {
  if (!visible.value || animating.value) return
  closing.value = true
  open.value = false
  animating.value = true
}

function onAnimEnd(e: AnimationEvent) {
  if (e.animationName === 'revealStrip') {
    closing.value = false
    animating.value = false
  } else if (e.animationName === 'hideStrip') {
    visible.value = false
    closing.value = false
    animating.value = false
  }
}

function BarsIcon(){ return h('svg',{xmlns:'http://www.w3.org/2000/svg',viewBox:'0 0 24 24'},[h('path',{fill:'currentColor',d:'M3 6h18v2H3zM3 11h18v2H3zM3 16h18v2H3z'})]) }
function CloseIcon(){ return h('svg',{xmlns:'http://www.w3.org/2000/svg',viewBox:'0 0 24 24'},[h('path',{d:'M6 6L18 18M18 6L6 18',stroke:'currentColor','stroke-width':'2.4','stroke-linecap':'round'})]) }
function HomeIcon(){ return h('svg',{xmlns:'http://www.w3.org/2000/svg',viewBox:'0 0 24 24'},[h('path',{fill:'currentColor',d:'M12 3l8 7v11h-5v-6H9v6H4V10l8-7z'})]) }
function GalleryIcon(){ return h('svg',{xmlns:'http://www.w3.org/2000/svg',viewBox:'0 0 24 24'},[
  h('rect',{x:'4',y:'6',width:'16',height:'12',rx:'2',fill:'none',stroke:'currentColor','stroke-width':'2'}),
  h('circle',{cx:'9',cy:'10',r:'1.4',fill:'currentColor'}),
  h('path',{d:'M7 16l3.2-3.2a1 1 0 0 1 1.4 0L14 15l2-2 3 3',fill:'none',stroke:'currentColor','stroke-width':'2','stroke-linecap':'round','stroke-linejoin':'round'})
]) }
function UserIcon(){ return h('svg',{xmlns:'http://www.w3.org/2000/svg',viewBox:'0 0 24 24'},[h('path',{fill:'currentColor',d:'M12 12a4.2 4.2 0 1 0-4.2-4.2A4.2 4.2 0 0 0 12 12zm0 2.2c-4.8 0-8.8 2.4-8.8 5.4V21h17.6v-1.4c0-3-4-5.4-8.8-5.4z'})]) }
</script>

<style scoped>
.strip-shell {
  transform: translateY(-50%);
  will-change: clip-path, transform, opacity;
  clip-path: inset(0 100% 0 0 round 9999px);
}
.strip-shell.is-open { animation: revealStrip 420ms cubic-bezier(.16,.84,.24,1) forwards; }
.strip-shell.is-closing { animation: hideStrip 360ms cubic-bezier(.2,.8,.2,1) forwards; }

@keyframes revealStrip {
  from { clip-path: inset(0 100% 0 0 round 9999px); filter: blur(0.8px); opacity: .0; }
  60%  { filter: blur(0.25px); }
  to   { clip-path: inset(0 0 0 0 round 9999px); filter: blur(0); opacity: 1; }
}
@keyframes hideStrip {
  from { clip-path: inset(0 0 0 0 round 9999px); filter: blur(0); opacity: 1; }
  to   { clip-path: inset(0 100% 0 0 round 9999px); filter: blur(.35px); opacity: .98; }
}

.menu-item { opacity: 0; transform: translateY(6px) scale(.96); }
.is-open .menu-item { animation: itemIn 280ms cubic-bezier(.2,.8,.2,1) forwards; }
.is-open .menu-item:nth-child(1) { animation-delay: 80ms; }
.is-open .menu-item:nth-child(2) { animation-delay: 140ms; }
.is-open .menu-item:nth-child(3) { animation-delay: 200ms; }

.is-closing .menu-item { animation: itemOut 220ms cubic-bezier(.2,.8,.2,1) forwards; }
.is-closing .menu-item:nth-child(3) { animation-delay: 0ms; }
.is-closing .menu-item:nth-child(2) { animation-delay: 50ms; }
.is-closing .menu-item:nth-child(1) { animation-delay: 100ms; }

@keyframes itemIn  { to { opacity: 1; transform: translateY(0) scale(1); } }
@keyframes itemOut { to { opacity: 0; transform: translateY(6px) scale(.96); } }
</style>
