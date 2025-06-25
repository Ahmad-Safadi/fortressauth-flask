from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_wtf import CSRFProtect

csrf = CSRFProtect()
db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Change if using other database
    app.secret_key = 'YourSecretKey'  # CHANGE THIS secret key before deployment
    app.config['SECRET_KEY'] =  'YourSecretKey'  # CHANGE THIS secret key before deployment

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Change if using other mail server
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # CHANGE THIS to your email
    app.config['MAIL_PASSWORD'] = 'your-email-password'  # CHANGE THIS to your email password or app password
    
    db.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)

    from .routes import Home, SignIn, SignUp, MainPage,verify,Forgot_Password,verify_reset_password_code,reset_password
    
    app.register_blueprint(Home.bp)
    app.register_blueprint(SignUp.bp)
    app.register_blueprint(SignIn.bp)
    app.register_blueprint(MainPage.bp)
    app.register_blueprint(verify.bp)
    app.register_blueprint(Forgot_Password.bp)
    app.register_blueprint(verify_reset_password_code.bp)
    app.register_blueprint(reset_password.bp)
    return app