# Liskov Substitution Principle
# If class B is subtype of class A, then we should be able to replace object of A with B without breaking the behaviour of the program
# Subclass should extend the capability of parent class not narrow it down


def animal_leg_count(animals):
    if isinstance(animal, Lion):
        print(lion_leg_count(animal))
    if isinstance(animal, Mouse):
        print(lion_leg_count(animal))
    if isinstance(animal, Pigeon):
        print(lion_leg_count(animal))
    
animal_leg_count(animals)

# Making it to LSP Principle

def animal_leg_count(animals):
    for animal in animals:
        print(animal.leg_count())
animal_leg_count(animals)

"""
The animal_leg_count function cares less the type of Animal passed, it just calls the leg_count method. 
All it knows is that the parameter must be of an Animal type, either the Animal class or its sub-class.
The Animal class now have to implement/define a leg_count method.
And its sub-classes have to implement the leg_count method:
"""

class Animal:
    def leg_count(self):
        pass


class Lion(Animal):
    def leg_count(self):
        pass

# When it's passed to the animal_leg_count function, it returns the number of legs a lion has.

