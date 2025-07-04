package DesignPatterns.Structural.Observer;

public class ObserverPatternDemo {
    public static void main(String[] args) {
        NewsAgency agency = new NewsAgency();

        NewsChannel channel1 = new NewsChannel("Channel 1");
        NewsChannel channel2 = new NewsChannel("Channel 2");

        agency.attach(channel1);
        agency.attach(channel2);

        agency.setNews("New Java version released!");
    }
}
