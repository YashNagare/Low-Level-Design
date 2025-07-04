package DesignPatterns.Creational.BuilderPattern;

public interface PizzaBuilder {

    void buildDough();
    void buildSauce();
    void buildTopping();
    Pizza getPizza();

}
