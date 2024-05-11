
from Component import Component

class Leaf(Component):

    def __init__(self, name) -> None:
        self.name = name
    
    def operation(self):
        return f"Leaf: {self.name}"