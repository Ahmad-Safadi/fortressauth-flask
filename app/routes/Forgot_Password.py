from flask import Blueprint, render_template, redirect, session
from app.models import User
from app.email import reset_password
from app.forms import ForgotPasswordForm

bp = Blueprint('Forgot_Password', __name__)

@bp.route('/Forgot_Password', methods=['GET', 'POST'])
def Forgot_Password():
    form = ForgotPasswordForm()
    error_message = ''

    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if not user:
            error_message = 'This Email Not Found'
        else:
            code = reset_password(email)
            session['reset_code'] = code
            session['email'] = email
            return redirect('/verify_reset_password_code')

    return render_template('Forget_Password.html', form=form, error_message=error_message)