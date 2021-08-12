from src.sound import sounds
from src.events.events import EVENTS

from src.keys.keybd_sim import press_key
from src.keys.keys import MAPPINGS

from threading import Thread
from Arduino import Arduino
from time import sleep

# For typing
from typing import Any
from collections import deque

# TODO: Don't use `Any` for deque. Create an `Event` type
def handle_events(event_queue: deque[Any], board: Arduino = None) -> None:
    while True:
        event = event_queue.popleft()
        event_type = type(event)

        if event_type == EVENTS['FlashLight']: handle_flash_light_event(event, board)
        elif event_type == EVENTS['Movement']: handle_movement_event(event)
        elif event_type == EVENTS['FireWeapon']: handle_fire_weapon(event)
        elif event_type == EVENTS['FireWeaponsGroup']: handle_fire_weapons_group(event)

def handle_flash_light_event(event: Any, board: Arduino) -> None:
    pin, volt, dur_ms = event.pin, event.volt, event.dur_ms
    original_volt = board.analogRead(pin)

    board.analogWrite(pin, volt)
    sleep(dur_ms / 1000.0)
    board.analogWrite(pin, original_volt)

def handle_movement_event(event: Any) -> None:
    direction = event.dir

    if direction == 'Left':
        press_key('a')
    elif direction == 'Right':
        press_key('d')
    elif direction == 'Up':
        press_key('w')
    elif direction == 'Down':
        press_key('s')

def handle_fire_weapon(event: Any) -> None:
    slot = event.slot

    # TODO: and `slot.is_available` (ie, not re-charging)
    if slot.is_used:
        _do_threaded(
            lambda: press_key(MAPPINGS[slot.id]),

            sounds.play_tng_keypress_1,
            sounds.play_tng_fire_weapon,
        )
    else:
        _do_threaded(sounds.play_tng_invalid_keypress_1)

def handle_fire_weapons_group(event: Any) -> None:
    slots = event.slots.value

    def play_sounds() -> None:
        sounds.play_tng_processed_input_1()
        sounds.play_tng_fire_weapon()

    _do_threaded(
        lambda: press_key(' '),
        play_sounds,
    )

def _do_threaded(*functions: Any) -> None:
    [Thread(target=function).start() for function in functions]

