from flask_mail import Message
from .extension import mail
from flask import render_template
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
