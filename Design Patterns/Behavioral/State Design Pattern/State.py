
class State:

    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print(f"Visiting... Station is {self.stations[self.pos]} {self.name}")