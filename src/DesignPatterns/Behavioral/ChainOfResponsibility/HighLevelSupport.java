package DesignPatterns.Behavioral.ChainOfResponsibility;

public class HighLevelSupport extends Handler{
    public void handleRequest(String request) {
        if (request.equalsIgnoreCase("high")) {
            System.out.println("Handled by HighLevelSupport");
        } else {
            System.out.println("Request cannot be handled");
        }
    }
}
