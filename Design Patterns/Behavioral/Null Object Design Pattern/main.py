from VehicleFactory import VehicleFactory

def main():

    vehicle = VehicleFactory()
    vehicleObj = vehicle.getVehicleObject("Bike")
    printVehicleDetails(vehicleObj)

def printVehicleDetails(vehicleObj):
    print(f"Seating Capacity {vehicleObj.getSeatingCapacity()}")
    print(f"Fuel Tank Capacity {vehicleObj.getTankCapacity()}")

if __name__ == '__main__':
    main()