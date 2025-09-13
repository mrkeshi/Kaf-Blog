import type { GalleryResponseDTO, SendGalleryDTO } from "~/models/Gallery/SendGalleryDTO";
import { Fetch } from "../utilities/CutsomMyFetchApi";
import { type ApiResponse } from "~/models/ApiRespose";

export const sendImageDataService = (data:SendGalleryDTO): Promise<ApiResponse<SendGalleryDTO>> => {
 
    return Fetch<SendGalleryDTO>('gsllery/gallery/',{
        method:'post',
        body:data
    });
}

export const getImageDataService = (
  page: number = 1,
  pageSize: number = 20
): Promise<ApiResponse<GalleryResponseDTO>> => {
  return Fetch<GalleryResponseDTO>('gsllery/gallery/', {
    method: 'get',
    params: { page, page_size: pageSize }
  });
};