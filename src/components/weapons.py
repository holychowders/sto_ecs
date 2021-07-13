from enum import Enum
from collections import namedtuple


SLOT_IDs = Enum('SLOT_IDs', 'FORWARD_1 FORWARD_2 FORWARD_3 FORWARD_4  AFT_1 AFT_2 AFT_3 AFT_4')

_slots_fields = ('slot1', 'slot2', 'slot3', 'slot4', 'slot5', 'slot6', 'slot7', 'slot8')
Slots = namedtuple('Slots', _slots_fields, defaults=(None,) * len(_slots_fields))

class Slot:
    def __init__(self, slot_id: SLOT_IDs, weapon_name: str = '', is_used: bool = True):
        self.id = slot_id
        self.weapon_name = weapon_name
        self.is_used = is_used

# TODO.
def get_equipped() -> Slots:
    sample = Slots(
        Slot(SLOT_IDs.FORWARD_1, 'name for f-slot 1'),
        Slot(SLOT_IDs.FORWARD_2, 'name for f-slot 2'),
        Slot(SLOT_IDs.FORWARD_3, 'name for f-slot 3'),
        Slot(SLOT_IDs.FORWARD_4, 'name for f-slot 4'),
        Slot(SLOT_IDs.AFT_1, 'name for a-slot 1'),
        Slot(SLOT_IDs.AFT_2, 'name for a-slot 2'),
        Slot(SLOT_IDs.AFT_3, 'Slot 3 (Unused)', is_used = False),
        Slot(SLOT_IDs.AFT_4, 'name for a-slot 4'),
    )

    return sample

class SLOT_GROUPS(Enum):
    ALL      = Slots(*SLOT_IDs)

    FORWARD = Slots(SLOT_IDs.FORWARD_1, SLOT_IDs.FORWARD_2, SLOT_IDs.FORWARD_3, SLOT_IDs.FORWARD_4)
    AFT     = Slots(SLOT_IDs.AFT_1, SLOT_IDs.AFT_2, SLOT_IDs.AFT_3, SLOT_IDs.AFT_4)
    #FORWARD  = Slots(SLOT_IDs[:4:])
    #AFT      = Slots(SLOT_IDs[4::])

    #ENERGY  = Slots()
    #KINETIC = Slots()

