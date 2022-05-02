from flask import Blueprint, render_template
from check2 import app, db


auth=Blueprint("auth",__name__)

@auth.route("/login")
def login ():
    return render_template("login.html")

