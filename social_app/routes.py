

# General imports
import time

# Flask Imports
from flask import render_template, flash, url_for, redirect, request
from flask_login import login_required, logout_user, login_user, current_user
from werkzeug.security import check_password_hash

# Imports From My Package
from social_app import app
from social_app.forms import RegisterForm, LoginForm
from social_app.utils import add_user_to_db
from social_app.db_models import User


@app.route("/")
def home_page():
    return render_template("home.html", logged_in=current_user.is_authenticated)

@app.route("/register", methods=["POST", "GET"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        data = register_form.data

        if add_user_to_db(data):
            flash(message="Account created successfully, you can login.", category="register-success" )
            return redirect(url_for('login'))
        else:
            flash(message="Email or Username is already taken", category="register-error")
            return redirect(url_for('register'))   

    return render_template("register.html", form=register_form, logged_in=current_user.is_authenticated)

@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        email = request.form["email"]
        password = request.form["password"]
        user_info = User.query.filter_by(email=email).first()
        if user_info == None:
            flash(message="Account doesn't exist", category="login-info")
            return redirect(url_for('login'))
        else:
            pass
        
        if check_password_hash(user_info.password, password):
            login_user(user_info)
            return redirect(url_for('secret_page'))
        else:
            flash(message="Wrong Password", category="login-error")
            return redirect(url_for('login'))            

    return render_template("login.html", form=login_form)

#** Routes Bellow Require Logins
#** Routes Bellow Require Logins
@app.route("/secret", methods=["GET", "POST"])
@login_required
def secret_page():
    if request.method == "POST":
        data = request.form
        print(data)
    return render_template("secret.html", name=current_user.username, logged_in=current_user.is_authenticated)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home_page'))

#** Custon Error pages
#** Custon Error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


