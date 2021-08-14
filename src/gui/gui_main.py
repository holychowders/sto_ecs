from src.gui import gui
from src.gui.weapons import weapons as gui_weapons

from src.components import weapons

from PyQt5.QtWidgets import QApplication, QGridLayout
import sys


def main() -> int:
    sto_gui = QApplication(sys.argv)
    main_widget = gui.create_main_widget()
    grid = QGridLayout()

    weapons_equipped = weapons.get_equipped()
    # This might be mistaken for an instance of the weapons portion of the GUI
    gui_weapons.add_section_to_grid(weapons_equipped, grid)

    main_widget.setLayout(grid)

    main_widget.showMaximized()

    return sys.exit(sto_gui.exec())
