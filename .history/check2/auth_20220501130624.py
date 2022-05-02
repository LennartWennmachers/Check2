from flask import Blueprint, render_template, flash, url_for, redirect, request
from check2 import app, db, views
from flask_login import login_user, current_user, login_required, logout_user, login_manager

from check2.models import User

auth=Blueprint("auth",__name__)


@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method=="POST":
        user=User.query.filter_by(username=request.form.get('username')).first()
        if user and check_password_hash(user.password, request.form.get('password')):
            login_user(user)
            next =request.args.get('next')
            return redirect(next or url_for('views.home'))
        flash('You seem to have entered an invalid password-username-combination', 'danger')
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
    
@auth.route('/signup', methods=['POST'])
def signup():
    if request.method=='POST':
        user=User.query.filter_by(username=request.form.get('username')).first()
        if username:
            flash("This username seems to already be in use. Please try a different one.", category="error")
            return redirect(url_for("auth.signup"))
        if email:
            flash("There already seems to be an account connected to this E-mail address. Please log in with your password or choose a different E-mail.", category='error')
            return redirect(url_for("auth.signup"))
        name=request.form.get("name")
        username=request.form.get("username")
        email=request.form.get("email")
        password=request.form.get("password")
        repeat_password=request.form.get("repeat_password")
        if password != repeat_password:
            flash("The two passwords you have entered do not seem to match please try again.", category="error")
            redirect(url_for("auth.register"))
        password_hash=generate_password_hash(password)
        users=User(name=name, username=username, email=email, password=password_hash)
        db.session.add(users)
        db.session.commit()
        flash("You have signed uo successfully! Congratulations!", 'success')
        return redirect(url_for('views.home')) 
    return render_template("to-do.html")       

            



