from .Vehicle import Vehicle
from DriveStrategy.SportyDriveStrategy import SportyDriveStrategy

class SportsVehicle(Vehicle):
    def __init__(self):
        super().__init__(SportyDriveStrategy())