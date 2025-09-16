from flask import render_template, jsonify, url_for, request, redirect
from . import dashboard_bp

@dashboard_bp.route("/dashboard")
def dashboard():
    pass

@dashboard_bp.route("/withdraw")
def withdraw():
    pass

@dashboard_bp.route("/deposit")
def deposit():
    pass

@dashboard_bp.route("/transactions")
def transactions():
    pass

@dashboard_bp.route("message-admin")
def message_admin():
    pass