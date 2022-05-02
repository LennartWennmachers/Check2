from flask import Blueprint, redirect, url_for
from check2 import app, db


views = Blueprint("views",__name__)

@views.route("/home")
def home ():
    return redirect(url_for('to-do.html'))
