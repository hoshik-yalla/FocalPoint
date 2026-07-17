import win32gui

def init():
    windows = []

    def enum(hwnd,_):
        title = win32gui.GetWindowText(hwnd)
        if win32gui.IsWindowVisible(hwnd) and title.strip():
            windows.append((hwnd, title))
        
    try:
        win32gui.EnumWindows(enum, None)
    except Exception as e:
        print(f"Error enumerating windows: {e}")

    return windows

def menu():
    pch = init()
    toutput = []
    houtput = []
    for hwnd, title in pch:
        toutput.append(title)
        houtput.append(hwnd)
    return toutput, houtput

def get_focus(hwnd):
    return (hwnd == win32gui.GetForegroundWindow())