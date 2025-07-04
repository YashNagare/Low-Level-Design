package DesignParkingLot.parkingspot;

import DesignParkingLot.vehicle.Vehicle;
import DesignParkingLot.vehicle.VehicleType;

public class CompactSpot extends ParkingSpot {

    public CompactSpot(String spotId) {
        super(spotId);
    }

    @Override
    public boolean canFitVehicle(Vehicle vehicle) {
        return vehicle.getVehicleType() == VehicleType.CAR;
    }
}
