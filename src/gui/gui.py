from src.gui.styling import MAIN_WIDGET_TITLE, MAIN_WIDGET_BG_COLOR

from PyQt5.QtWidgets import QLabel, QPushButton, QWidget

from dataclasses import dataclass

# For typing
from typing import Any, Tuple
from PyQt5.QtCore import Qt


@dataclass
class WidgetGeometry:
    x_pos: int = 0
    y_pos: int = 0
    width: int = 0
    vertical_padding: int = 0

    def asTuple(self) -> Tuple[int, int, int, int]:
        return (
            self.x_pos,
            self.y_pos,
            self.width,
            self.vertical_padding,
        )
    def asTupleForAddingToGridWithLayout(self) -> Tuple[int, int, int, int]:
        return (
            self.y_pos,
            self.x_pos,
            self.vertical_padding,
            self.width,
        )

@dataclass
class WidgetStyling:
    displayed_text: str = ''
    style_sheet: str = ''
    geometry: WidgetGeometry = None
    alignment: str = None


def create_main_widget() -> QWidget:
    widget = QWidget()

    widget.setWindowTitle(MAIN_WIDGET_TITLE)
    widget.setStyleSheet(f'background: {MAIN_WIDGET_BG_COLOR};')

    return widget

def create_label(styling_data: WidgetStyling)-> QLabel:
    label = QLabel()
    sd = styling_data

    label.setText(sd.displayed_text)
    label.setStyleSheet(sd.style_sheet)
    if sd.alignment:
        label.setAlignment(sd.alignment)

    return label

def create_button(styling_data: WidgetStyling, function: Any=None) -> QPushButton:
    button = QPushButton()
    sd = styling_data

    if function:
        button.clicked.connect(function)

    button.setText(sd.displayed_text)
    button.setStyleSheet(sd.style_sheet)

    return button

