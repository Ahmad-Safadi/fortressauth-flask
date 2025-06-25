from flask import Blueprint, render_template, redirect, session
from app.models import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import ChangePasswordForm

bp = Blueprint('MainPage', __name__)

@bp.route('/MainPage', methods=['GET', 'POST'])
def home():
    form = ChangePasswordForm()
    message = ''

    if form.validate_on_submit():
        oldpassword = form.old_password.data
        newpassword = form.new_password.data
        user_id = session.get('id')
        user = User.query.get(user_id)

        if check_password_hash(user.password, oldpassword):
            hashed_password = generate_password_hash(newpassword)
            user.password = hashed_password
            db.session.commit()
            message = 'Password updated successfully.'
        else:
            message = 'The old password is wrong.'

    return render_template('MainPage.html', form=form, message=message)