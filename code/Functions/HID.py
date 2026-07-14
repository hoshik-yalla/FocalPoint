from pynput import mouse, keyboard
import time

mouse = mouse.Controller()

def mouse_activity():
    #Mouse Position
    ps1 = mouse.position
    time.sleep(2)
    ps2 = mouse.position
        
    #Logic
    if ps1 != ps2:
        status = "Active"
    else:
        status = "Inactive"

def key_activity():
    status = False