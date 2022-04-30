from flask import Blueprint
from check2 import app, db


views = Blueprint("views",__name__)

@views.route("/")
def home ():
    return "This is a hompage"
