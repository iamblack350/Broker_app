from flask import request, redirect, render_template, jsonify
from . import auth_bp

@auth_bp.route("/register")
def register():
    pass

@auth_bp.route("/login")
def login():
    pass

@auth_bp.route("/logout")
def logout():
    pass

@auth_bp.route("/forgot-password")
def forgot_password():
    pass