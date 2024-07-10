"""This module contains the classes and their relevant methods to handel user login and registration"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from web_flask.models import User

class RegistrationFrom(FlaskForm):
    """class for registration form"""
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                              validators=[DataRequired()])
    confirm_password = PasswordField('confirm password',
                         validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """check if username already exists"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('username already exists, please choose a different username')

    def validate_email(self, email):
        """check if email already exists"""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email already exists, login instead')

class LoginForm(FlaskForm):
    """class for login form"""
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                              validators=[DataRequired()])
    remember = BooleanField('Remember User')
    submit = SubmitField('Login')
