from flask import Flask
import os
import threading 
import webview

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True 

app.secret_key = os.environ.get('SECRET_KEY', 'dev-fallback-key')

from views import *


# ---- PyWebView ---- #
# def run_flask():
#     app.run(port=5000)

# if __name__ == "__main__":
#     thread = threading.Thread(target=run_flask)
#     thread.daemon = True
#     thread.start()

#     webview.create_window(
#         "WaVu",
#         "http://localhost:5000",
#         width=1920,
#         height=1080
#     )

#     webview.start()
# ---- PyWebView ---- #


if __name__ ==  "__main__":
    app.run(debug=True)  