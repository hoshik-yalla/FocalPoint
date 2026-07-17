from pynput import mouse
import keyboard
import time

mousy = mouse.Controller()

def mouse_activity():
    #Mouse Position
    ps1 = mousy.position
    time.sleep(5)
    ps2 = mousy.position
    #Logic
    if ps1 != ps2:
        return True
    else:
        return False


def key_activity():
    fired = False

    def handler(_):
        nonlocal fired
        fired = True
    hook = keyboard.hook(handler)
    time.sleep(5)
    keyboard.unhook(hook)
    return fired