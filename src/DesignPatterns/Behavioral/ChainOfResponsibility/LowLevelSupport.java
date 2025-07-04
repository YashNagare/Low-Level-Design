package DesignPatterns.Behavioral.ChainOfResponsibility;

public class LowLevelSupport extends Handler{
    public void handleRequest(String request) {
        if (request.equalsIgnoreCase("low")) {
            System.out.println("Handled by LowLevelSupport");
        } else if (next != null) {
            next.handleRequest(request);
        }
    }
}
