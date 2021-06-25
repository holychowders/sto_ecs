from src import events, event_handler

from Arduino import Arduino
from time import sleep
from random import randint, choice


# TODO: Allow specifying port at CLI
#BOARD_PORT = '/dev/ttyACM0'  # Elegoo MEGA 2560 R3
BOARD_PORT = '/dev/ttyUSB0'  # redevZone Nano
BAUDRATE = 9_600


def main() -> None:
    event_queue = events.EventQueue()
    # FIXME: This doesn't actually work
    #TODO: Uncomment after testing
    #board = Arduino(baud=BAUDRATE, port=BOARD_PORT)
    #board.pinMode(13, 'OUTPUT')

    while True:
        sleep(1.0)

        event = events.EVENTS['FlashLight'](pin=randint(13,13), volt=4.0, dur_ms=1000)
        events.emit(event, event_queue)

        event = events.EVENTS['Movement'](dir=choice(['Left', 'Right']))
        events.emit(event, event_queue)

        print('\nEVENT QUEUE:', event_queue)

        board = None
        event_handler.handle_events(event_queue, board)


if __name__ == '__main__':
    main()

