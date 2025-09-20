from flask import render_template, flash, url_for, request, redirect
from flask_login import login_required, current_user
from decimal import Decimal
from model.database import db
from model.models import Withdrawal, Deposit
from . import dashboard_bp
from utils.utils import get_transactions


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():
    user = current_user
    portfolio_value = user.balance * Decimal(1.15)
    all_transactions = get_transactions(user)
    return render_template("dashboard.html",user=user,
                           portfolio_value=portfolio_value, transactions=all_transactions)

@dashboard_bp.route("/withdraw", methods=["GET", "POST"])
@login_required
def withdraw():
    if request.method == "POST":
        amount = request.form.get("amount", "").strip()

        if not amount.isdigit():
            flash("Please enter a valid amount")
            return redirect(request.url)

        amount = int(amount)
        user = current_user
        if amount > user.balance:
            flash("Insufficient funds!")
            return redirect(request.url)

        user.balance -= amount

        withdrawal = Withdrawal(user_id=user.id,
                                amount= amount)
        db.session.add(withdrawal)
        db.session.commit()
    return render_template("withdraw.html")

@dashboard_bp.route("/deposit")
@login_required
def deposit():
    return render_template("deposit.html")

@dashboard_bp.route("/transactions")
@login_required
def transactions():
    user = current_user
    all_transactions = get_transactions(user)
    return render_template("transactions.html", transactions=all_transactions, user=user)

@dashboard_bp.route("/message-admin")
@login_required
def message_admin():
    pass