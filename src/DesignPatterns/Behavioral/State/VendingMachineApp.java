package DesignPatterns.Behavioral.State;

public class VendingMachineApp {
    public static void main(String[] args) {

        VendingMachine vendingMachine = new VendingMachine();

        vendingMachine.insertCoin(1.0);
        vendingMachine.selectedItem("A1");
        vendingMachine.insertCoin(1.5);
        vendingMachine.dispenseItem();

        System.out.println("\n---Second Transaction ---");
        vendingMachine.selectedItem("B2");
        vendingMachine.insertCoin(2.0);
        vendingMachine.dispenseItem();
    }
}
