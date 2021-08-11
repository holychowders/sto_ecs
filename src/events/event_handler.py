from src.sound import sounds
from src.events.events import EVENTS

from src.keys.keybd_sim import press_key, PRESS_KEY_DURATION_MS
from src.keys.keys import MAPPINGS, CODES as KEY_CODES

from threading import Thread
from Arduino import Arduino
from time import sleep

# For typing
from typing import Any  # TODO: Don't use `Any`. Create an `Event` type
from collections import deque


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
    dir = event.dir

    if dir == 'Left':
        press_key(KEY_CODES['a'])
        sleep(PRESS_KEY_DURATION_MS)
        release_key(KEY_CODES['a'])

    elif dir == 'Right':
        press_key(KEY_CODES['d'])
        sleep(PRESS_KEY_DURATION_MS)
        release_key(KEY_CODES['d'])

    elif dir == 'Up':
        press_key(KEY_CODES['w'])
        sleep(PRESS_KEY_DURATION_MS)
        release_key(KEY_CODES['w'])

    elif dir == 'Down':
        press_key(KEY_CODES['s'])
        sleep(PRESS_KEY_DURATION_MS)
        release_key(KEY_CODES['s'])

def handle_fire_weapon(event: Any) -> None:
    slot = event.slot

    # TODO: and `slot.is_available` (ie, not re-charging)
    if slot.is_used:
        press_keys = lambda: press_key(MAPPINGS[slot.id])

        do_threaded(
            press_keys,
            sounds.play_tng_keypress_1,
            sounds.play_tng_fire_weapon
        )
    else:
        do_threaded(sounds.play_tng_invalid_keypress_1)

def handle_fire_weapons_group(event: Any) -> None:
    slots = event.slots.value

    def handle() -> None:
        sounds.play_tng_processed_input_1()
        press_key(KEY_CODES['SPACE'])
        sounds.play_tng_fire_weapon()
        #for slot_id in slots:
        #    sounds.play_tng_fire_weapon()
        #    press_key(MAPPINGS[slot_id])
        #    sleep(.3)

    do_threaded(handle)

def do_threaded(*functions: Any) -> None:
    [Thread(target=function).start() for function in functions]

