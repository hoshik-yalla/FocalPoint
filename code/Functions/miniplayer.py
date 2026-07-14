import webview

def initialize():
    webview.create_window("Test Window", 
                          "placeholder-mp\index.html",
                          width=200, height=200, 
                          transparent=True, 
                          frameless=True,
                          resizable=False,
                          zoomable=False,
                          focus=False)
    webview.start()