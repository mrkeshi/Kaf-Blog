<template>
  <div v-if="data?.length" class="rounded-3xl border border-line bg-card p-6 shadow-card">
    <div class="mb-4 flex items-center gap-2.5 border-b border-line pb-4 text-base font-extrabold text-ink">
      <span class="h-5 w-[3px] shrink-0 rounded-full bg-teal" aria-hidden="true"></span>
      <svg width="18" height="18" viewBox="0 0 39 39" fill="currentColor" class="text-teal" aria-hidden="true">
        <path d="M6.3375 19.5C6.3375 16.7213 8.59625 14.4625 11.375 14.4625H17.875V11.375H11.375C6.89 11.375 3.25 15.015 3.25 19.5C3.25 23.985 6.89 27.625 11.375 27.625H17.875V24.5375H11.375C8.59625 24.5375 6.3375 22.2787 6.3375 19.5ZM13 21.125H26V17.875H13V21.125ZM27.625 11.375H21.125V14.4625H27.625C30.4037 14.4625 32.6625 16.7213 32.6625 19.5C32.6625 22.2787 30.4037 24.5375 27.625 24.5375H21.125V27.625H27.625C32.11 27.625 35.75 23.985 35.75 19.5C35.75 15.015 32.11 11.375 27.625 11.375Z" />
      </svg>
      <span>پیوندها</span>
    </div>

    <ul role="list" class="flex flex-col gap-1">
      <li v-for="item in data" :key="item.link" role="listitem">
        <a
          :href="item.link"
          rel="nofollow noopener noreferrer"
          target="_blank"
          :aria-label="`${item.title} (لینک خارجی)`"
          class="group flex items-center gap-2.5 rounded-xl px-2.5 py-2 text-sm font-bold text-ink-soft transition-all duration-200 hover:bg-teal/10 hover:text-teal"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" class="shrink-0 text-teal" aria-hidden="true">
            <path d="M12 12C14.21 12 16 10.21 16 8C16 5.79 14.21 4 12 4C9.79 4 8 5.79 8 8C8 10.21 9.79 12 12 12ZM12 14C9.33 14 4 15.34 4 18V20H20V18C20 15.34 14.67 14 12 14Z" />
          </svg>
          <span class="flex-1">{{ item.title }}</span>
          <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="shrink-0 -scale-x-100 opacity-40 transition-opacity duration-200 group-hover:opacity-80" aria-hidden="true">
            <path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6M15 3h6v6M10 14L21 3" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
        </a>
      </li>
    </ul>
  </div>
</template>

<script lang="ts" setup>
import type { PropType } from 'vue'
import type { LinkDTO } from '~/models/SideBarData/MetaDataDTO'

defineProps({ data: { type: Object as PropType<LinkDTO[]> } })
</script>
