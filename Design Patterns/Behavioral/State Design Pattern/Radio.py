
from FMState import FMState
from AMState import AMState

class Radio:

    def __init__(self) -> None:
        self.fmstate = FMState(self)
        self.amstate = AMState(self)
        self.state = self.fmstate

    def toggleAMFM(self):
        self.state.toggleAMFM()

    def scan(self):
        self.state.scan()