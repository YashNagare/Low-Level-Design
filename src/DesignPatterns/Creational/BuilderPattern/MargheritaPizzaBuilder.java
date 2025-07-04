package DesignPatterns.Creational.BuilderPattern;

public class MargheritaPizzaBuilder implements PizzaBuilder {

    private Pizza pizza = new Pizza();

    @Override
    public void buildDough() {
        pizza.setDough("Thin Crust");
    }

    @Override
    public void buildSauce() {
        pizza.setSauce("Tomato Basil");
    }

    @Override
    public void buildTopping() {
        pizza.setTopping("Mozzarella Chesse");
    }

    @Override
    public Pizza getPizza() {
        return pizza;
    }
}
