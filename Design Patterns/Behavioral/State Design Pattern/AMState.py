
from State import State

class AMState(State):

    def __init__(self, radio) -> None:
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggleAMFM(self):
        print("Switching to FM")
        self.radio.state = self.radio.fmstate