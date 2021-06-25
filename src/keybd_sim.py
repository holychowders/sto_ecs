import ctypes


KEY_CODES = {
    'w': 0x11,
    'a': 0x1E,
    's': 0x1F,
    'd': 0x20,

    'e': 0x12,
}


SendInput = ctypes.windll.user32.SendInput

def press_key(hex_key_code: str) -> None:
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hex_key_code, 0x0008, 0, ctypes.pointer(extra))

    x = Input(ctypes.c_ulong(1), ii_)

    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(hex_key_code: str) -> None:
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hex_key_code, 0x0008 | 0x0002, 0, ctypes.pointer(extra))

    x = Input(ctypes.c_ulong(1), ii_)

    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


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

