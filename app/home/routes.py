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
from app.home import blueprint
from app.home.models import Department, Function, Plant, Branch, Project, Shift
from app.home.forms import DepartmentForm, FunctionForm, PlantForm, BranchForm, ProjectForm, ShiftForm, UserForm

from app.auth.models import User
from app.auth.utils import hash_pass

from jinja2 import TemplateNotFound

# Department
@blueprint.route('/department', methods=['GET', 'POST'])
def department():
    return render_template('department/departments.html')

@blueprint.route('/get-departments', methods=['GET', 'POST'])
def get_departments():
    data = [r.as_dict() for r in Department.query.all()]
    return jsonify(data=data)

@blueprint.route('/department/<dept_id>', methods=['GET', 'POST'])
def department_create(dept_id):
    if (dept_id == "New"):
        form = DepartmentForm(request.form)
        if 'save' in request.form:
            dept = Department(**request.form)
            db.session.add(dept)
            db.session.commit()
            return redirect(url_for('home_blueprint.department'))
        return render_template('department/create-edit-department.html', form=form)

    dept = Department.query.filter_by(dept_id=dept_id).first()
    form = DepartmentForm(obj=dept)
    if 'save' in request.form:
        dept.dept_name = form.dept_name.data
        db.session.commit()
        return redirect(url_for('home_blueprint.department'))
    return render_template('department/create-edit-department.html', form=form)

# Function
@blueprint.route('/function', methods=['GET', 'POST'])
def function():
    return render_template('function/functions.html')

@blueprint.route('/get-functions', methods=['GET', 'POST'])
def get_functions():
    data = [r.as_dict() for r in Function.query.all()]
    return jsonify(data=data)

@blueprint.route('/function/<func_id>', methods=['GET', 'POST'])
def function_create(func_id):
    if (func_id == "New"):
        form = FunctionForm(request.form)
        if 'save' in request.form:
            func = Function(**request.form)
            db.session.add(func)
            db.session.commit()
            return redirect(url_for('home_blueprint.function'))
        return render_template('function/create-edit-function.html', form=form)

    func = Function.query.filter_by(func_id=func_id).first()
    form = FunctionForm(obj=func)
    if 'save' in request.form:
        func.func_name = form.func_name.data
        db.session.commit()
        return redirect(url_for('home_blueprint.function'))
    return render_template('function/create-edit-function.html', form=form)

# Plant
@blueprint.route('/plant', methods=['GET', 'POST'])
def plant():
    return render_template('plant/plants.html')

@blueprint.route('/get-plants', methods=['GET', 'POST'])
def get_plants():
    data = [r.as_dict() for r in Plant.query.all()]
    return jsonify(data=data)

@blueprint.route('/plant/<plant_id>', methods=['GET', 'POST'])
def plant_create(plant_id):
    if (plant_id == "New"):
        form = PlantForm(request.form)
        if 'save' in request.form:
            plant = Plant(**request.form)
            db.session.add(plant)
            db.session.commit()
            return redirect(url_for('home_blueprint.plant'))
        return render_template('plant/create-edit-plant.html', form=form)

    plant = Plant.query.filter_by(plant_id=plant_id).first()
    form = PlantForm(obj=plant)
    if 'save' in request.form:
        plant.plant_name = form.plant_name.data
        db.session.commit()
        return redirect(url_for('home_blueprint.plant'))
    return render_template('plant/create-edit-plant.html', form=form)

# Branch
@blueprint.route('/branch', methods=['GET', 'POST'])
def branch():
    return render_template('branch/branches.html')

@blueprint.route('/get-branches', methods=['GET', 'POST'])
def get_branches():
    data = [r.as_dict() for r in Branch.query.all()]
    return jsonify(data=data)

@blueprint.route('/branch/<branch_id>', methods=['GET', 'POST'])
def branch_create(branch_id):
    if (branch_id == "New"):
        form = BranchForm(request.form)
        if 'save' in request.form:
            branch = Branch(**request.form)
            db.session.add(branch)
            db.session.commit()
            return redirect(url_for('home_blueprint.branch'))
        return render_template('branch/create-edit-branch.html', form=form)

    branch = Branch.query.filter_by(branch_id=branch_id).first()
    form = BranchForm(obj=branch)
    if 'save' in request.form:
        branch.branch_name = form.branch_name.data
        db.session.commit()
        return redirect(url_for('home_blueprint.branch'))
    return render_template('branch/create-edit-branch.html', form=form)

# Project
@blueprint.route('/project', methods=['GET', 'POST'])
def project():
    return render_template('project/projects.html')

@blueprint.route('/get-projects', methods=['GET', 'POST'])
def get_projects():
    data = [r.as_dict() for r in Project.query.all()]
    return jsonify(data=data)

@blueprint.route('/project/<project_id>', methods=['GET', 'POST'])
def project_create(project_id):
    if (project_id == "New"):
        form = ProjectForm(request.form)
        if 'save' in request.form:
            project = Project(**request.form)
            db.session.add(project)
            db.session.commit()
            return redirect(url_for('home_blueprint.project'))
        return render_template('project/create-edit-project.html', form=form)

    project = Project.query.filter_by(project_id=project_id).first()
    form = ProjectForm(obj=project)
    if 'save' in request.form:
        project.project_name = form.project_name.data
        db.session.commit()
        return redirect(url_for('home_blueprint.project'))
    return render_template('project/create-edit-project.html', form=form)

# Shift
@blueprint.route('/shift', methods=['GET', 'POST'])
def shift():
    return render_template('shift/shifts.html')

@blueprint.route('/get-shifts', methods=['GET', 'POST'])
def get_shifts():
    data = [r.as_dict() for r in Shift.query.all()]
    return jsonify(data=data)

@blueprint.route('/shift/<shift_id>', methods=['GET', 'POST'])
def shift_create(shift_id):
    if (shift_id == "New"):
        form = ShiftForm(request.form)
        if 'save' in request.form:
            shift = Shift(**request.form)
            db.session.add(shift)
            db.session.commit()
            return redirect(url_for('home_blueprint.shift'))
        return render_template('shift/create-edit-shift.html', form=form)

    shift = Shift.query.filter_by(shift_id=shift_id).first()
    form = ShiftForm(obj=shift)
    if 'save' in request.form:
        shift.shift_name = form.shift_name.data
        db.session.commit()
        return redirect(url_for('home_blueprint.shift'))
    return render_template('shift/create-edit-shift.html', form=form)

# Shift
@blueprint.route('/employee', methods=['GET', 'POST'])
def employee():
    return render_template('employee/employees.html')

@blueprint.route('/get-employees', methods=['GET', 'POST'])
def get_employees():
    data = []
    for record in db.session.query(User).join(Department, Department.dept_id == User.dept_id).join(Function, Function.func_id == User.func_id).join(Plant, Plant.plant_id == User.plant_id).join(Branch, Branch.branch_id == User.branch_id).join(Project, Project.project_id == User.project_id).join(Shift, Shift.shift_id == User.shift_id).all():
        player_record = {
            'usr_miId' : record.usr_miId,
            'usr_alternateMiId' : record.usr_alternateMiId,
            'usr_name' : record.usr_name,
            'usr_department' : record.usr_department.dept_name,
            'usr_function' : record.usr_function.func_name,
            'usr_type' : record.usr_type.upper(),
            'usr_plant' : record.usr_plant.plant_name,
            'usr_designation' : record.usr_designation.upper(),
            'usr_gender' : record.usr_gender,
            'usr_branch' : record.usr_branch.branch_name,
            'usr_project' : record.usr_project.project_name,
            'usr_contactNumber' : record.usr_contactNumber,
            'usr_emergencyContactNumber' : record.usr_emergencyContactNumber,
            'usr_status' : record.usr_status,
            'usr_shift' : record.usr_shift.shift_name,
            'usr_isProxy' : record.usr_isProxy
        }
        data.append(player_record)
    return jsonify(data=data)

@blueprint.route('/employee/<usr_miId>', methods=['GET', 'POST'])
def employee_create(usr_miId):
    if (usr_miId == "New"):
        form = UserForm(request.form)

        form.usr_miId.render_kw['readonly'] = False

        form.dept_id.choices += [(r.as_dict()["dept_id"], r.as_dict()["dept_name"]) for r in Department.query.all()]
        form.func_id.choices += [(r.as_dict()["func_id"], r.as_dict()["func_name"]) for r in Function.query.all()]
        form.plant_id.choices += [(r.as_dict()["plant_id"], r.as_dict()["plant_name"]) for r in Plant.query.all()]
        form.branch_id.choices += [(r.as_dict()["branch_id"], r.as_dict()["branch_name"]) for r in Branch.query.all()]
        form.project_id.choices += [(r.as_dict()["project_id"], r.as_dict()["project_name"]) for r in Project.query.all()]
        form.shift_id.choices += [(r.as_dict()["shift_id"], r.as_dict()["shift_name"]) for r in Shift.query.all()]

        if 'save' in request.form:
            emp = User(**request.form)

            emp.usr_password = hash_pass("Wistron@123")

            db.session.add(emp)
            db.session.commit()
            return redirect(url_for('home_blueprint.employee'))
        return render_template('employee/create-edit-employee.html', form=form)

    emp = User.query.filter_by(usr_miId=usr_miId).first()
    form = UserForm(obj=emp)

    form.usr_miId.render_kw['readonly'] = True

    form.dept_id.choices += [(r.as_dict()["dept_id"], r.as_dict()["dept_name"]) for r in Department.query.all()]
    form.func_id.choices += [(r.as_dict()["func_id"], r.as_dict()["func_name"]) for r in Function.query.all()]
    form.plant_id.choices += [(r.as_dict()["plant_id"], r.as_dict()["plant_name"]) for r in Plant.query.all()]
    form.branch_id.choices += [(r.as_dict()["branch_id"], r.as_dict()["branch_name"]) for r in Branch.query.all()]
    form.project_id.choices += [(r.as_dict()["project_id"], r.as_dict()["project_name"]) for r in Project.query.all()]
    form.shift_id.choices += [(r.as_dict()["shift_id"], r.as_dict()["shift_name"]) for r in Shift.query.all()]
    if 'save' in request.form:

        emp.usr_alternateMiId = form.usr_alternateMiId.data
        emp.usr_name = form.usr_name.data
        emp.dept_id = form.dept_id.data
        emp.func_id = form.func_id.data
        emp.usr_type = form.usr_type.data
        emp.plant_id = form.plant_id.data
        emp.usr_designation = form.usr_designation.data
        emp.usr_gender = form.usr_gender.data
        emp.branch_id = form.branch_id.data
        emp.usr_experience = form.usr_experience.data
        emp.usr_dob = form.usr_dob.data
        emp.project_id = form.project_id.data
        emp.usr_permanentAddress = form.usr_permanentAddress.data
        emp.usr_currentAddress = form.usr_currentAddress.data
        emp.usr_pickUpRoute = form.usr_pickUpRoute.data
        emp.usr_pickUpPoint = form.usr_pickUpPoint.data
        emp.usr_contactNumber = form.usr_contactNumber.data
        emp.usr_emergencyContactNumber = form.usr_emergencyContactNumber.data
        emp.usr_bloodGroup = form.usr_bloodGroup.data
        emp.usr_doj = form.usr_doj.data
        emp.usr_status = form.usr_status.data
        emp.shift_id = form.shift_id.data
        emp.usr_isProxy = form.usr_isProxy.data

        db.session.commit()
        return redirect(url_for('home_blueprint.employee'))
    return render_template('employee/create-edit-employee.html', form=form)