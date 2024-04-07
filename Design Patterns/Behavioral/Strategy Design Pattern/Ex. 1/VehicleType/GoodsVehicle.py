from .Vehicle import Vehicle
from DriveStrategy.NormalDriveStrategy import NormalDriveStrategy

class GoodsVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalDriveStrategy())