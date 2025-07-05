package DesignPatterns.Creational.Prototype;

public class Main {

    public static void main(String[] args) {
        Employee original = new Employee(101, "XYZ");
        Employee copy = original.clone();

        original.showDetails();
        copy.showDetails();
    }

}
