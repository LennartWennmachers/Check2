from flask import Blueprint, render_template, flash, url_for, redirect
from check2 import app, db
from flask_login import login_user, current_user, login_required, logout_user, login_manager
import requests

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



