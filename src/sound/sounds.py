from playsound import playsound
from threading import Thread


def play_tng_fire_weapon() -> None:
    def play() -> None:
        playsound('assets/tng_console_fire_weapon.wav')

    thread = Thread(target=play)

    thread.start()

