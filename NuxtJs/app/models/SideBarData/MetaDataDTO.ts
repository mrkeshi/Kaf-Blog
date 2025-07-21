export interface TagDTO {
  id: number
  name: string
  slug: string
}

export interface CategoryDTO {
  id: number
  name: string
  slug: string
  post_count: number
}

export interface LinkDTO {
  id: number
  title: string
  link: string
}

export interface SidebarDataDTO {
  tags: TagDTO[]
  categories: CategoryDTO[]
  links: LinkDTO[]
}
