package DesignParkingLot.parkingspot;

import DesignParkingLot.vehicle.Vehicle;
import DesignParkingLot.vehicle.VehicleType;

public class BikeSpot extends ParkingSpot {

    public BikeSpot(String spotId) {
        super(spotId);
    }

    @Override
    public boolean canFitVehicle(Vehicle vehicle) {
        return vehicle.getVehicleType() == VehicleType.BIKE;
    }
}
