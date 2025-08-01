import { $fetch, FetchError, type FetchOptions } from "ohmyfetch";
import { type ApiResponse } from "../models/ApiRespose.js";
import { useRuntimeConfig, useCookie } from "nuxt/app";
import { useCustomToastify } from "~/composable/useCustomToastify.js";

const { showError } = useCustomToastify();

export async function Fetch<G>(
  url: string,
  config: FetchOptions<"json"> = {}
): Promise<ApiResponse<G>> {
  const nuxtConfig = useRuntimeConfig();
  const isProduction = nuxtConfig.public.isProduction;

  const method = config.method?.toUpperCase() || "GET";
  const csrfToken = useCookie("csrftoken").value;

  if (
    isProduction &&
    ["POST", "PUT", "PATCH", "DELETE"].includes(method) &&
    csrfToken
  ) {
    config.headers = {
      ...config.headers,
      "X-CSRFToken": csrfToken,
    };
  } else {
    config.headers = {
      ...config.headers,
    };
  }
  if (isProduction) {
    config = {
      ...config,
      baseURL:nuxtConfig.public.baseURL,
      credentials: "include",
    };
  } else {
    config = {
      ...config,
      baseURL:nuxtConfig.public.baseURL,
    };
  }


  
server {
    listen 80;
    server_name penvis.ir www.penvis.ir;

    # ریدایرکت HTTP به HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name penvis.ir www.penvis.ir;

    ssl_certificate /etc/letsencrypt/live/penvis.ir/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/penvis.ir/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    access_log /var/log/nginx/penvis_access.log;
    error_log /var/log/nginx/penvis_error.log;

    # فرانت (Nuxt) — فقط درخواست‌های عادی کلاینت به فرانت
    location / {
        proxy_pass http://127.0.0.1:3000/;  # فرانت روی localhost:3000
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    # پراکسی امن API
    location /proxy/api/ {
        rewrite ^/proxy/api/(.*)$ /$1 break;
        proxy_pass http://127.0.0.1:8001/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # جلوگیری از دسترسی مستقیم به API
    location /api/ {
        deny all;
        return 403;
    }

    # استاتیک و مدیا (اختیاری)
    location /static/ {
        alias /var/www/Kaf-Blog/Django/staticfiles/;
    }

    location /media/ {
        alias /var/www/Kaf-Blog/Django/media/;
    }
}



  return $fetch<ApiResponse<G>>(url, config)
    .then((res) => res)
    .catch((e: FetchError) => {
      // const errorDetail = e.data?.detail || e.message || "خطای نامشخص";
      // showError({
      //   title: "خطا",
      //   message: errorDetail,
      // });
      // console.error(e);
      throw e;
    });
}
