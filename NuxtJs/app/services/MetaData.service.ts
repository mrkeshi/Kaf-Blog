import { Fetch } from "../utilities/CutsomMyFetchApi";
import { type ApiResponse } from "~/models/ApiRespose";
import { type SidebarDataDTO } from "~/models/SideBarData/MetaDataDTO";


export const getSideBarDataService = (): Promise<ApiResponse<SidebarDataDTO>> => {
 
    return Fetch<SidebarDataDTO>(`metadata/`,{
        method:'get',
    });
}
