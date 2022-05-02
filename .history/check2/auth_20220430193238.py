from flask import Blueprint, render_template, flash, url_for, redirect, request
from check2 import app, db
from flask_login import login_user, current_user, login_required, logout_user, login_manager, check_password_hash

auth=Blueprint("auth",__name__)

@auth.route("/login")
def login ():
    return render_template("login.html")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method=="POST":
        user=User.query.filter_by(username=request.form.get('username')).first()
        if user and check_password_hash(user.password, request.form.get('password')):
            login_user(user)
            next =request.args.get('next')
            return redirect(next or url_for('views.dashboard'))
        flash('Wrong Password, Please try again', 'danger')
    return render_template('admin/login.html')





