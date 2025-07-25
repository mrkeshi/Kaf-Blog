export interface NotificationSubscriptionPayloadDTO {
  subscription_info: ReturnType<PushSubscription['toJSON']>
  browser_info: string
  device_info: string
}