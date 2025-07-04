package DesignParkingLot.parkingspot;

public class ParkingSpotFactory {

    public static ParkingSpot createParkingSpot(ParkingSpotType parkingSpotType, String spotId) {
        return switch (parkingSpotType) {
            case BIKE -> new BikeSpot(spotId);
            case COMPACT -> new CompactSpot(spotId);
            case LARGE -> new LargeSpot(spotId);
            default -> throw new IllegalArgumentException("Unknown parking spot type: " + parkingSpotType);
        };
    }

}
