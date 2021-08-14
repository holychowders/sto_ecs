from src.gui.gui import create_label, create_button
from src.gui.weapons.styling import *

from src.components.weapons import SLOT_IDs

from src.events.events import EVENTS
from src.events.event_handler import handle_fire_weapon, handle_fire_weapons_group

# For typing
from src.components.weapons import SLOT_GROUPS, Slots, Slot
from src.gui.gui import WidgetStyling
from typing import Any
from PyQt5.QtWidgets import QGridLayout


# TODO: Consider making a WeaponsGui class since the same data seem to be being passed around repeatedly
def add_section_to_grid(weapon_slots: Slots, grid: QGridLayout) -> None:
    add_header_label_to_grid(grid)
    add_modifiers_label_to_grid(grid)
    add_fire_all_button_to_grid(grid)
    add_fire_buttons_to_grid(weapon_slots, grid)


def add_header_label_to_grid(grid: QGridLayout) -> None:
    header_label = create_label(HEADER_STYLING)

    grid.addWidget(header_label, *HEADER_STYLING.geometry.asTupleForAddingToGridWithLayout())


def add_modifiers_label_to_grid(grid: QGridLayout) -> None:
    modifiers_label = create_label(MODIFIERS_STYLING)

    grid.addWidget(modifiers_label, *MODIFIERS_STYLING.geometry.asTupleForAddingToGridWithLayout())


def add_fire_all_button_to_grid(grid: QGridLayout) -> None:
    event = EVENTS['FireWeaponsGroup'](SLOT_GROUPS.ALL)
    handler = get_on_fire_weapons_group_handler(event)

    button = create_button(FIRE_ALL_BUTTON_STYLING, handler)

    grid.addWidget(button, *FIRE_ALL_BUTTON_STYLING.geometry.asTupleForAddingToGridWithLayout())

def get_on_fire_weapons_group_handler(event: Any) -> Any:
    event = event

    def handle_fire_weapons_groups_event() -> None:
        handle_fire_weapons_group(event)

    return handle_fire_weapons_groups_event


def add_fire_buttons_to_grid(weapon_slots: Slots, grid: QGridLayout) -> None:
    styling = FIRE_BUTTON_INITIAL_STYLING_DATA

    # TODO: Automatically center buttons
    for slot in weapon_slots:
        if slot is None:
            break

        styling.displayed_text = slot.weapon_name
        update_fire_button_style_sheet(slot, styling)
        update_fire_button_geometry(slot, styling)

        fire_button = create_button(styling, get_fire_weapon_handler(EVENTS['FireWeapon'](slot)))

        grid.addWidget(fire_button, *styling.geometry.asTupleForAddingToGridWithLayout())

def update_fire_button_style_sheet(slot: Slots, styling_data: WidgetStyling) -> None:
        # TODO: If this is the case, can flash a button on the weapons section. We do want to use the same event for this case
        if not slot.is_used:
            styling_data.style_sheet = FIRE_BUTTON_UNUSED_STYLE_SHEET
        else:
            styling_data.style_sheet = FIRE_BUTTON_STYLE_SHEET

def update_fire_button_geometry(slot: Slot, styling_data: WidgetStyling) -> None:
    if slot.id == SLOT_IDs.FORWARD_1:
        styling_data.geometry.x_pos = FIRE_BUTTON_LEFTMOST_POSITION_PX
    elif slot.id == SLOT_IDs.AFT_1:
        styling_data.geometry.x_pos = FIRE_BUTTON_LEFTMOST_POSITION_PX
        styling_data.geometry.y_pos += FIRE_BUTTON_VERTICAL_SPACING_FWD_AFT_PX
    else:
        styling_data.geometry.x_pos += FIRE_BUTTON_HORIZONTAL_SPACING_PX

def get_fire_weapon_handler(event: Any) -> Any:
    event = event

    def handle_fire_weapon_event() -> None:
        handle_fire_weapon(event)

    return handle_fire_weapon_event
