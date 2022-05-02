from flask import Blueprint, Flask, redirect, session, url_for
from check2 import app, auth, db

app = Flask(__name__)
views = Blueprint("views",__name__)

@views.route('/home')
@views.route("/")
def home ():
        return redirect(url_for('to_do.html'))
