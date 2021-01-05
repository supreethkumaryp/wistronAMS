# -*- encoding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, IntegerField, FloatField, PasswordField, SelectField, DateField, FileField, HiddenField, BooleanField
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

class UserForm(FlaskForm):
    """User Form"""

    usr_miId = TextField(
        'MI ID',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )
    usr_alternateMiId = TextField(
        'Alternate MI ID',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )
    usr_name = TextField(
        'Name',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )
    dept_id = SelectField(
        'Department',
        choices=[("", "-- Select --")],
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This field is required"}
    )
    func_id = SelectField(
        'Function',
        choices=[("", "-- Select --")],
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This field is required"}
    )
    usr_type = SelectField(
        'Type',
        choices=[("", "-- Select --"), ("dl", "DL"), ("idl", "IDL")],
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This field is required"}
    )
    plant_id = SelectField(
        'Plant',
        choices=[("", "-- Select --")],
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This field is required"}
    )
    usr_designation = SelectField(
        'Designation',
        choices=[
            ("", "-- Select --"),
            ("em", "Engineering Manager"),
            ("m", "Manager"),
            ("am", "Assistant Manager"),
            ("tl", "Team Leader"),
            ("se", "Senior Engineer"),
            ("je", "Junior Engineer"),
            ("get", "GET"),
            ("det", "DET"),
            ("op", "Operator")
        ],
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This field is required"}
    )
    usr_gender = SelectField(
        'Gender',
        choices=[("", "-- Select --"), ("male", "Male"), ("female", "Female")],
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This field is required"}
    )
    branch_id = SelectField(
        'Branch',
        choices=[("", "-- Select --")],
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This field is required"}
    )
    usr_experience = FloatField(
        'Experience',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )
    usr_dob = DateField(
        'Date of Birth',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This field is required"}
    )
    project_id = SelectField(
        'Project',
        choices=[("", "-- Select --")],
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This field is required"}
    )
    usr_permanentAddress = TextAreaField(
        'Permanent Address',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This field is required"}
    )
    usr_currentAddress = TextAreaField(
        'Current Address',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This field is required"}
    )
    usr_pickUpRoute = TextField(
        'PickUp Route',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )
    usr_pickUpPoint = TextField(
        'PickUp Point',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )
    usr_contactNumber = TextField(
        'Contact Number',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )
    usr_emergencyContactNumber = TextField(
        'Emergency Contact',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This Field is required"}
    )
    usr_bloodGroup = SelectField(
        'Blood Group',
        choices=[
            ("", "-- Select --"),
            ("A+", "A+"),
            ("A-", "A-"),
            ("B+", "B+"),
            ("B-", "B-"),
            ("O+", "O+"),
            ("O-", "O-"),
            ("AB+", "AB+"),
            ("AB-", "AB-")
        ],
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This field is required"}
    )
    usr_doj = DateField(
        'Date of Joining',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This field is required"}
    )
    usr_status = SelectField(
        'Status',
        choices=[
            ("", "-- Select --"),
            ("active", "Active"),
            ("inactive", "In-Active"),
            ("abscond", "Abscond")
        ],
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This field is required"}
    )
    shift_id = SelectField(
        'Shift',
        choices=[("", "-- Select --")],
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This field is required"}
    )
    usr_isProxy = BooleanField(
        'Is Shift Incharge',
        validators=[DataRequired()]
    )

class RosterDateForm(FlaskForm):
    """Roster Date Form"""

    rst_date = DateField(
        'Roster Date',
        validators=[DataRequired()],
        render_kw={"required":"true", "data-validation-required-message":"This field is required"}
    )