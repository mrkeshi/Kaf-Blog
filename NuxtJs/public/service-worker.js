self.addEventListener("push", function(event) {
  const data = event.data?.json() || {};

  const options = {
    body: data.body || "شما یک نوتیف جدید دارید",
    icon: "/images/l192.png",
    badge: "/images/l192.png",
    data: {
      url: data.url || "/"  
    }
  };

  event.waitUntil(
    self.registration.showNotification(data.title || "نوتیف جدید", options)
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
