from flask import request, redirect, render_template, session, url_for, flash
from flask_bcrypt import check_password_hash
from flask_login import login_user, login_required, current_user, logout_user
from . import auth_bp
from . import User
from . import db
import bcrypt

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        firstname = request.form.get("firstname", "").strip()
        lastname = request.form.get("lastname", "").strip()
        email = request.form.get("email", "").strip()
        # phone = request.form.get("phone", "").strip()
        password = request.form.get("password", "").strip()

        #check if user exist
        user = User.query.filter_by(email=email).first()
        if user:
            flash("user already exist", "error")
            return redirect(url_for('auth.register'))

        password_byte = password.encode('utf-8')
        password_hash = bcrypt.hashpw(password_byte, bcrypt.gensalt())


        user = User(firstname=firstname, lastname=lastname, email=email, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        flash("User Registered Successfully")
        return redirect(url_for('auth.login'))
    return render_template("register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        byte_password = password.encode("utf-8")
        user = User.query.filter_by(email=email).first()

        if user and bcrypt.checkpw(byte_password,user.password_hash):
            login_user(user)
            flash("logged in successfully!", "success")
            return redirect(url_for('dashboard.dashboard'))
        flash("Invalid Credential", "error")
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth_bp.route("/forgot-password")
def forgot_password():
    return render_template("forgot_password.html")

@auth_bp.route("/reset-password/<token>")
def reset_password(token):
    return render_template("reset_password.html")