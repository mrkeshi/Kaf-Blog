<template>
  <footer role="contentinfo" class="relative mt-20 border-t border-line bg-base-soft px-4 py-10 md:px-6 lg:px-8">
    <div class="mx-auto flex w-full max-w-[1440px] flex-col items-center justify-between gap-4 text-center sm:flex-row sm:text-start">
      <p class="text-sm text-ink-faint">
        © اینا واژه‌ نیستن؛ تکه‌های دلمونه. بردنش آزاده، فراموشیِ اسممون نه.
      </p>

      <nav aria-label="پیمایش پایین صفحه" class="flex items-center gap-1">
        <NuxtLink :to="{ name: 'index' }" class="rounded-lg px-3 py-1.5 text-sm text-ink-soft transition-colors duration-200 hover:bg-brand/10 hover:text-brand">خانه</NuxtLink>
        <span class="text-line" aria-hidden="true">·</span>
        <NuxtLink :to="{ name: 'contact' }" class="rounded-lg px-3 py-1.5 text-sm text-ink-soft transition-colors duration-200 hover:bg-brand/10 hover:text-brand">تماس با من</NuxtLink>
        <span class="text-line" aria-hidden="true">·</span>
        <NuxtLink :to="{ name: 'about' }" class="rounded-lg px-3 py-1.5 text-sm text-ink-soft transition-colors duration-200 hover:bg-brand/10 hover:text-brand">درباره من</NuxtLink>
      </nav>
    </div>

    <div class="mx-auto mt-8 h-px w-full max-w-[1440px] bg-gradient-to-r from-transparent via-brand/40 to-transparent" aria-hidden="true"></div>
  </footer>
</template>

<script lang="ts" setup>
</script>
