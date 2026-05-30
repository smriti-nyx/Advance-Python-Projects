from plyer import notification

notification.notify(
    title = "Hello",
    message = "My first desktop notification",
    app_name ="My python app",
    timeout = 6 #seconds before the notification disappears
)