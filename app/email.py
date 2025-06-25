#email.py

from flask_mail import Message
from flask import current_app
from app import mail
import random as rn
from flask import Blueprint, render_template, request, redirect, session  



def send_email(email):
    x = [rn.randint(1, 9) for _ in range(6)]
    verify_code = ''.join(str(i) for i in x)
    subject = "Your Verification Code"
    body = f"Hello,\n\nThank you for using our service. Your verification code is:\n\n[ {verify_code} ]\n\nPlease do not share this code with anyone. If you did not request this code, please ignore this message.\n\nBest regards,\nThe Support Team"

    
    msg = Message(
        subject=subject,
        recipients=[email],
        body=body,
        sender=current_app.config["MAIL_USERNAME"]
    )

    mail.send(msg)
    return verify_code

def reset_password(email):
    x = [rn.randint(1, 9) for _ in range(6)]
    reset_code = ''.join(str(i) for i in x)
    
    subject = "Password Reset Verification Code"
    body = f"""Hello,

We received a request to reset the password for your account. 
To proceed, please use the following verification code:

[ {reset_code} ]

If you did not request a password reset, please ignore this message.

Thank you,
Support Team
"""

    msg = Message(
        subject=subject,
        recipients=[email],
        body=body,
        sender=current_app.config["MAIL_USERNAME"]
    )

    mail.send(msg)
    return reset_code