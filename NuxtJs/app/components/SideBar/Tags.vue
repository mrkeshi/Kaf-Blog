<template>
  <div v-if="data?.length" class="rounded-3xl border border-line bg-card p-6 shadow-card">
    <div class="mb-4 flex items-center gap-2.5 border-b border-line pb-4 text-base font-extrabold text-ink">
      <span class="h-5 w-[3px] shrink-0 rounded-full bg-brand" aria-hidden="true"></span>
      <svg width="18" height="18" viewBox="0 0 41 41" fill="currentColor" class="text-brand" aria-hidden="true">
        <path d="M34.1666 17.0834V13.6667H27.3333V6.83337H23.9166V13.6667H17.0833V6.83337H13.6666V13.6667H6.83325V17.0834H13.6666V23.9167H6.83325V27.3334H13.6666V34.1667H17.0833V27.3334H23.9166V34.1667H27.3333V27.3334H34.1666V23.9167H27.3333V17.0834H34.1666ZM23.9166 23.9167H17.0833V17.0834H23.9166V23.9167Z" />
      </svg>
      <span>برچسب‌ها</span>
    </div>

    <ul role="list" aria-label="برچسب‌ها" class="flex flex-wrap gap-2">
      <li v-for="item in data" :key="item.slug" role="listitem">
        <NuxtLink
          :to="{ name: 'tag-slug', params: { slug: item.slug } }"
          class="inline-flex items-center rounded-full border border-line bg-card-soft px-3 py-1 text-xs font-bold text-ink-soft transition-all duration-200 hover:border-brand/40 hover:bg-brand/10 hover:text-brand"
        >
          {{ item.name }}
        </NuxtLink>
      </li>
    </ul>
  </div>
</template>

<script lang="ts" setup>
import type { PropType } from 'vue'
import type { TagDTO } from '~/models/SideBarData/MetaDataDTO'

defineProps({ data: { type: Object as PropType<TagDTO[]> } })
</script>
