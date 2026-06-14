export interface NotificationDTO {
  id: number
  title: string
  message: string
  type: 'info' | 'success' | 'warning' | 'error' | 'post'
  link: string
  created_at: string
}
