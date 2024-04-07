from .notification_alert_observer import NotificationAlertObserver


class EmailAlertObserverImpl(NotificationAlertObserver):
    def __init__(self, email_id, stock_observable):
        self.email_id = email_id
        self.stock_observable = stock_observable

    def update(self):
        self.send_mail(self.email_id, "product is in stock hurry up!!!")

    def send_mail(self, email_id, msg):
        print(f"Mail sent to {email_id}")
