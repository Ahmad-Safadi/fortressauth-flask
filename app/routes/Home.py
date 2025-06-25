from flask import Blueprint, render_template, redirect
from app.forms import HomeForm

bp = Blueprint('home_routes', __name__)

@bp.route('/', methods=['GET', 'POST'])
def home():
    form = HomeForm()
    if form.validate_on_submit():
        if form.sign_in.data:
            return redirect('/SignIn')
        elif form.sign_up.data:
            return redirect('/SignUp')
    return render_template('home.html', form=form)