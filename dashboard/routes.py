from flask import render_template, jsonify, url_for, request, redirect
from flask_login import login_required

from . import dashboard_bp


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@dashboard_bp.route("/withdraw")
@login_required()
def withdraw():
    return render_template("withdraw.html")

@dashboard_bp.route("/deposit")
@login_required
def deposit():
    return render_template("deposit.html")

@dashboard_bp.route("/transactions")
@login_required
def transactions():
    return render_template("transactions.html")

@dashboard_bp.route("/message-admin")
@login_required
def message_admin():
    pass