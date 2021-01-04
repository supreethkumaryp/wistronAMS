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
from app.home.forms import DepartmentForm, FunctionForm, PlantForm, BranchForm, ProjectForm, ShiftForm

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