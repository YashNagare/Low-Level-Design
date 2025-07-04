package DesignPatterns.Creational.SingletonDesignPattern.SingleThreaded;

public final class Singleton {

    private static Singleton instance;
    public String value;

    private Singleton(String value) {
        System.out.println("Called SingletonPatternSingleThreaded class");
        this.value = value;
    }

    public static Singleton getInstance(String value) {
        if (instance == null) {
            instance = new Singleton(value);
        }
        return instance;
    }
    
}
