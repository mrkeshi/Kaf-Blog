import { Fetch } from "../utilities/CutsomMyFetchApi";
import { type ApiResponse } from "~/models/ApiRespose";
import type { PaginatedPostListResponseDTO } from "~/models/Post/PostDTO";


export const getPostListService = (current:number): Promise<ApiResponse<PaginatedPostListResponseDTO>> => {
 
    return Fetch<PaginatedPostListResponseDTO>(`posts/?page=${current}`,{
        method:'get',
    });
}
