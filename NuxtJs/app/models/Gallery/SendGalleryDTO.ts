export interface SendGalleryDTO {
  location: string;
  sender_name: string;
  photo: string | null;
}
export interface GalleryItemDTO {
  id: number;
  location: string;
  sender_name: string;
  photo: string;
  status: "pending" | "approved" | "rejected"; 
  created_at: string; 
}

export interface GalleryResponseDTO {
  count: number;
  next: string | null;
  previous: string | null;
  results: GalleryItemDTO[];
}