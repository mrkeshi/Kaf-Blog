import { $fetch, FetchError, FetchOptions } from "ohmyfetch";
import { ApiResponse } from "../models/ApiRespose";
import { BASE_URL } from "./Config";
import { errorMessages } from "vue/compiler-sfc";

export async function Fetch<G>(
  url: string,
  config: FetchOptions<"json"> = {}
): Promise<ApiResponse<G>> {
  config = {
    ...config,
    baseURL: BASE_URL,
  };
  return $fetch<ApiResponse<G>>(url, config)
    .then((res) => res)
    .catch((e: FetchError) => {
      return {
        data: null,
      };
    });
}
