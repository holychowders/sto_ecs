from src import events

from collections import namedtuple
from typing import Iterable, Any  # TODO: Don't use `Any`! Create an `Event` type


EVENTS = {
    'FlashLight': namedtuple('FlashLightEvent', ('pin', 'volt', 'dur_ms')),
    'Movement': namedtuple('MovementEvent', ('dir'))
}


class EventQueue():

    def __init__(self) -> None:
        self.queue: Any = []

    def clear(self) -> None:
        self.queue.clear()

    def __str__(self) -> str:
        events_str = ''

        for event in self.queue:
            events_str += f'\n{event}'

        return events_str

    def __len__(self) -> int:
        return len(self.queue)

    def __add__(self, event: Any) -> None:
        self.queue.append(event)

    def __iter__(self) -> Iterable[Any]:
        return iter(self.queue)

def emit(event: Any, event_queue: EventQueue) -> None:
    event_queue += event

