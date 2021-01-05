# -*- encoding: utf-8 -*-

from flask import jsonify, render_template, redirect, request, url_for, flash
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)
from datetime import date

from app import db, login_manager
from app.auth import blueprint
from app.auth.models import User
from app.auth.forms import LoginForm, ResetPasswordForm
from app.auth.utils import hash_pass, verify_pass

from jinja2 import TemplateNotFound

@blueprint.route('/')
def route_default():

    if not User.query.filter_by(usr_miId="dev").first():
        emp = User(
            usr_miId = "dev",
            usr_alternateMiId = "dev",
            usr_name = "Developer",
            usr_designation = "m",
            usr_isFirstLogin = False
        )

        emp.usr_password = hash_pass("Wistron@123")

        db.session.add(emp)
        db.session.commit()

    return redirect(url_for('auth_blueprint.login'))

@blueprint.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm(request.form)

    if 'login' in request.form:

        empid = request.form['usr_miId']
        password = request.form['usr_password']

        user = User.query.filter_by(usr_miId=empid).first()

        if user and verify_pass(password, user.usr_password):
            login_user(user)

            if user.usr_isFirstLogin == True:
                return redirect(url_for('auth_blueprint.resetPassword'))

            return redirect(url_for('auth_blueprint.route_default'))

        # Something (user or pass) is not ok
        return render_template('login.html', msg='Wrong MI Id or Password', form=form)

    if not current_user.is_authenticated:
        return render_template('login.html', form=form)
    
    return redirect(url_for('home_blueprint.employee'))

@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_blueprint.login'))

@blueprint.route('/reset-password', methods=['GET', 'POST'])
@login_required
def resetPassword():
    form = ResetPasswordForm(request.form)

    if 'save' in request.form:

        if (form.usr_password.data == form.usr_confirmPassword.data):
            emp = User.query.filter_by(usr_miId=current_user.usr_miId).first()
            emp.usr_password = hash_pass(form.usr_password.data)
            emp.usr_isFirstLogin = False
            db.session.commit()
            return redirect(url_for('home_blueprint.employee'))

        return render_template('reset-password.html', msg='Password and Confirm Password Must Match', form=form)

    return render_template('reset-password.html', form=form)