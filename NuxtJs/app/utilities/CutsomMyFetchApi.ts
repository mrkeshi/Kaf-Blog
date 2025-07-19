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


  config = {
    ...config,
    baseURL: "http://127.0.0.1:8000/api/",
  };

  return $fetch<ApiResponse<G>>(url, config)
    .then((res) => {
         return res
    })
    .catch((e: FetchError) => {
     console.log(e.message)
     showError({
      title:"ارور کیر خریدی",
      message:`${e.message}`
     })
      return {
        data: null,
      };
    });
}
