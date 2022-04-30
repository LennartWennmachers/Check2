from check2 import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(150))
    def __repr__(self):
        return '<User %r>' % self.username
  
  
class Login_input(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128))

password = db.relationship('Password', backref='order', uselist=False, lazy=True)

db.create_all()
db.session.commit