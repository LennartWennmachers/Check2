from flask import Blueprint, Flask, redirect, render_template, session, url_for
from check2 import app, auth, db

app = Flask(__name__)
views = Blueprint("views",__name__)




