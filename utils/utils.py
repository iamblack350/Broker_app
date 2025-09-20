from flask_mail import Message
from .extension import mail
from flask import render_template
from model.models import Withdrawal, Deposit
from itertools import chain
from flask_login import current_user
from datetime import datetime


def send_reset_email(user, reset_link):
    msg = Message(
        subject="Password Reset Request - BrokerPro",
        sender="noreply@brokerpro.com",
        recipients=[user.email]
    )

    # Render the HTML template
    msg.html = render_template(
        "password_reset_email.html",
        user=user,
        reset_link=reset_link,
        current_year=datetime.utcnow().year
    )

    mail.send(msg)

def get_transactions(user):
    withdrawal = Withdrawal.query.filter_by(user_id=current_user.id).all()
    deposits = Deposit.query.filter_by(user_id=current_user.id).all()

    all_transactions = list(chain(withdrawal, deposits))
    all_transactions.sort(key=lambda t: t.created_at, reverse=True)

    return all_transactions