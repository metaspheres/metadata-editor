from flask import Flask
import secrets

app = Flask(__name__)

app.secret_key = secrets.token_hex(16)

from views import *

if __name__ ==  "__main__":
    app.run(debug=True) # nao esquecer de remover debug...
