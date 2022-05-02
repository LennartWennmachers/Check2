from flask import Blueprint, redirect, session, url_for
from check2 import app, auth, db


views = Blueprint("views",__name__)

@views.route("/")
def home ():
    if "user" in session:
        return redirect(url_for('to-do.html'))
    else:
        return redirect(url_for('auth.login'))