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
