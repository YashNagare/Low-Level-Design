package DesignParkingLot.parkingspot;

import DesignParkingLot.vehicle.Vehicle;
import DesignParkingLot.vehicle.VehicleType;

public class LargeSpot extends ParkingSpot {

    public LargeSpot(String spotId) {
        super(spotId);
    }

    @Override
    public boolean canFitVehicle(Vehicle vehicle) {
        return vehicle.getVehicleType() == VehicleType.TRUCK;
    }
}
