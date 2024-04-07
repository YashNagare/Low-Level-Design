# Single Responsibility Principles
# A class should have only 1 reason to change.
# If a class has more than one responsibility, it becomes coupled.
# A change to one responsibility results to modification of the other responsibility.

class Animal:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        pass

    def save(self):
        pass


# The Animal class violates the SRP.

class Animal:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        pass

class AnimalDB:
    def get_animal(self):
        pass
    
    def save(self, animal):
        pass