package DesignPatterns.Creational.Prototype;

public class Employee implements Prototype{

    private int id;
    private String name;

    public Employee(int id, String name) {
        this.id = id;
        this.name = name;
    }

    @Override
    public Employee clone() {
        return new Employee(id, name);
    }

    public void showDetails() {
        System.out.println("ID: " + id + ", Name: " + name);
    }
}
