import { precacheAndRoute } from 'workbox-precaching';

// Inject file list into the service worker at build time
precacheAndRoute(self.__WB_MANIFEST)

self.addEventListener('push', function(event) {
  let data = {};
  try {
    data = event.data?.json() || {};
  } catch(e) {
    data = { body: event.data?.text() || "شما یک نوتیف جدید دارید" };
  }

  const options = {
    body: data.body || "شما یک نوتیف جدید دارید",
    icon: "/images/l192.png",
    badge: "/images/l192.png",
    data: { url: data.url || "/" }
  };

  event.waitUntil(
    self.registration.showNotification(data.title || "نوتیف جدید", options)
  );

  event.waitUntil(
    clients.matchAll({ includeUncontrolled: true, type: "window" }).then(clientsList => {
      clientsList.forEach(client => {
        client.postMessage({
          type: 'push',
          title: data.title || "نوتیفیکیشن جدید ",
          body: data.body || "شما یک نوتیف جدید دارید"
        });
      });
    })
  );
});

self.addEventListener("notificationclick", function(event) {
  event.notification.close(); 

  const urlToOpen = event.notification.data?.url || "/";

  event.waitUntil(
    clients.matchAll({ type: "window", includeUncontrolled: true }).then(clientList => {
      for (const client of clientList) {
        if (client.url === urlToOpen && "focus" in client) {
          return client.focus();
        }
      }
      if (clients.openWindow) {
        return clients.openWindow(urlToOpen);
      }
    })
  );
});
