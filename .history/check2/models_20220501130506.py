from check2 import db, login_manager
from flask_login import UserMixin
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id)) 

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(150))
    def __repr__(self):
        return '<User %r>' % self.username
  


db.create_all()
db.session.commit