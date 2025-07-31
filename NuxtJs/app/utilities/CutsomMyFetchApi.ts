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
  const method = config.method?.toUpperCase() || "GET";
  const csrfToken = useCookie("csrftoken").value;

  if (["POST", "PUT", "PATCH", "DELETE"].includes(method) && csrfToken) {
    config.headers = {
      ...config.headers,
      "X-CSRFToken": csrfToken,
    };
  }

  config = {
    ...config,
    baseURL: nuxtConfig.public.baseURL, 
    credentials: "include",
  };

  return $fetch<ApiResponse<G>>(url, config)
    .then((res) => res)
    .catch((e: FetchError) => {
      const errorDetail = e.data?.detail || e.message || "خطای نامشخص";
      showError({
        title: "خطا",
        message: errorDetail,
      });
      console.error(e);
      throw e;
    });
}
