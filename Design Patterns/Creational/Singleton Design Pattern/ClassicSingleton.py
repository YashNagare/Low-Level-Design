
class ClassicSingleton(object):

    __shared_instance = "GeeksforGeeks"

    @staticmethod
    def getInstance():
        if ClassicSingleton.__shared_instance == "GeeksforGeeks":
            ClassicSingleton()
        return ClassicSingleton.__shared_instance
    
    def __init__(self) -> None:
        if ClassicSingleton.__shared_instance != "GeeksforGeeks":
            raise Exception("This class is a singleton class!")
        else:
            ClassicSingleton.__shared_instance = self

if __name__ == "__main__":
    
    obj = ClassicSingleton()
    print(obj)

    obj = ClassicSingleton.getInstance()
    print(obj)