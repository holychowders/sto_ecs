from src.sound.sounds import play_tng_fire_weapon
from src.events.events import EVENTS, EventQueue

from src.keys.keybd_sim import press_key, PRESS_KEY_DURATION_MS
from src.keys.keys import CODES as KEY_CODES

from Arduino import Arduino
from time import sleep
from typing import Any  # TODO: Don't use `Any`. Create an `Event` type


def handle_events(event_queue: EventQueue, board: Arduino = None) -> None:
    while True:
        event = event_queue.popleft()
        event_type = type(event)

        if event_type == EVENTS['FlashLight']: handle_flash_light_event(event, board)
        elif event_type == EVENTS['Movement']: handle_movement_event(event)
        elif event_type == EVENTS['FireWeapon']: handle_fire_weapon(event)

#def handle_events(event_queue: EventQueue, board: Arduino = None) -> None:
#    for event in event_queue:
#        event_type = type(event)
#
#        if event_type == EVENTS['FlashLight']:
#            handle_flash_light_event(event, board)
#
#        elif event_type == EVENTS['Movement']:
#            handle_movement_event(event)
#
#        elif event_type == EVENTS['FireWeapon']:
#            handle_fire_weapon(event)
#
#    event_queue.clear()
#    print('queue after clear:', event_queue)

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
    #keybd_sim.press_key(keys.MAPPINGS[event.weapon_slot_id])
    play_tng_fire_weapon()

