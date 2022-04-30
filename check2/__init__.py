from flask import Blueprint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask(__name__)
login_manager = LoginManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///check-mate.db'

app.config["SECRET_KEY"]='Vater1998!'
db = SQLAlchemy(app)

from .models import User





login_manager.login_view = "auth.login"
login_manager.login_message_category 

from .auth import auth 
from .views import views

app.register_blueprint(views, url_prefix ="/")
app.register_blueprint(auth, url_prefix ="/")