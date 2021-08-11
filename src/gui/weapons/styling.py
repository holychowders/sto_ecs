from src.gui.gui import WidgetStyling, WidgetGeometry

from PyQt5.QtCore import Qt


HEADER_STYLING: WidgetStyling = WidgetStyling(
    displayed_text = 'WEAPONS',
    geometry = WidgetGeometry(
        x_pos = 0,
        y_pos = 0,
        width = 12,
        vertical_padding = 12,
    ),
    alignment = Qt.AlignHCenter,
    style_sheet = (
        "*{" +
            "border: 10px dotted '#ff0000';" +
            "border-radius: 30px;" +
            "padding: 25px 0;" +
            "color: '#ff0000';" +
            "font-size: 30px;" +
        "}"
    ),
)

MODIFIERS_STYLING: WidgetStyling = WidgetStyling(
    displayed_text = 'MODIFIERS',
    geometry = WidgetGeometry(
        x_pos = 2,
        y_pos = 2,
        width = 8,
        vertical_padding = 3,
    ),
    alignment = Qt.AlignHCenter,
    style_sheet = (
        "*{" +
            "border: 6px dotted '#ff0000';" +
            "border-radius: 10px;" +
            "padding: 25px 0px;" +
            "color: '#ff0000';" +
            "font-size: 25px;" +
        "}"
    ),
)


FIRE_ALL_BUTTON_STYLING = WidgetStyling(
    displayed_text = 'FIRE ALL',
    geometry = WidgetGeometry(
        x_pos = 5,
        y_pos = 6,
        width = 2,
        vertical_padding = 4,
    ),
    style_sheet = (
        "*{" +
            "border: 9px solid '#ff0000';" +
            "border-radius: 30px;" +
            "padding: 45px 25px;" +
            "color: '#ff1111';" +
            "font-family: Shanti;" +
            "font-size: 23px;" +
        "}" +
        "*:pressed{" +
            "border: '#ff0000';" +
            "background: '#ff0000';" +
            "color: '#000000';" +
        "}"
    ),
)


FIRE_BUTTON_LEFTMOST_POSITION_PX: int = 2
FIRE_BUTTON_INITIAL_STYLING_DATA: WidgetStyling = (
    WidgetStyling(
        geometry = WidgetGeometry(
            x_pos = FIRE_BUTTON_LEFTMOST_POSITION_PX,
            y_pos = 5,
            width = 2,
            vertical_padding = 3,
        ),
    )
)

FIRE_BUTTON_VERTICAL_SPACING_FWD_AFT_PX: int = 3
FIRE_BUTTON_HORIZONTAL_SPACING_PX: int = 2

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
        "border: '#ff0000';" +
        "background: '#ff0000';" +
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

