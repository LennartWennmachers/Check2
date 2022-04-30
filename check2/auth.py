from flask import Blueprint
from check2 import app, db


auth=Blueprint("auth",__name__)

@auth.route("/")
def login ():
    return "This is a login-page"