from flask import Blueprint, render_template, redirect, session
from app.models import User
from app import db
from werkzeug.security import check_password_hash
from app.forms import SignInForm

bp = Blueprint('SignIn', __name__)

@bp.route('/SignIn', methods=['GET', 'POST'])
def home():
    form = SignInForm()
    error_message = ''

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password): 
            session['id'] = user.id
            session['name'] = user.name
            return redirect('/MainPage')
        else:
            error_message = 'The Email or Password is Wrong'

    return render_template('SignIn.html', form=form, error_message=error_message)