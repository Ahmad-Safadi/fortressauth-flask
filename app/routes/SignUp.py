from flask import Blueprint, render_template, redirect, session
from app.models import User
from app import db
from werkzeug.security import generate_password_hash
from app.email import send_email
from app.forms import SignUpForm

bp = Blueprint('SignUp', __name__)

@bp.route('/SignUp', methods=['GET', 'POST'])
def home():
    form = SignUpForm()
    email_error = ''
    password_error = ''
    name_error = ''
    has_error = False
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        email = form.email.data
        hashed_password = generate_password_hash(password)

        
        user = User.query.filter_by(email=email).first()
        
        if len(name.strip()) < 2:
            name_error = 'Name must be at least 2 characters.'
            has_error = True
        
        if len(password) < 8:
            password_error = 'Password must be at least 8 characters'
            has_error = True
        
        if user:
            email_error = 'This email is already used'
            has_error = True
        
        if not has_error:
            session['name'] = name
            session['email'] = email
            session['password'] = hashed_password
            code = send_email(email)
            session['verify_code'] = code
            return redirect('/verify')

    return render_template('SignUp.html', form=form, email_error=email_error,password_error=password_error,name_error=name_error)