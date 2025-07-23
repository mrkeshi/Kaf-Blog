import { Fetch } from "../utilities/CutsomMyFetchApi";
import { type ApiResponse } from "~/models/ApiRespose";
import type { CommentDTO } from "~/models/Post/CommentDTO";
import type { PaginatedPostListResponseDTO, PostDetailDTO } from "~/models/Post/PostDTO";
import Slug from "~/pages/[slug].vue";


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
export const sendCommentDataService = (data:CommentDTO): Promise<ApiResponse<CommentDTO>> => {
 
    return Fetch<CommentDTO>('comments/create',{
        method:'post',
        body:data
    });
}

export const getPostListCategoryService = (current:number,category:string): Promise<ApiResponse<PaginatedPostListResponseDTO>> => {

    return Fetch<PaginatedPostListResponseDTO>(`posts/category/${category}/?page=${current}`,{
        method:'get',
    });
}
