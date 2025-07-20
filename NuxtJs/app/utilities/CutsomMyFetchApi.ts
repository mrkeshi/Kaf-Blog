import { $fetch, FetchError, type FetchOptions } from "ohmyfetch";
import { type ApiResponse } from "../models/ApiRespose.js";
import { errorMessages } from "vue/compiler-sfc";
import { useRuntimeConfig } from "nuxt/app";
import { useCustomToastify } from "~/composable/useCustomToastify.js";

const {showError}=useCustomToastify()
export async function Fetch<G>(
  url: string,
  config: FetchOptions<"json"> = {}
): Promise<ApiResponse<G>> {

  const nuxtconfig=useRuntimeConfig()
  config = {
    ...config,
    baseURL: nuxtconfig.public.baseURL
  };

  return $fetch<ApiResponse<G>>(url, config)
    .then((res) => {
      console.log(res,"aaaaaaaa")
         return res
    })
  .catch((e: FetchError) => {
  const errorDetail = e.data?.detail || e.message || 'خطای نامشخص';
  showError({
    title: "خطا",
    message: errorDetail
  });
  console.log(e);
  throw e;
});
}
