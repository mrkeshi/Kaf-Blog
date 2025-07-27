# 📰 Blog Platform – Django + Nuxt 4

A modern, full-featured blog platform built with **Django REST Framework** on the backend and **Nuxt 4 (Vue 3 + TypeScript)** on the frontend.  
Optimized for **SEO**, **performance**, and **user experience** with full **SSR** support and **push notifications** for new posts.

---

## 🚀 Features
- ✅ Django REST API backend  
- ✅ Post, Comment, Tag, and Category models  
- ✅ Site-wide SEO and dynamic meta tags  
- ✅ Site settings API  
- ✅ Unsuccessful login logging  
- ✅ Built-in Django Admin panel for managing content and settings  
- ✅ Nuxt 4 frontend with Vue 3 Composition API  
- ✅ Tailwind CSS and TypeScript support  
- ✅ Server-Side Rendering (SSR)  
- ✅ Push Notification support for new posts  
- ✅ Modular, clean, and scalable codebase  



<pre lang="markdown"><code> ## 🐍 Backend – Django Project Structure ``` Django/ ├── your_app/ │ ├── models.py │ ├── views.py │ ├── serializers.py │ └── urls.py ├── core/ │ ├── models.py # site settings, login logs, etc. │ └── admin.py ├── utilities.py ├── settings/ │ ├── base.py │ ├── dev.py │ └── prod.py ├── manage.py └── requirements.txt ``` ## 🌐 Frontend – Nuxt 4 Project Structure ``` NuxtApp/ ├── assets/ # Static assets like fonts and images ├── components/ # UI components (PostCard, CommentBox, etc.) ├── composables/ # Vue composables (e.g., useSeo, usePush) ├── layouts/ # Default, error, and custom layouts ├── middleware/ # Auth guards and route middleware ├── pages/ # Nuxt pages (index.vue, post/[slug].vue, tag/[slug].vue) ├── plugins/ # Nuxt plugins (e.g. push notification setup) ├── public/ # Static public files (manifest, icons) ├── stores/ # Pinia stores (auth, settings, etc.) ├── models/ # TypeScript interfaces and types ├── utils/ # Helper functions (SEO generation, formatting) ├── nuxt.config.ts # Nuxt configuration └── package.json ``` </code></pre>

## 📦 Setup Instructions (Optional)

> You can add a step-by-step guide here for how to run the backend and frontend if needed.



## 📬 Push Notifications

This project supports push notifications for new blog posts.  
When a user allows notifications, they will receive real-time updates whenever new content is published.


## 📌 SEO Optimization

Dynamic SEO meta tags are generated for all important pages including:
- Home  
- Tags  
- Categories  
- Post details  
- Search results  
- Contact/About pages  
Structured data (`schema.org`) is also included for rich results and better search engine visibility.

## 📄 License

MIT – Free to use, modify, and distribute.
