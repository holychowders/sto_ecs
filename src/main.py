from src.gui import gui_main

from Arduino import Arduino
from collections import deque

from typing import Any


# TODO: Allow specifying port at CLI
#BOARD_PORT = '/dev/ttyACM0'  # Elegoo MEGA 2560 R3
#BOARD_PORT = '/dev/ttyUSB0'  # redevZone Nano
#BAUDRATE = 9_600


EVENT_QUEUE: deque[Any] = deque()

def main() -> None:
    gui_main.main()

    # FIXME: This doesn't actually work
    #board = Arduino(baud=BAUDRATE, port=BOARD_PORT)
    #board.pinMode(13, 'OUTPUT')


if __name__ == '__main__':
    main()

