from Observable.iphone_observable_impl import IphoneObservableImpl
from Observer.email_alert_observer_impl import EmailAlertObserverImpl
from Observer.mobile_alert_observer_impl import MobileAlertObserverImpl


def main():
    iphone_stock_observable = IphoneObservableImpl()

    observer1 = EmailAlertObserverImpl('abc@gmail.com', iphone_stock_observable)
    observer2 = EmailAlertObserverImpl('xyz@gmail.com', iphone_stock_observable)
    observer3 = MobileAlertObserverImpl('abc_username', iphone_stock_observable)

    iphone_stock_observable.add_observer(observer1)
    iphone_stock_observable.add_observer(observer2)
    iphone_stock_observable.add_observer(observer3)

    iphone_stock_observable.set_stock_count(10)


if __name__ == '__main__':
    main()
