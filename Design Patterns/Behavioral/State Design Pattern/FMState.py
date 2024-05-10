
from State import State

class FMState(State):

    def __init__(self, radio) -> None:
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggleAMFM(self):
        print("Switching to AM")
        self.radio.state = self.radio.amstate