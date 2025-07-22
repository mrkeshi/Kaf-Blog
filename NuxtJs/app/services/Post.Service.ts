import { Fetch } from "../utilities/CutsomMyFetchApi";
import { type ApiResponse } from "~/models/ApiRespose";
import type { PaginatedPostListResponseDTO, PostDetailDTO } from "~/models/Post/PostDTO";


export const getPostListService = (current:number): Promise<ApiResponse<PaginatedPostListResponseDTO>> => {
 
    return Fetch<PaginatedPostListResponseDTO>(`posts/?page=${current}`,{
        method:'get',
    });
}

export const getSinglePostService = (Slug:String): Promise<ApiResponse<PostDetailDTO>> => {
 
    return Fetch<PostDetailDTO>(`posts/${Slug}/`,{
        method:'get',
    });
}
