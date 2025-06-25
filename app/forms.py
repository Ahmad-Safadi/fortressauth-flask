from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, Regexp


class HomeForm(FlaskForm):
    sign_in = SubmitField('Sign In')
    sign_up = SubmitField('Sign Up')


class SignInForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message="Invalid email")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=18)])
    submit = SubmitField('Send')


class SignUpForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', )
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Send')


class VerificationForm(FlaskForm):
    digit1 = StringField('Digit 1', validators=[DataRequired(), Length(min=1, max=1), Regexp(r'\d')])
    digit2 = StringField('Digit 2', validators=[DataRequired(), Length(min=1, max=1), Regexp(r'\d')])
    digit3 = StringField('Digit 3', validators=[DataRequired(), Length(min=1, max=1), Regexp(r'\d')])
    digit4 = StringField('Digit 4', validators=[DataRequired(), Length(min=1, max=1), Regexp(r'\d')])
    digit5 = StringField('Digit 5', validators=[DataRequired(), Length(min=1, max=1), Regexp(r'\d')])
    digit6 = StringField('Digit 6', validators=[DataRequired(), Length(min=1, max=1), Regexp(r'\d')])
    submit = SubmitField('Verify')


class ResetPasswordVerificationForm(FlaskForm):
    digit1 = StringField('Digit 1', validators=[DataRequired(), Length(min=1, max=1), Regexp(r'\d')])
    digit2 = StringField('Digit 2', validators=[DataRequired(), Length(min=1, max=1), Regexp(r'\d')])
    digit3 = StringField('Digit 3', validators=[DataRequired(), Length(min=1, max=1), Regexp(r'\d')])
    digit4 = StringField('Digit 4', validators=[DataRequired(), Length(min=1, max=1), Regexp(r'\d')])
    digit5 = StringField('Digit 5', validators=[DataRequired(), Length(min=1, max=1), Regexp(r'\d')])
    digit6 = StringField('Digit 6', validators=[DataRequired(), Length(min=1, max=1), Regexp(r'\d')])
    submit = SubmitField('Verify')


class ResetPasswordForm(FlaskForm):
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Update')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired(), Length(min=8, max=18)])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=8, max=18)])
    submit = SubmitField('Update')


class ForgotPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message="Invalid email")])
    submit = SubmitField('Send Code')