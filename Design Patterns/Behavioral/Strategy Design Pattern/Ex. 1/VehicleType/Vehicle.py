from DriveStrategy import DriveStrategy

class Vehicle:
    def __init__(self, drive_strategy : DriveStrategy):
        self.drive_strategy = drive_strategy

    def drive(self):
        self.drive_strategy.drive()