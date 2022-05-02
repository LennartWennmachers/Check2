from flask import Blueprint, render_template
from check2 import app, db
from flask_login import login_user, current_user, login_required, logout_user, login_manager,

auth=Blueprint("auth",__name__)

@auth.route("/login")
def login ():
    return render_template("login.html")

