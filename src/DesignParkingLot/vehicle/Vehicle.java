package DesignParkingLot.vehicle;

public abstract class Vehicle {

    protected String licencePlate;
    protected VehicleType vehicleType;

    public Vehicle(String licencePlate, VehicleType vehicleType) {
        this.licencePlate = licencePlate;
        this.vehicleType = vehicleType;
    }

    public String getLicencePlate() {
        return licencePlate;
    }

    public VehicleType getVehicleType() {
        return vehicleType;
    }
}
