
class BorgSingleton(object):
    __shared_state = dict()

    def __init__(self) -> None:
        self.__dict__ = self.__shared_state
        self.state = "GeeksforGeeks"
    
    def __str__(self) -> str:
        return self.state
    
if __name__ == "__main__":
    person1 = BorgSingleton()
    person2 = BorgSingleton()
    person3 = BorgSingleton()
    
    person1.state = "DataStructures"
    person2.state = "Algorithms"

    print(person1)
    print(person2)

    person3.state = "Geeks"
    
    print(person1)
    print(person2)
    print(person3)
