from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

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

class LoginForm(FlaskForm):
    """class for registration form"""
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                              validators=[DataRequired()])
    remember = BooleanField('Remember User')
    submit = SubmitField('Login')
