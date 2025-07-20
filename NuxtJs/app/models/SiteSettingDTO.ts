export interface SiteSettingDTO {
  site_name: string;
  site_url: string;
  email_admin: string ;
  site_logo: string | null ;
  site_icon: string |null;
  music: string ;
  music_cover: string ;
  meta_description: string ;
  music_artist: string ;
  music_title: string ;
  meta_keywords: string ;
  meta_author: string ;
  is_active: boolean;
  count:number
}
