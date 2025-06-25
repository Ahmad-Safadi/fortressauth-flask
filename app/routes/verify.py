from flask import Blueprint, render_template, redirect, session
from app.models import User
from app import db
from app.forms import VerificationForm

bp = Blueprint('verify', __name__)

@bp.route('/verify', methods=['GET', 'POST'])
def verify():
    verify_code = session.get('verify_code')
    if not verify_code:
        return redirect('/SignIn')

    form = VerificationForm()
    error_message = ''

    if form.validate_on_submit():
        user_code = (
            form.digit1.data + form.digit2.data + form.digit3.data +
            form.digit4.data + form.digit5.data + form.digit6.data
        )
        if user_code == verify_code:
            name = session.get('name')
            email = session.get('email')
            password = session.get('password')
            new_user = User(name=name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            session.pop('name', None)
            session.pop('email', None)
            session.pop('password', None)
            return redirect('/SignIn')
        else:
            error_message = 'The code is wrong'

    return render_template('verify.html', form=form, error_message=error_message)