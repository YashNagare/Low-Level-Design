
from Component import Component

class Composite(Component):
    
    def __init__(self, name) -> None:
        self.name = name
        self.children = list()

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        results = [f"Composite: {self.name}"]
        for child in self.children:
            results.append(child.operation())
        return "\n".join(results)