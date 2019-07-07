from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class Registration(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    password = StringField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    submit = SubmitField('Sign Up')

class Login(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    password = StringField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    remember = BooleanField('Remember Me?')
    submit = SubmitField('Login')
