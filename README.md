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

## 🐍 Backend – Django Project Structure
```
Django/
├── BlogDjango/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── Contact/
├── Post/
├── Setting/
│ ├── migrations/
│ │ └── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── media/
├── static/
├── staticfiles/
├── templates/
├── venv/ # virtual environment folder (optional)
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## 🌐 Frontend – Nuxt 4 Project Structure
```
NUXTJS/
├── .nuxt/
├── .output/
├── app/
│ ├── assets/
│ ├── components/
│ ├── composable/
│ ├── layouts/
│ ├── middleware/
│ ├── models/
│ ├── pages/
│ ├── plugins/
│ ├── services/
│ ├── stores/
│ ├── utilities/
│ ├── app.vue
│ ├── error.vue
│ └── service-worker.js
├── node_modules/
├── public/
├── .env
├── .gitignore
├── nuxt.config.ts
├── package-lock.json
├── package.json
└── tsconfig.json
```

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
