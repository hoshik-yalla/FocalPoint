import webview


class Api():
    def destroy(self):
        print("API Received")
        window.destroy()

def initialize():
    webview.start()

window = webview.create_window("Test Window", 
                          "http://127.0.0.1:5500/code/miniplayer/index.html",
                          width=300, height=310, 
                          transparent=True, 
                          frameless=True,
                          resizable=False,
                          zoomable=False,
                          focus=False,
                          js_api=Api())

initialize()