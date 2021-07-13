from playsound import playsound

from typing import Any


def play(*sounds: Any) -> None:
    [sound() for sound in sounds]


play_tng_keypress_1 = lambda: playsound('assets/tng_console_keypress_1.wav')
play_tng_processed_input_1 = lambda: playsound('assets/tng_console_processed_input_1.wav')
play_tng_invalid_keypress_1 = lambda: playsound('assets/tng_console_invalid_keypress_1.wav')
play_tng_fire_weapon = lambda: playsound('assets/tng_console_fire_weapon.wav')
