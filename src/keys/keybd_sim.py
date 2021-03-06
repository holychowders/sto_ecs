from pyautogui import getWindowsWithTitle
from pydirectinput import press

from time import sleep
from warnings import warn


def press_key(char: str) -> None:
    _focus_game_window()
    sleep(.4)  # FIXME: Find a smarter way to ensure the game is ready to accept input
    press(char)

# FIXME: Make the game window global
def _focus_game_window() -> None:
    # FIXME: We must be sure another window with the same title can't get selected
    for window in getWindowsWithTitle('Star Trek Online'):
        if window.title == 'Star Trek Online':
            window.activate()
            break
    else:
        warn('Game window not found and will not be focused.', RuntimeWarning)


