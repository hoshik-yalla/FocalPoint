import webview

class Api():
    def destroy(self):
        print("Session Ended")
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


window = webview.create_window("FocalPoint - Miniplayer", 
                          "miniplayer/index.html",
                          width=300, height=310, 
                          transparent=True, 
                          frameless=True,
                          resizable=False,
                          zoomable=False,
                          focus=False,
                          js_api=Api())