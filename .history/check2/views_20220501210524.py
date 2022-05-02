from flask import Blueprint, redirect, session, url_for
from check2 import app, auth, db


views = Blueprint("views",__name__)

@views.route("/")
def home ():
        return redirect(url_for('login.html'))
