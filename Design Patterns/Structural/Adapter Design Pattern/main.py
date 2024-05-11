
from Socket import Socket
from Adapter import Adapter
from ElectricKettle import ElectricKettle

def main():
    
    # Plug in
    socket = Socket()
    adapter = Adapter(socket)
    kettle = ElectricKettle(adapter)

    # Make Coffee
    kettle.boil()
    return 0


if __name__ == "__main__":
    main()