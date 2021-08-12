import ctypes
import pygetwindow
from time import sleep


PRESS_KEY_DURATION_MS = 0.01


SendInput = ctypes.windll.user32.SendInput

def press_key(hex_key_code: str) -> None:
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hex_key_code, 0x0008, 0, ctypes.pointer(extra))

    x = Input(ctypes.c_ulong(1), ii_)

    _focus_game_window()
    # FIXME: Find a smarter way to do this
    sleep(.05)

    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(hex_key_code: str) -> None:
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hex_key_code, 0x0008 | 0x0002, 0, ctypes.pointer(extra))

    x = Input(ctypes.c_ulong(1), ii_)

    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# TODO: If this project is going to run on an independent device (it should) such that all a user has to do is plug in a Raspberry Pi or something,
# we probably won't need to do this and could probably just do what we were doing before -- just send keypresses. If the user has the
# game in focus, our project's GUI shouldn'ttake away focus from the game when it is used since it's on another device.
def _focus_game_window() -> None:
    # FIXME: Potential bug: Any other window with the exact name will be included in the list of window objects returned
    for window in pygetwindow.getWindowsWithTitle('Star Trek Online'):
        if window.title == 'Star Trek Online':
            game_window = window
            break

    game_window.activate()

# C struct redefinitions

# Was called PUL
PTR_C_ULONG = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", PTR_C_ULONG)
    ]

class HardwareInput(ctypes.Structure):
    _fields_ = [
        ("uMsg", ctypes.c_ulong),
        ("wParamL", ctypes.c_short),
        ("wParamH", ctypes.c_ushort)
    ]

class MouseInput(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("time",ctypes.c_ulong),
        ("dwExtraInfo", PTR_C_ULONG)
    ]

class Input_I(ctypes.Union):
    _fields_ = [
        ("ki", KeyBdInput),
        ("mi", MouseInput),
        ("hi", HardwareInput)
    ]

class Input(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ulong),
        ("ii", Input_I)
    ]

