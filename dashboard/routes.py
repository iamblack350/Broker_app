from flask import render_template, flash, url_for, request, redirect
from flask_login import login_required, current_user
from decimal import Decimal
from model.database import db
from model.models import Withdrawal, Deposit
from . import dashboard_bp


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():
    user = current_user
    portfolio_value = user.balance * Decimal(1.15)
    return render_template("dashboard.html",user=user, portfolio_value=portfolio_value)

@dashboard_bp.route("/withdraw", methods=["GET", "POST"])
@login_required
def withdraw():
    if request.method == "POST":
        amount = request.form.get("amount", "").strip()

        user = current_user
        if int(amount) > user.balance:
            flash("Insufficient funds!")
            return redirect(request.url)

        new_balance = user.balance - int(amount)

        withdrawal = Withdrawal(user_id=user.id,
                                amount= int(amount))
        db.session.add(withdrawal)
        db.commit()

        user.balance = new_balance
        db.commit()
    return render_template("withdraw.html")

@dashboard_bp.route("/deposit")
@login_required
def deposit():
    return render_template("deposit.html")

@dashboard_bp.route("/transactions")
@login_required
def transactions():
    user = current_user
    withdrawal = Withdrawal.query.filter_by(user_id=current_user.id)
    deposits = Deposit.query.filter_by(user_id=current_user.id)

    return render_template("transactions.html")

@dashboard_bp.route("/message-admin")
@login_required
def message_admin():
    pass