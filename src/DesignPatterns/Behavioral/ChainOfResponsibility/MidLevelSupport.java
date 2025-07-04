package DesignPatterns.Behavioral.ChainOfResponsibility;

public class MidLevelSupport extends Handler{
    public void handleRequest(String request) {
        if (request.equalsIgnoreCase("medium")) {
            System.out.println("Handled by MidLevelSupport");
        } else if (next != null) {
            next.handleRequest(request);
        }
    }
}
