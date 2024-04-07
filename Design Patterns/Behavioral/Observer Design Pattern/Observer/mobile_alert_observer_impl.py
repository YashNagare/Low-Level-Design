from .notification_alert_observer import NotificationAlertObserver


class MobileAlertObserverImpl(NotificationAlertObserver):
    def __init__(self, username, stock_observable):
        self.username = username
        self.stock_observable = stock_observable

    def update(self):
        self.send_msg(self.username, "Product is in stock hurry up!!!")

    def send_msg(self, username, msg):
        print(f"Message sent to: {username}")
