from src.gui.gui import create_label, create_button
from src.gui.weapons.styling import *

from src.components.weapons import SLOT_IDs

from src.events.events import EVENTS
from src.events.event_handler import handle_fire_weapon, handle_fire_weapons_group

# For typing
from typing import Any
from src.components.weapons import SLOT_GROUPS, Slots
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtCore import Qt

def add_section_to_grid(weapon_slots: Slots, grid: QGridLayout) -> None:
    section_label = create_label(SECTION_LABEL_DISPLAY_NAME, SECTION_LABEL_STYLE_SHEET, Qt.AlignHCenter)
    modifiers_section_label = create_label(MODIFIERS_SECTION_DISPLAY_NAME, MODIFIERS_SECTION_LABEL_STYLE_SHEET, Qt.AlignHCenter)

    event = EVENTS['FireWeaponsGroup'](SLOT_GROUPS.ALL)
    handler = on_fire_weapons_group(event)
    fire_all_button = create_button(FIRE_ALL_BUTTON_DISPLAY_NAME, FIRE_ALL_BUTTON_STYLE_SHEET, handler)

    grid.addWidget(section_label, *SECTION_LABEL_WIDGET_GEOMETRY)
    grid.addWidget(modifiers_section_label, *MODIFIERS_SECTION_LABEL_WIDGET_GEOMETRY)
    grid.addWidget(fire_all_button, *FIRE_ALL_BUTTON_WIDGET_GEOMETRY)

    row = FIRE_BUTTON_STARTING_ROW
    column = FIRE_BUTTON_LEFTMOST_COLUMN
    # TODO: Automatically center buttons
    for slot in weapon_slots:
        if slot is None:
            break

        if slot.id == SLOT_IDs.AFT_1:
            row += FIRE_BUTTON_FWD_AFT_ROW_SPACING
            column = FIRE_BUTTON_LEFTMOST_COLUMN

        # TODO: If this is the case, can flash a button on the weapons section. We do want to use the same event for this case
        if not slot.is_used:
            style_sheet = FIRE_BUTTON_UNUSED_STYLE_SHEET
        else:
            style_sheet = FIRE_BUTTON_STYLE_SHEET

        event = EVENTS['FireWeapon'](slot)
        handler = on_fire_weapon(event)
        button = create_button(slot.weapon_name, style_sheet, handler)

        grid.addWidget(button, row, column, FIRE_BUTTON_ROW_HEIGHT, FIRE_BUTTON_COLUMN_WIDTH)

        column += FIRE_BUTTON_COLUMNS_SPACING

def on_fire_weapon(event: Any) -> Any:
    event = event

    def handle_fire_weapon_event() -> None:
        handle_fire_weapon(event)

    return handle_fire_weapon_event

def on_fire_weapons_group(event: Any) -> Any:
    event = event

    def handle_fire_weapons_groups_event() -> None:
        handle_fire_weapons_group(event)

    return handle_fire_weapons_groups_event

