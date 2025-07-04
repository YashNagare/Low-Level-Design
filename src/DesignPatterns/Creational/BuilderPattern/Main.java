package DesignPatterns.Creational.BuilderPattern;

public class Main {
    public static void main(String[] args) {
        Cook cook = new Cook();
        PizzaBuilder margheritaBuilder = new MargheritaPizzaBuilder();

        cook.setPizzaBuilder(margheritaBuilder);
        Pizza pizza = cook.makePizza();

        System.out.println(pizza);
    }
}
