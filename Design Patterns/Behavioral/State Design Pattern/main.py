
from Radio import Radio

def main():

    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggleAMFM] + [radio.scan] * 3
    actions *= 2

    for action in actions:
        action()


if __name__ == "__main__":
    main()