from datetime import datetime, timedelta
from flask import request, redirect, render_template, session, url_for, flash
from utils.utils import send_reset_email
import secrets
from flask_login import login_user, login_required, current_user, logout_user
from model.models import PasswordReset
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

@auth_bp.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email", "").strip()

        #check if account exist
        user = User.query.filter_by(email=email).first()
        if user:

            #Generate random token
            token = secrets.token_urlsafe(32)

            #store token to PasswordReset table
            reset_entry = PasswordReset(user_id = user.id,
                                        token=token,
                                        expires_at=datetime.utcnow() + timedelta(minutes= 5))
            db.session.add(reset_entry)
            db.session.commit()

            #send a verification to email address
            reset_link = url_for("auth.reset_password", token=token, _external=True)
            send_reset_email(user, reset_link)
            flash("We've sent a reset password link to your email")
            return redirect(url_for("auth.login"))
        flash("Email not found")
    return render_template("forgot_password.html")

@auth_bp.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):

    reset_entry = PasswordReset.query.filter_by(token=token, used=False).first()

    if not reset_entry or reset_entry.expires_at < datetime.utcnow():
        flash("The reset link is invalid or has expired")
        return redirect(url_for("auth.forgot_password"))
    if request.method == "POST":
        password = request.form.get("password", "").strip()
        confirm_password = request.form.get("confirm_password", "").strip()

        if password != confirm_password:
            flash("password do not match!")
            return redirect(request.url)

        #Update user password
        user = User.query.get(reset_entry.user_id)
        password_byte = password.encode("utf-8")
        hash_password = bcrypt.hashpw(password_byte, bcrypt.gensalt())
        user.password_hash = hash_password
        db.session.commit()

        reset_entry.used = True
        db.session.commit()

        flash("Your password has been reset successfully!")
        return redirect("auth.login")

    return render_template("reset_password.html")