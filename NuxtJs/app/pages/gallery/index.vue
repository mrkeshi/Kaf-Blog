<template>
  <div class="min-h-screen font-mahoor">
    <div class="w-full text-center pt-28 md:pt-32 pb-8 px-4 md:px-8">
      <h1 class="text-2xl md:text-4xl font-extrabold tracking-tight mb-6 text-black-500">گالری جذاب ما</h1>
      <div class="w-28 h-[3px] mx-auto mb-4 bg-blue-500"></div>
      <p class="text-md md:text-lg text-black-300 leading-relaxed">در این قسمت شما میتونید عکس‌های ارسالی توسط خودم و کاربران رو مشاهده کنید.</p>
      <p v-if="page > 1" class="text-sm text-black-300 mt-1">صفحه ({{ page }})</p>
      <div class="flex justify-center mt-8">
        <NuxtLink
          :to="{ name: 'gallery-send' }"
          class="flex items-center justify-center gap-2 px-6 py-2 bg-blue-500 text-white font-semibold text-lg max-md:text-base border-2 border-blue-500 transition-all duration-300 hover:bg-transparent hover:text-blue-500 rounded-full"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 md:w-7 md:h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M4 16v2a2 2 0 002 2h12a2 2 0 002-2v-2M16 12l-4-4m0 0l-4 4m4-4v12" />
          </svg>
          <span class="leading-none">ارسال عکس</span>
        </NuxtLink>
      </div>
      <div class="w-full mt-8 px-4 md:px-8">
        <div class="h-[1px] w-full bg-gradient-to-r from-transparent via-black/20 to-transparent"></div>
      </div>
    </div>

    <div class="w-full px-3 sm:px-4 md:px-6 lg:px-8">
      <div v-if="pending || isPageChanging" class="masonry-cols" :style="{'--gap': gapCss, '--cols': cols}">
        <div v-for="i in pageSize" :key="'sk-'+i" class="card">
          <SkeletonSimple class="w-full h-[240px]" />
        </div>
      </div>

      <div v-else>
        <div v-if="!items.length" class="text-center py-16 text-black-300">فعلاً عکسی موجود نیست.</div>

        <div v-else ref="wrapRef" class="masonry-cols" :style="{'--gap': gapCss, '--cols': cols}">
          <div
            v-for="(item, idx) in items"
            :key="item.id + '-' + page"
            class="card"
            :aria-busy="!loaded[idx]"
            @click="openLightbox(idx)"
          >
            <div v-if="!loaded[idx]" class="abs">
              <SkeletonSimple class="w-full h-full" />
            </div>

            <img
              :src="item.photo"
              :alt="`عکس گالری ${item.location ?? ''}`"
              class="img"
              :class="loaded[idx] ? 'opacity-100' : 'opacity-0'"
              loading="lazy"
              decoding="async"
              draggable="false"
              v-ready-img="idx"
            />

            <div class="grad"></div>

            <div class="meta">
              <span v-if="item.location" class="meta-txt">
                <svg xmlns="http://www.w3.org/2000/svg" class="meta-ic" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                  <path d="M12 2.25c-4.28 0-7.75 3.47-7.75 7.75 0 5.32 6.53 10.79 7.06 11.22.4.33.98.33 1.38 0 .53-.43 7.06-5.9 7.06-11.22 0-4.28-3.47-7.75-7.75-7.75zm0 10.5a2.75 2.75 0 110-5.5 2.75 2.75 0 010 5.5z"/>
                </svg>
                {{ item.location }}
              </span>
            </div>
          </div>
        </div>
      </div>

      <div v-if="totalPages > 1" class="flex items-center justify-center gap-3 mt-12">
        <button class="px-3 py-1.5 border border-black-100 text-black-500 disabled:opacity-40"
                :disabled="page <= 1 || pending || isPageChanging"
                @click="goTo(page - 1)">قبلی</button>
        <span class="text-black-500 text-sm">صفحه {{ page }} از {{ totalPages }}</span>
        <button class="px-3 py-1.5 border border-black-100 text-black-500 disabled:opacity-40"
                :disabled="page >= totalPages || pending || isPageChanging"
                @click="goTo(page + 1)">بعدی</button>
      </div>
    </div>

    <transition name="fade">
      <div v-if="lightbox.open"
           class="fixed inset-0 z-50 bg-black/90 backdrop-blur-sm flex flex-col items-center justify-center"
           @click.self="closeLightbox"
           @keydown.esc="closeLightbox"
           tabindex="0">
        <div class="max-w-[96vw] max-h-[86vh] flex items-center justify-center">
          <img :src="items[lightbox.index]?.photo"
               :alt="`پیش‌نمایش ${items[lightbox.index]?.location ?? ''}`"
               class="object-contain select-none touch-none max-w-full max-h-[86vh]"
               draggable="false" />
        </div>
        <div class="mt-3 text-white text-xs md:text-sm">
          ارسال‌شده توسط: <span class="font-semibold">{{ items[lightbox.index]?.sender_name || 'نامشخص' }}</span>
        </div>
      </div>
    </transition>
  </div>
</template>

<script lang="ts" setup>
import { NuxtLink } from '#components'
import { getImageDataService } from '~/services/Gallery.service'
import { generateSeoMeta } from '~/utilities/seo'
import type { GalleryResponseDTO, GalleryItemDTO } from '~/models/Gallery/SendGalleryDTO'
import type { Directive } from 'vue'

definePageMeta({ layout: 'simple-layout' })

const route = useRoute()
const router = useRouter()
const setting = useMySettingDataStore()

const pageSize = 20
const page = ref<number>(Number(route.query.page ?? 1) || 1)
const isPageChanging = ref(false)

watchEffect(() => {
  if (!setting.siteSettingData) return
  const suffix = page.value > 1 ? ` (صفحه ${page.value})` : ''
  const pageUrl = `${setting.siteSettingData.site_url}${route.path}${page.value > 1 ? `?page=${page.value}` : ''}`
  const seo = generateSeoMeta({
    title: `${setting.siteSettingData.site_name} - گالری من${suffix}`,
    description: 'در این صفحه گالری و تصاویر ارسالی از من و کاربران رو مشاهده می کنید',
    image: setting.siteSettingData.site_logo || setting.siteSettingData.site_icon,
    url: pageUrl,
    keywords: ['گالری آقای کاف', 'گالری ما', `${setting.siteSettingData.site_name}`, 'گالری من'],
    author: setting.siteSettingData.meta_author,
    type: 'about'
  })
  useHead({ ...seo, link: [{ rel: 'canonical', href: pageUrl }] })
})

watch(page, (p) => { router.push({ query: p > 1 ? { ...route.query, page: p } : {} }) })
watch(() => route.query.page, (qp) => {
  const num = Number(qp ?? 1) || 1
  if (num !== page.value) page.value = num
})

const nuxt = useNuxtApp()
const asyncKey = computed(() => `gallery-${route.path}-${page.value}`)
const { data, pending } = await useAsyncData(
  asyncKey.value,
  () => getImageDataService(page.value, pageSize),
  {
    server: true,
    watch: [page],
    default: () => ({ count: 0, next: null, previous: null, results: [] } as GalleryResponseDTO),
    getCachedData: k => nuxt.payload.static?.[k] ?? nuxt.payload.data?.[k]
  }
)

const response = computed<GalleryResponseDTO>(() => {
  const v: any = data.value
  if (!v) return { count: 0, next: null, previous: null, results: [] }
  return (v.results || v.count !== undefined) ? (v as GalleryResponseDTO) : (v.data as GalleryResponseDTO)
})

function parseItemDate(it: any): number {
  const raw = it?.created_at || it?.createdAt || it?.updated_at || it?.date || null
  const t = raw ? new Date(raw).getTime() : NaN
  if (!Number.isNaN(t)) return t
  const asNum = typeof it?.id === 'number' ? it.id : Number(it?.id)
  return Number.isFinite(asNum) ? asNum : 0
}
const items = computed<GalleryItemDTO[]>(() => {
  const list = (response.value?.results ?? []).slice()
  return list.sort((a, b) => parseItemDate(b) - parseItemDate(a))
})

const totalCount = computed(() => response.value?.count ?? 0)
const totalPages = computed(() => Math.max(1, Math.ceil(totalCount.value / pageSize)))

const wrapRef = ref<HTMLElement | null>(null)
const loaded = ref<boolean[]>([])

const cols = computed(() => {
  const w = wrapRef.value?.clientWidth || 0
  if (w < 640) return 2
  if (w < 900) return 3
  if (w < 1280) return 4
  return 5
})
const gapCss = computed(() => ((wrapRef.value?.clientWidth || 0) < 640 ? '8px' : '12px'))

const vReadyImg: Directive<HTMLImageElement, number> = {
  mounted(el, binding) {
    const idx = binding.value
    const done = () => { loaded.value[idx] = true }
    if (el.complete && el.naturalWidth > 0) done()
    else {
      el.addEventListener('load', done, { once: true })
      el.addEventListener('error', done, { once: true })
      // @ts-ignore
      if ('decode' in el) el.decode().then(done).catch(done)
    }
  },
  updated(el, binding) {
    if (el.complete && el.naturalWidth > 0) loaded.value[binding.value] = true
  }
}

watch(items, (arr) => {
  loaded.value = new Array(arr.length).fill(false)
  isPageChanging.value = false
})

async function goTo(p: number) {
  if (p < 1 || p > totalPages.value) return
  isPageChanging.value = true
  page.value = p
}

const lightbox = reactive({ open: false, index: 0 })
function openLightbox(idx: number) {
  lightbox.open = true
  lightbox.index = idx
  nextTick(() => {
    const overlay = document.querySelector('[tabindex="0"]') as HTMLElement | null
    overlay?.focus()
  })
}
function closeLightbox() { lightbox.open = false }
</script>

<style>
.fade-enter-active, .fade-leave-active { transition: opacity .18s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

.masonry-cols{
  column-gap: var(--gap, 12px);
  column-count: var(--cols, 4);
  column-fill: balance;
}
@media (max-width: 640px){
  .masonry-cols{ column-gap: 8px; }
}

.card{
  display: inline-block;
  width: 100%;
  margin: 0 0 calc(var(--gap,12px) * 0.6);
  position: relative;
  break-inside: avoid;
  overflow: hidden;
  background: transparent;
  box-shadow: 0 8px 22px rgba(0,0,0,.10);
  transition: transform .18s ease, box-shadow .18s ease, filter .18s ease, opacity .2s ease;
  cursor: pointer;
  will-change: transform;
}
.card:hover{
  transform: translateY(-3px) scale(1.01);
  box-shadow: 0 16px 36px rgba(0,0,0,.18);
}

.img{
  display:block;
  width:100%;
  height:100%;
  object-fit:cover;
  transition: transform .25s ease, opacity .25s ease;
}
.card:hover .img{ transform: scale(1.03); }

.abs{ position:absolute; inset:0; }

.grad{
  position: absolute;
  inset-inline: 0;
  bottom: 0;
  height: 38%;
  background: linear-gradient(to top, rgba(0,0,0,.55), rgba(0,0,0,.35) 40%, rgba(0,0,0,0) 100%);
  pointer-events: none;
}

.meta{
  position: absolute;
  right: 0;
  bottom: 0;
  padding: .5rem .6rem;
  display: flex;
  align-items: center;
  gap: .35rem;
  direction: rtl;
}
.meta-txt{
  color: #fff;
  font-weight: 500;
  font-size: clamp(10px, .8vw, 13px);
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  white-space: normal;
  overflow: visible;
}
.meta-ic{
  width: 15px;
  height: 15px;
  color: #fff;
  flex: 0 0 auto;
}

@media (prefers-reduced-motion: reduce){
  .card, .img{ transition:none }
  .card:hover{ transform:none }
}
</style>
