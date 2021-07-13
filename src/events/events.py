from collections import namedtuple

# For typing
from typing import Any  # TODO: Don't use `Any`! Create an `Event` type
from collections import deque


EVENTS = {
    'FlashLight': namedtuple('FlashLightEvent', ('pin', 'volt', 'dur_ms')),
    'Movement': namedtuple('MovementEvent', ('dir')),
    'FireWeapon': namedtuple('FireWeaponEvent', ('slot')),
    'FireWeaponsGroup': namedtuple('FireWeaponsGroupEvent', ('slots')),
}


def emit(event: Any, event_queue: deque[Any]) -> None:
    event_queue += event

