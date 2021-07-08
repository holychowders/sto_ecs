from enum import Enum
from collections import namedtuple


class SLOT_IDs(Enum):
    FORWARD_1 = 'Forward-1'
    FORWARD_2 = 'Forward-2'
    FORWARD_3 = 'Forward-3'
    FORWARD_4 = 'Forward-4'

    AFT_1 = 'AFT-1'
    AFT_2 = 'AFT-2'
    AFT_3 = 'AFT-3'
    AFT_4 = 'AFT-4'

_slots_fields = ('slot1', 'slot2', 'slot3', 'slot4', 'slot5', 'slot6', 'slot7', 'slot8')
Slots = namedtuple('Slots', _slots_fields, defaults=(None,) * len(_slots_fields))

class Slot:
    def __init__(self, slot_id: SLOT_IDs, weapon_name: str):
        self.id = slot_id
        self.weapon_name = weapon_name

def get_equipped() -> Slots:
    # TODO.
    sample = Slots(
        Slot(SLOT_IDs.FORWARD_1, 'name for f-slot 1'),
        Slot(SLOT_IDs.FORWARD_2, 'name for f-slot 2'),
        Slot(SLOT_IDs.FORWARD_3, 'name for f-slot 3'),
        Slot(SLOT_IDs.FORWARD_4, 'name for f-slot 4'),
        Slot(SLOT_IDs.AFT_1, 'name for a-slot 1'),
        Slot(SLOT_IDs.AFT_2, 'name for a-slot 2'),
        Slot(SLOT_IDs.AFT_3, 'Slot 3 (Unused)'),
        Slot(SLOT_IDs.AFT_4, 'name for a-slot 3'),
    )

    return sample

