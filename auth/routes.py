from flask import request, redirect, render_template, jsonify
from . import auth_bp

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        firstname = request.form.get("firstname", "").strip()
        lastname = request.form.get("lastname", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        password = request.form.get("email", "").strip()
    return render_template("register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    pass

@auth_bp.route("/forgot-password")
def forgot_password():
    pass

@auth_bp.route("/reset-password/<token>")
def reset_password(token):
    pass