export interface TagDTO {
  id: number
  name: string
  slug: string
}

export interface CategoryDTO {
  id: number
  name: string
  slug: string
}

export interface CommentDTO {
  id: number
  name: string
  message: string
  answer: string
  created_at: string
}

export interface PostListDTO {
  id: number
  title: string
  slug: string
  image?: string | null
  created_at: string
  views: number
  comment_count: number
  like_count: number
  category: CategoryDTO
  tags: TagDTO[]
  is_draft: boolean
  content: string
}

export interface PaginatedPostListResponseDTO {
  count: number
  next?: string | null
  previous?: string | null
  results: PostListDTO[]
}

export interface PostDetailDTO {
  id: number
  title: string
  slug: string
  content: string
  image?: string | null
  created_at: string
  updated_at?: string
  is_draft: boolean
  views: number
  comment_count: number
  like_count: number
  category: CategoryDTO
  tags: TagDTO[]
  comments: CommentDTO[]
}

export interface LikedDTO{
  liked:boolean
}


export interface LikeResponseDTO {
  code: 0 | 1 | 2;            // 0 = error, 1 = liked, 2 = disliked
  status: 'liked' | 'disliked';
  post: number;
}