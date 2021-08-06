from collections import namedtuple

from typing import Tuple


_widget_data_fields: Tuple[str, str, str, str] = ('int', 'column', 'rows', 'columns')
WidgetData: WidgetData = namedtuple('WidgetData', _widget_data_fields, defaults=(None,) * len(_widget_data_fields))


SECTION_LABEL_DISPLAY_NAME: str = 'WEAPONS'
SECTION_LABEL_WIDGET_DATA: WidgetData = WidgetData(0, 0, 12, 12)
SECTION_LABEL_STYLE_SHEET: str = (
    "*{" +
        "border: 10px dotted '#ff0000';" +
        "border-radius: 30px;" +
        "padding: 25px 0;" +
        "color: '#ff0000';" +
        "font-size: 30px;" +
    "}"
)

MODIFIERS_SECTION_DISPLAY_NAME: str = 'MODIFIERS'
MODIFIERS_SECTION_LABEL_WIDGET_DATA: WidgetData = WidgetData(2, 2, 3, 8)
MODIFIERS_SECTION_LABEL_STYLE_SHEET: str = (
    "*{" +
        "border: 6px dotted '#ff0000';" +
        "border-radius: 10px;" +
        "padding: 25px 0px;" +
        "color: '#ff0000';" +
        "font-size: 25px;" +
    "}"
)

FIRE_ALL_BUTTON_DISPLAY_NAME: str = 'FIRE ALL'
FIRE_ALL_BUTTON_WIDGET_DATA: WidgetData = WidgetData(7, 5, 2, 2)
FIRE_ALL_BUTTON_STYLE_SHEET: str = (
    "*{" +
        "border: 9px solid '#ff0000';" +
        "border-radius: 30px;" +
        "padding: 45px 25px;" +
        "color: '#ff1111';" +
        "font-family: Shanti;" +
        "font-size: 23px;" +
    "}" +
    "*:pressed{" +
        "border: '#aa0000';" +
        "background: '#aa0000';" +
        "color: '#000000';" +
    "}"
)

FIRE_BUTTON_STARTING_ROW: int = 6
# FIXME: Changing this only translates buttons vertically rather than resizing
FIRE_BUTTON_ROW_HEIGHT: int = 1

FIRE_BUTTON_LEFTMOST_COLUMN: int = 2
FIRE_BUTTON_COLUMNS_SPACING: int = 2
FIRE_BUTTON_COLUMN_WIDTH: int = 2

FIRE_BUTTON_FWD_AFT_ROW_SPACING: int = 3

FIRE_BUTTON_STYLE_SHEET: str = (
    "*{" +
        "border: 6px solid '#ff0000';" +
        "border-radius: 30px;" +
        "padding: 25px 25px;" +
        "color: '#ff1111';" +
        "font-family: Shanti;" +
        "font-size: 20px;" +
    "}" +
    "*:pressed{" +
        "border: '#aa0000';" +
        "background: '#aa0000';" +
        "color: '#000000';" +
    "}"
)
FIRE_BUTTON_UNUSED_STYLE_SHEET: str = (
    "*{" +
        "border: 6px solid '#770000';" +
        "border-radius: 30px;" +
        "padding: 25px 25px;" +
        "color: '#770000';" +
        "font-family: Shanti;" +
        "font-size: 20px;" +
    "}"
)

