# -*- encoding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import TextField, SelectField, TextAreaField, DateField, PasswordField
from wtforms.validators import InputRequired, DataRequired

class LoginForm(FlaskForm):
    """Login Form"""

    usr_miId = TextField(
        'MI Id',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )
    usr_password = PasswordField(
        'Enter Password',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )

class ResetPasswordForm(FlaskForm):
    """Reset Password Form"""

    usr_password = PasswordField(
        'Password',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )

    usr_confirmPassword = PasswordField(
        'Confirm Password',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )