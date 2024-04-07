from .Vehicle import Vehicle
from DriveStrategy.SportyDriveStrategy import SportyDriveStrategy

class OffRoadVehicle(Vehicle):
    def __init__(self):
        super().__init__(SportyDriveStrategy())