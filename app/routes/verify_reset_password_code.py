from flask import Blueprint, render_template, redirect, session
from app.forms import ResetPasswordVerificationForm

bp = Blueprint('verify_reset_password_code', __name__)

@bp.route('/verify_reset_password_code', methods=['GET', 'POST'])
def Forgot_Password():
    form = ResetPasswordVerificationForm()
    error_message = ''
    code = session.get('reset_code')

    if form.validate_on_submit():
        user_code = (
            form.digit1.data + form.digit2.data + form.digit3.data +
            form.digit4.data + form.digit5.data + form.digit6.data
        )
        if code == user_code:
            session.pop('reset_code', None)
            return redirect('/reset_password')
        else:
            error_message = 'The Code Is Wrong'

    return render_template('verify_reset_password_code.html', form=form, error_message=error_message)