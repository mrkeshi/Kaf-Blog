import { $fetch, FetchError, type FetchOptions } from "ohmyfetch";
import { type ApiResponse } from "../models/ApiRespose.js";
import { errorMessages } from "vue/compiler-sfc";
import { useRuntimeConfig } from "nuxt/app";


export async function Fetch<G>(
  url: string,
  config: FetchOptions<"json"> = {}
): Promise<ApiResponse<G>> {


 const runtimeConfig = useRuntimeConfig();
  config = {
    ...config,
    baseURL: "http://127.0.0.1:8000/api",
  };

  return $fetch<ApiResponse<G>>(url, config)
    .then((res) => {
    console.log("success")
      return res

    })
    .catch((e: FetchError) => {
     console.log(e.message)
      return {
        data: null,
      };
    });
}
