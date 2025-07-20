export default defineNuxtPlugin((nuxtApp) => {
  const enToFaMap: { [key: string]: string } = {
    '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
    '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'
  }

  function convertToPersian(input: string | number): string {
    return input.toString().replace(/[0-9]/g, d => enToFaMap[d] ?? d)
  }

  nuxtApp.vueApp.directive('persian-number', {
    mounted(el, binding) {
      el.textContent = convertToPersian(binding.value)
    },
    updated(el, binding) {
      el.textContent = convertToPersian(binding.value)
    }
  })
})
