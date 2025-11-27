from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import length, DataRequired,Email,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), length(min = 2, max= 20)])
    email = StringField('email', validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired()])
    Remember = BooleanField('Remember Me')
    submit = SubmitField('Login')