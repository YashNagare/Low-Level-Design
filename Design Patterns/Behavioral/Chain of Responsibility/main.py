
from Chain import Chain
from ConcreteHandlerA import ConcreteHandlerA
from ConcreteHandlerB import ConcreteHandlerB

def main():
    
    chain = Chain()
    chain.add_handler(ConcreteHandlerA())
    chain.add_handler(ConcreteHandlerB())

    requests = ['A', 'B', 'C']

    for request in requests:
        print(f"Processing request: {request}")
        chain.handle_request(request)
        print()


if __name__ == '__main__':
    main()
