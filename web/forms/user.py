# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import TextField, PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from web.models.user import User


class RegisterForm(Form):
    username = TextField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    first_name = TextField('first_name', validators=[DataRequired(), Length(min=3, max=25)])
    last_name = TextField('last_name', validators=[DataRequired(), Length(min=3, max=25)])
    email = TextField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Verify password', [DataRequired(), EqualTo('password', message='Passwords must match')])

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append("Username already registered")
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        return True

class EmailForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])


class PasswordForm(Form):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password',
                              validators=[DataRequired(), EqualTo('password', message='Passwords must match')])


class UsernameForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    username2 = StringField('Confirm Username',
                            validators=[DataRequired(), EqualTo('username', message='Usernames must match')])
