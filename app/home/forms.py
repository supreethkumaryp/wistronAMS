# -*- encoding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, IntegerField, PasswordField, SelectField, DateField, FileField, HiddenField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileRequired

class DepartmentForm(FlaskForm):
    """Department Form"""

    dept_id = HiddenField(
        'Department Id',
        validators=[DataRequired()],
        default="New",
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )
    dept_name = TextField(
        'Department Name',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )

class FunctionForm(FlaskForm):
    """Function Form"""

    func_id = HiddenField(
        'Function Id',
        validators=[DataRequired()],
        default="New",
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )
    func_name = TextField(
        'Function Name',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )

class PlantForm(FlaskForm):
    """Plant Form"""

    plant_id = HiddenField(
        'Plant Id',
        validators=[DataRequired()],
        default="New",
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )
    plant_name = TextField(
        'Plant Name',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )

class BranchForm(FlaskForm):
    """Branch Form"""

    branch_id = HiddenField(
        'Branch Id',
        validators=[DataRequired()],
        default="New",
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )
    branch_name = TextField(
        'Branch Name',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )

class ProjectForm(FlaskForm):
    """Project Form"""

    project_id = HiddenField(
        'Project Id',
        validators=[DataRequired()],
        default="New",
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )
    project_name = TextField(
        'Project Name',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )

class ShiftForm(FlaskForm):
    """Shift Form"""

    shift_id = HiddenField(
        'Shift Id',
        validators=[DataRequired()],
        default="New",
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )
    shift_name = TextField(
        'Shift Name',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )