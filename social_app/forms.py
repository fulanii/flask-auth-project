

from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegisterForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(message="Email is required"), Email(message="Email is invalid") ])
    password = PasswordField(label='Password', validators=[DataRequired(message="Password is required"), Length(min=8, message="minimun length is 8")] )
    username = StringField(label='Username', validators=[DataRequired(message="Username is required"),  Length(max = 30, min=3, message="minimun length is 3 and maximun is 30 ")])

    submit = SubmitField(label="Submit")


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(message="Email is required"), Email(message="Email is invalid") ]) 
    password = PasswordField(label='Password', validators=[DataRequired(message="Password is required")])

    submit = SubmitField(label="Submit")