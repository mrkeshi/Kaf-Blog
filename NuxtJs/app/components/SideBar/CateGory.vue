<template>
  <div v-if="data?.length" class="rounded-3xl border border-line bg-card p-6 shadow-card">
    <div class="mb-4 flex items-center gap-2.5 border-b border-line pb-4 text-base font-extrabold text-ink">
      <span class="h-5 w-[3px] shrink-0 rounded-full bg-brand" aria-hidden="true"></span>
      <!-- Category shapes icon – colored brand -->
      <svg width="18" height="18" viewBox="0 0 37 37" fill="currentColor" class="text-brand" aria-hidden="true">
        <path d="M18.4999 3.08337L10.0208 16.9584H26.9791L18.4999 3.08337Z" />
        <path d="M26.9792 33.9166C30.8107 33.9166 33.9167 30.8106 33.9167 26.9791C33.9167 23.1477 30.8107 20.0416 26.9792 20.0416C23.1478 20.0416 20.0417 23.1477 20.0417 26.9791C20.0417 30.8106 23.1478 33.9166 26.9792 33.9166Z" />
        <path d="M4.625 20.8125H16.9583V33.1458H4.625V20.8125Z" />
      </svg>
      <span>دسته‌بندی</span>
    </div>

    <ul role="list" class="flex flex-col gap-1">
      <li
        v-for="(item, idx) in data"
        :key="item.slug"
        role="listitem"
        class="flex items-center justify-between gap-2 border-b border-line-soft py-2 transition-colors duration-200 last:border-b-0 last:pb-0 hover:border-line"
      >
        <NuxtLink
          :to="{ name: 'category-slug', params: { slug: item.slug } }"
          class="flex flex-1 items-center gap-2 text-[15px] font-bold text-ink transition-colors duration-200 hover:text-brand"
        >
          <!-- Colored dot cycle: brand / teal / rose / amber / ok -->
          <span
            class="h-1.5 w-1.5 shrink-0 rounded-full"
            :class="dotColors[idx % dotColors.length]"
            aria-hidden="true"
          ></span>
          {{ item.name }}
        </NuxtLink>
        <NuxtLink
          :to="{ name: 'category-slug', params: { slug: item.slug } }"
          tabindex="-1"
          :aria-label="`${item.post_count} مطلب`"
          class="flex h-7 min-w-7 shrink-0 items-center justify-center rounded-lg border border-line bg-card-soft px-1.5 text-xs font-bold text-ink-soft transition-all duration-200 hover:border-brand/40 hover:bg-brand/10 hover:text-brand"
        >
          <span v-persian-number="item.post_count"></span>
        </NuxtLink>
      </li>
    </ul>
  </div>
</template>

<script lang="ts" setup>
import type { PropType } from 'vue'
import type { CategoryDTO } from '~/models/SideBarData/MetaDataDTO'

defineProps({ data: { type: Object as PropType<CategoryDTO[]> } })

const dotColors = [
  'bg-brand',
  'bg-teal',
  'bg-rose',
  'bg-amber',
  'bg-ok',
]
</script>
