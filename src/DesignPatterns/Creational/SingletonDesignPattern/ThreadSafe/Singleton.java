package DesignPatterns.Creational.SingletonDesignPattern.ThreadSafe;

public final class Singleton {

    private static Singleton instance;
    public String value;

    private Singleton(String value) {
        System.out.println("Called SingletonPatternMultiThreaded class");
        this.value = value;
    }

    public static synchronized Singleton getInstance(String value) {
        if (instance == null) {
            instance = new Singleton(value);
        }
        return instance;
    }

}
