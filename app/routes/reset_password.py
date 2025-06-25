from flask import Blueprint, render_template, redirect, session
from app.models import User
from app import db
from werkzeug.security import check_password_hash, generate_password_hash
from app.forms import ResetPasswordForm

bp = Blueprint('reset_password', __name__)

@bp.route('/reset_password', methods=['GET', 'POST'])
def Forgot_Password():
    form = ResetPasswordForm()
    error_message = ''
    email = session.get('email')
    user = User.query.filter_by(email=email).first()

    if form.validate_on_submit():
        new_password = form.new_password.data

        if check_password_hash(user.password, new_password):
            error_message = 'The new password must be different from the current one.'
        else:
            hashed_password = generate_password_hash(new_password)
            user.password = hashed_password
            db.session.commit()
            session.clear()
            return redirect('/SignIn')

    return render_template('reset_password.html', form=form, error_message=error_message)