from flask import Blueprint, redirect, render_template, session, url_for
from check2 import app, auth, db


views = Blueprint("views",__name__)

@views.route("/")
def home ():
    if "user" in session:
        return render_template('to-do.html')
    else:
        return redirect(url_for('auth.login'))