from flask import Flask

app = Flask(__name__)
app.secret_key = b'0H*J3jjw[_931]g'

from app import routes