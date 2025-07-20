import type { SiteSettingDTO } from "~/models/SiteSettingDTO";
import { Fetch } from "../utilities/CutsomMyFetchApi";
import { type ApiResponse } from "~/models/ApiRespose";


export const getSettingDataService = (): Promise<ApiResponse<SiteSettingDTO>> => {
 
    return Fetch<SiteSettingDTO>('setting/',{
        method:'get',
    });
}
