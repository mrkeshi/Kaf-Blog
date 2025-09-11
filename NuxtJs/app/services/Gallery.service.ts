import type { SendGalleryDTO } from "~/models/Gallery/SendGalleryDTO";
import { Fetch } from "../utilities/CutsomMyFetchApi";
import { type ApiResponse } from "~/models/ApiRespose";

export const sendImageDataService = (data:SendGalleryDTO): Promise<ApiResponse<SendGalleryDTO>> => {
 
    return Fetch<SendGalleryDTO>('gsllery/gallery/',{
        method:'post',
        body:data
    });
}
