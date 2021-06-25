from src import events, keybd_sim

from Arduino import Arduino
from time import sleep
from typing import Any  # TODO: Don't use `Any`! Create an `Event` type


PRESS_KEY_DURATION_MS = 0.01


def handle_events(event_queue: events.EventQueue, board: Arduino) -> None:
    for event in event_queue:
        event_type = type(event)

        if event_type == events.EVENTS['FlashLight']:
            print('handle flash light event')
            # TODO: Uncomment after testing
            #handle_flash_light_event(event, board)

        elif event_type == events.EVENTS['Movement']:
            print('handle movement event')
            handle_movement_event(event)

        else:
            print('not handling event')

    event_queue.clear()

def handle_flash_light_event(event: Any, board: Arduino) -> None:
    pin, volt, dur_ms = event.pin, event.volt, event.dur_ms
    original_volt = board.analogRead(pin)

    board.analogWrite(pin, volt)
    sleep(dur_ms / 1000.0)
    board.analogWrite(pin, original_volt)

def handle_movement_event(event: Any) -> None:
    dir = event.dir

    if dir == 'Left':
        keybd_sim.press_key(keybd_sim.KEY_CODES['a'])
        sleep(PRESS_KEY_DURATION_MS)
        keybd_sim.release_key(keybd_sim.KEY_CODES['a'])

    elif dir == 'Right':
        keybd_sim.press_key(keybd_sim.KEY_CODES['d'])
        sleep(PRESS_KEY_DURATION_MS)
        keybd_sim.release_key(keybd_sim.KEY_CODES['d'])

    elif dir == 'Up':
        keybd_sim.press_key(keybd_sim.KEY_CODES['w'])
        sleep(PRESS_KEY_DURATION_MS)
        keybd_sim.release_key(keybd_sim.KEY_CODES['w'])

    elif dir == 'Down':
        keybd_sim.press_key(keybd_sim.KEY_CODES['s'])
        sleep(PRESS_KEY_DURATION_MS)
        keybd_sim.release_key(keybd_sim.KEY_CODES['s'])

