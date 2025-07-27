export function generateSeoMeta({
  title,
  description,
  image,
  url,
  keywords = [],
  author = 'Your Brand',
  type = 'website'
}: {
  title: string
  description: string
  image: string
  url: string
  keywords?: string[]
  author?: string
  type?: 'website' | 'article' | 'product' | string
}) {
  return {
    title,
    meta: [
      { name: 'description', content: description },
      { name: 'keywords', content: keywords.join(', ') },
      { name: 'author', content: author },
      { property: 'og:type', content: type },
      { property: 'og:title', content: title },
      { property: 'og:description', content: description },
      { property: 'og:image', content: image },
      { property: 'og:url', content: url },
      { name: 'twitter:card', content: 'summary_large_image' },
      { name: 'twitter:title', content: title },
      { name: 'twitter:description', content: description },
      { name: 'twitter:image', content: image }
    ],
    link: [
      { rel: 'canonical', href: url }
    ]
  }
}