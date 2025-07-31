import { Fetch } from "~/utilities/CutsomMyFetchApi";
import { useCustomToastify } from "./useCustomToastify";
import { type NotificationSubscriptionPayloadDTO } from "~/models/PushNotification/PushNotification";

function urlBase64ToUint8Array(base64String: string): Uint8Array {
  const padding = '='.repeat((4 - base64String.length % 4) % 4);
  const base64 = (base64String + padding).replace(/-/g, '+').replace(/_/g, '/');
  const rawData = window.atob(base64);
  const outputArray = new Uint8Array(rawData.length);
  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i);
  }
  return outputArray;
}

export function usePushNotification() {
  const config = useRuntimeConfig();
  const publicVapidKey = config.public.vapidKey;
  const { showError, showSuccess } = useCustomToastify();

  async function subscribeUserToPush() {
    const setting = useMySettingDataStore();  

    if (!('serviceWorker' in navigator)) return console.log("Service Worker پشتیبانی نمی‌شود.");
    if (!('PushManager' in window)) return console.log("Push Notification پشتیبانی نمی‌شود.");

    const permission = await Notification.requestPermission();
    if (permission !== 'granted') {
      return showError({ title: "ناموفق", message: "مجوز درخواست نوتیفیکیشن رد شد." });
    }

    let reg: ServiceWorkerRegistration;
    try {
      reg = await navigator.serviceWorker.register('/service-worker.js');
    } catch (error) {
      return showError({ title: "خطا", message: "ثبت Service Worker با مشکل مواجه شد." });
    }

    const existingSubscription = await reg.pushManager.getSubscription();
    if (existingSubscription) {
      return showSuccess({ title: "قبلاً عضو شدید", message: "شما قبلاً در خبرنامه ثبت نام کردید." });
    }

    const subscription = await reg.pushManager.subscribe({
      userVisibleOnly: true,
      applicationServerKey: urlBase64ToUint8Array(publicVapidKey),
    });

    const payload: NotificationSubscriptionPayloadDTO = {
      subscription_info: subscription.toJSON(),
      browser_info: navigator.userAgent,
      device_info: navigator.platform,
    };

    await Fetch("/notification-subscriptions/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (setting.siteSettingData?.count != null) {
      setting.siteSettingData.count++;
    }

    showSuccess({ title: "موفقیت", message: "شما با موفقیت در خبرنامه ثبت نام کردید." });
  }

  async function unsubscribeUserFromPush() {
    const setting = useMySettingDataStore(); 

    try {
      const reg = await navigator.serviceWorker.getRegistration();
      if (!reg) {
        showError({ title: 'خطا', message: 'Service Worker یافت نشد.' });
        return false;
      }

      const subscription = await reg.pushManager.getSubscription();
      if (!subscription) {
        showError({ title: 'خطا', message: 'شما در حال حاضر عضو نیستید.' });
        return false;
      }

      const unsubscribed = await subscription.unsubscribe();
      if (!unsubscribed) {
        showError({ title: 'خطا', message: 'لغو اشتراک ناموفق بود.' });
        return false;
      }

      const payload = {
        subscription_info: subscription.toJSON(),
        browser_info: navigator.userAgent,
        device_info: navigator.platform,
      };

      await Fetch('/notification-subscriptions/unsubscribe/', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      showSuccess({ title: 'لغو اشتراک', message: 'اشتراک شما با موفقیت لغو شد.' });

      if (setting.siteSettingData?.count != null) {
        setting.siteSettingData.count--;
      }

      return true;
    } catch (error) {
      showError({ title: 'خطا', message: 'مشکلی در لغو اشتراک رخ داده است.' });
      return false;
    }
  }

  async function isUserSubscribed(): Promise<boolean> {
    const reg = await navigator.serviceWorker.getRegistration();
    const sub = await reg?.pushManager.getSubscription();
    return !!sub;
  }

  async function shouldAskForPushPermission(): Promise<boolean> {
    if (Notification.permission === "denied") return false;
    if (Notification.permission === "default") return true;

    const reg = await navigator.serviceWorker.getRegistration();
    const sub = await reg?.pushManager.getSubscription();
    return !sub;
  }

  return {
    subscribeUserToPush,
    unsubscribeUserFromPush,
    shouldAskForPushPermission,
    isUserSubscribed,
  };
}
