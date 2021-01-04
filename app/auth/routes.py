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

from jinja2 import TemplateNotFound