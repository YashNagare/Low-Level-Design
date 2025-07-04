package DesignPatterns.Behavioral.ChainOfResponsibility;

public class ChainOfResponsibility {
    public static void main(String[] args) {
        Handler low = new LowLevelSupport();
        Handler mid = new MidLevelSupport();
        Handler high = new HighLevelSupport();

        low.setNext(mid);
        mid.setNext(high);

        low.handleRequest("low");
        low.handleRequest("medium");
        low.handleRequest("high");
        low.handleRequest("urgent");
    }
}
