import type { NotificationDTO } from '~/models/Notification/NotificationDTO'

const getBaseURL = () => useRuntimeConfig().public.baseURL as string

/**
 * Fetch unread notifications for this browser token.
 * @param token   - stable UUID stored in localStorage
 * @param since   - optional: only return notifications with id > since
 */
export const getNotificationsService = async (
  token: string,
  since?: number
): Promise<NotificationDTO[]> => {
  const params: Record<string, string> = { token }
  if (since) params.since = String(since)

  return $fetch<NotificationDTO[]>(
    `${getBaseURL()}notifications/?${new URLSearchParams(params).toString()}`
  )
}

/**
 * Mark a list of notification IDs as read for this token.
 */
export const markNotificationsReadService = async (
  token: string,
  ids: number[]
): Promise<{ marked: number }> => {
  return $fetch<{ marked: number }>(`${getBaseURL()}notifications/mark-read/`, {
    method: 'POST',
    body: { token, ids }
  })
}
