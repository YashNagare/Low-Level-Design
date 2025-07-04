package DesignPatterns.Creational.SingletonDesignPattern.DoubleCheckedLocking;


public class DemoDoubleCheckedLocking {

    public static void main(String[] args) {
        Thread threadFoo = new Thread(new DemoDoubleCheckedLocking.ThreadFoo());
        Thread threadBar = new Thread(new DemoDoubleCheckedLocking.ThreadBar());
        threadFoo.start();
        threadBar.start();
    }

    static class ThreadFoo implements Runnable {
        @Override
        public void run() {
            Singleton singleton = Singleton.getInstance("FOO");
            System.out.println(singleton.value);
        }
    }

    static class ThreadBar implements Runnable {
        @Override
        public void run() {
            Singleton singleton = Singleton.getInstance("BAR");
            System.out.println(singleton.value);
        }
    }

}
