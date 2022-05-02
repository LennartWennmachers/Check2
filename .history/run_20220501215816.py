from check2 import app
from flask import Flask
from os import environ

app = Flask(__name__)
app.config.from_object('config')

if __name__ == '__main__':
    app.run(debug=True)
