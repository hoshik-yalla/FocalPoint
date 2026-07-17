import webview

start = False

class Api():
    def destroy(self):
        print("API Received")
        if window != None:
            window.destroy()

def initialize(on_ready=None):
    webview.start(on_ready)

def update_activity(health):
    payload = "state("+str(health)+")"
    if window != None:
        window.run_js(payload)
    return "heartbeat sent"

def survived():
    if window != None:
        window.run_js("survived()")


window = webview.create_window("Test Window", 
                          "http://127.0.0.1:5500/code/miniplayer/index.html",
                          width=300, height=310, 
                          transparent=True, 
                          frameless=True,
                          resizable=False,
                          zoomable=False,
                          focus=False,
                          js_api=Api())