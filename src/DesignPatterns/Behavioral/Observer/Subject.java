package DesignPatterns.Structural.Observer;

interface Subject {

    void attach(Observer o);
    void detach(Observer o);
    void notifyObservers();
}
