
from Leaf import Leaf
from Composite import Composite

def main():

    # Creating Leaf objects
    leaf1 = Leaf("Leaf 1")
    leaf2 = Leaf("Leaf 2")
    leaf3 = Leaf("Leaf 3")

    # Creating Composite objects
    composite1 = Composite("Composite 1")
    composite2 = Composite("Composite 2")

    # Adding Leaf elements to Composite 1
    composite1.add(leaf1)
    composite1.add(leaf2)

    # Adding Composite 1 and Leaf 3 to Composite 2
    composite2.add(composite1)
    composite2.add(leaf3)

    # Displaying the structure and executing operations
    print(composite2.operation())


if __name__ == "__main__":
    main()