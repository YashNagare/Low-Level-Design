from Car import Car
from NullVehicle import NullVehicle

class VehicleFactory:
    def getVehicleObject(self, typeOfVehicle):
        print(typeOfVehicle)
        if "Car" == typeOfVehicle:
            return Car()
        return NullVehicle()