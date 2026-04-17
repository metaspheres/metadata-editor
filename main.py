from flask import Flask
import os

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY', 'dev-fallback-key')

from views import *

if __name__ ==  "__main__":
    app.run() 