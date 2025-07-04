package DesignParkingLot.fee;

import DesignParkingLot.ParkingTicket;

public interface FeeStrategy {

    double calculateFees(ParkingTicket parkingTicket);

}
