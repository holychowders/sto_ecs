from src.gui.styling import MAIN_WIDGET_TITLE, MAIN_WIDGET_BG_COLOR

from PyQt5.QtWidgets import QLabel, QPushButton, QWidget

# For typing
from typing import Any
from PyQt5.QtCore import Qt

def create_main_widget() -> QWidget:
    widget = QWidget()

    widget.setWindowTitle(MAIN_WIDGET_TITLE)
    widget.setStyleSheet(f'background: {MAIN_WIDGET_BG_COLOR};')

    return widget

# TODO: style_sheet param is a bit under-specific. Do we care right now? IDK.
def create_label(text: str, style_sheet: str, alignment: Qt.AlignmentFlag=None) -> QLabel:
    label = QLabel(text)

    label.setStyleSheet(style_sheet)

    if alignment:
        label.setAlignment(alignment)

    return label

def create_button(text: str, style_sheet: str, function: Any=None) -> QPushButton:
    button = QPushButton(text)
    button.setStyleSheet(style_sheet)

    if function:
        button.clicked.connect(function)

    return button

