package DesignParkingLot;

import DesignParkingLot.fee.FeeStrategy;
import DesignParkingLot.fee.FlatRateFeeStrategy;
import DesignParkingLot.parkingspot.ParkingSpot;
import DesignParkingLot.vehicle.Vehicle;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;

public class ParkingLot {

    private static final ParkingLot INSTANCE = new ParkingLot();
    private final List<ParkingFloor> floorList = new ArrayList<>();
    private final Map<String, ParkingTicket> activeTickets = new ConcurrentHashMap<>();
    private FeeStrategy feeStrategy;

    private ParkingLot() {
        feeStrategy = new FlatRateFeeStrategy();
    }

    public static synchronized ParkingLot getInstance() {
        return INSTANCE;
    }

    public void addFloor(ParkingFloor parkingFloor) {
        floorList.add(parkingFloor);
    }

    public void setFeeStrategy(FeeStrategy feeStrategy) {
        this.feeStrategy = feeStrategy;
    }

    public synchronized ParkingTicket parkVehicle(Vehicle vehicle) throws Exception {
        for (ParkingFloor floor : floorList) {
            Optional<ParkingSpot> spotOpt = floor.getAvailableParkingSpot(vehicle);
            if (spotOpt.isPresent()) {
                ParkingSpot spot = spotOpt.get();
                if (spot.assignVehicle(vehicle)) {
                    ParkingTicket ticket = new ParkingTicket(vehicle, spot);
                    activeTickets.put(vehicle.getLicencePlate(), ticket);
                    return ticket;
                }
            }
        }
        throw new Exception("No available spot for " + vehicle.getVehicleType());
    }

    public synchronized double unparkVehicle(String licence) throws Exception {
        ParkingTicket parkingTicket = activeTickets.remove(licence);
        if (parkingTicket == null) throw new Exception("Ticket not found");

        parkingTicket.getParkingSpot().removeVehicle();
        parkingTicket.setExitTimestamp();
        return feeStrategy.calculateFees(parkingTicket);
    }

}
