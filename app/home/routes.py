# -*- encoding: utf-8 -*-

from flask import jsonify, render_template, redirect, request, url_for, flash
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)
from datetime import date, datetime
import csv

from app import db, login_manager
from app.home import blueprint
from app.home.models import Department, Function, Plant, Branch, Project, Shift, Roster
from app.home.forms import DepartmentForm, FunctionForm, PlantForm, BranchForm, ProjectForm, ShiftForm, UserForm, RosterDateForm, ImportForm

from app.auth.models import User
from app.auth.utils import hash_pass

from jinja2 import TemplateNotFound

# Context
@blueprint.context_processor
def inject_today_date():
    return {'today_date': date.today()}

# Department
@blueprint.route('/department', methods=['GET', 'POST'])
@login_required
def department():
    return render_template('department/departments.html')

@blueprint.route('/get-departments', methods=['GET', 'POST'])
@login_required
def get_departments():
    data = [r.as_dict() for r in Department.query.all()]
    return jsonify(data=data)

@blueprint.route('/department/<dept_id>', methods=['GET', 'POST'])
@login_required
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
@login_required
def function():
    return render_template('function/functions.html')

@blueprint.route('/get-functions', methods=['GET', 'POST'])
@login_required
def get_functions():
    data = [r.as_dict() for r in Function.query.all()]
    return jsonify(data=data)

@blueprint.route('/function/<func_id>', methods=['GET', 'POST'])
@login_required
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
@login_required
def plant():
    return render_template('plant/plants.html')

@blueprint.route('/get-plants', methods=['GET', 'POST'])
@login_required
def get_plants():
    data = [r.as_dict() for r in Plant.query.all()]
    return jsonify(data=data)

@blueprint.route('/plant/<plant_id>', methods=['GET', 'POST'])
@login_required
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
@login_required
def branch():
    return render_template('branch/branches.html')

@blueprint.route('/get-branches', methods=['GET', 'POST'])
@login_required
def get_branches():
    data = [r.as_dict() for r in Branch.query.all()]
    return jsonify(data=data)

@blueprint.route('/branch/<branch_id>', methods=['GET', 'POST'])
@login_required
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
@login_required
def project():
    return render_template('project/projects.html')

@blueprint.route('/get-projects', methods=['GET', 'POST'])
@login_required
def get_projects():
    data = [r.as_dict() for r in Project.query.all()]
    return jsonify(data=data)

@blueprint.route('/project/<project_id>', methods=['GET', 'POST'])
@login_required
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
@login_required
def shift():
    return render_template('shift/shifts.html')

@blueprint.route('/get-shifts', methods=['GET', 'POST'])
@login_required
def get_shifts():
    data = [r.as_dict() for r in Shift.query.all()]
    return jsonify(data=data)

@blueprint.route('/shift/<shift_id>', methods=['GET', 'POST'])
@login_required
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
@login_required
def employee():
    return render_template('employee/employees.html')

@blueprint.route('/get-employees', methods=['GET', 'POST'])
@login_required
def get_employees():
    data = []

    if (current_user.usr_designation == "em"):
        records = db.session.query(User).join(Department, Department.dept_id == User.dept_id).join(Function, Function.func_id == User.func_id).join(Plant, Plant.plant_id == User.plant_id).join(Branch, Branch.branch_id == User.branch_id).join(Project, Project.project_id == User.project_id).join(Shift, Shift.shift_id == User.shift_id).all()
    else:
        records = db.session.query(User).filter(User.usr_department == current_user.usr_department).join(Department, Department.dept_id == User.dept_id).join(Function, Function.func_id == User.func_id).join(Plant, Plant.plant_id == User.plant_id).join(Branch, Branch.branch_id == User.branch_id).join(Project, Project.project_id == User.project_id).join(Shift, Shift.shift_id == User.shift_id).all()

    for record in records:
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
@login_required
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

# Roster
@blueprint.route('/roster/<rst_date>', methods=['GET', 'POST'])
@login_required
def roster(rst_date):
    form = RosterDateForm(request.form)
    form.rst_date.data = datetime.strptime(rst_date, r"%Y-%m-%d")

    data = []
    
    for record in User.query.filter_by(usr_department=current_user.usr_department, usr_shift=current_user.usr_shift).all():

        if record.usr_status == "resigned":
            continue

        rst = Roster.query.filter_by(rst_date=datetime.strptime(rst_date, r"%Y-%m-%d"), usr_miId=record.usr_miId).first()
        data.append({
            'usr_miId' : record.usr_miId,
            'usr_name' : record.usr_name,
            'usr_value' : rst.rst_status if rst else ""
        })

    if 'save' in request.form:
        for key in request.form:

            if not key.startswith("usr_status_"):
                continue

            rst = Roster.query.filter_by(usr_miId=key.split("_")[-1], rst_date = datetime.strptime(rst_date, r"%Y-%m-%d")).first()

            if rst:
                rst.rst_status = request.form[key]
            else:
                rst = Roster(
                    usr_miId = key.split("_")[-1],
                    rst_date = datetime.strptime(rst_date, r"%Y-%m-%d"),
                    rst_status = request.form[key]
                )

                db.session.add(rst)
            db.session.commit()

        return redirect('/roster/{}'.format(rst_date))

    return render_template('roster/rosters.html', data=data, form=form)

# Import / Export
@blueprint.route('/import-employees', methods=['GET', 'POST'])
@login_required
def import_users():
    form = ImportForm(request.form)

    if 'importcsv' in request.form:
        uploaded_file = request.files['csv_file']

        if uploaded_file.filename != '':

            if not uploaded_file.filename.split(".")[-1].lower() == "csv":
                return render_template('import-employees.html', msg="Only CSV File is allowed", form=form)

            uploaded_file.save("import.csv")

            with open('import.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        employee = User(
                            usr_miId = str(row[0]),
                            usr_alternateMiId = str(row[1]),
                            usr_name = str(row[2]),
                            dept_id = Department.query.filter_by(dept_name=str(row[3])).first().dept_id,
                            func_id = Function.query.filter_by(func_name=str(row[4])).first().func_id,
                            usr_type = str(row[5]),
                            plant_id = Plant.query.filter_by(plant_name=str(row[6])).first().plant_id,
                            usr_designation = str(row[7]),
                            usr_gender = str(row[8]),
                            branch_id = Branch.query.filter_by(branch_name=str(row[9])).first().branch_id,
                            usr_experience = float(row[10]),
                            usr_dob = datetime.strptime(str(row[11]), r"%d-%m-%Y"),
                            project_id = Project.query.filter_by(project_name=str(row[12])).first().project_id,
                            usr_permanentAddress = str(row[13]),
                            usr_currentAddress = str(row[14]),
                            usr_pickUpRoute = str(row[15]),
                            usr_pickUpPoint = str(row[16]),
                            usr_contactNumber = str(row[17]),
                            usr_emergencyContactNumber = str(row[18]),
                            usr_bloodGroup = str(row[19]),
                            usr_doj = datetime.strptime(str(row[20]), r"%d-%m-%Y"),
                            usr_status = str(row[21]),
                            shift_id = Shift.query.filter_by(shift_name=str(row[22])).first().shift_id,
                            usr_isProxy = 1 if str(row[23]) == "Yes" else 0,
                            usr_isFirstLogin = 1
                        )

                        employee.usr_password = hash_pass("Wistron@123")

                        db.session.add(employee)
                        db.session.commit()

                        line_count += 1
        
            return redirect(url_for('home_blueprint.employee'))

    return render_template('import-employees.html', form=form)

# Dashboard
@blueprint.route('/dashboard/<reoprt_date>', methods=['GET', 'POST'])
@login_required
def dashboard(reoprt_date):

    form = RosterDateForm(request.form)
    form.rst_date.data = datetime.strptime(reoprt_date, r"%Y-%m-%d")

    data = {}
    data1 = {}

    depts = Department.query.all()
    shifts = Shift.query.all()

    for dept in depts:
        data[dept.dept_name] = {}
        for shift in shifts:
            data[dept.dept_name][shift.shift_name] = {}

            data[dept.dept_name][shift.shift_name]['total'] = db.session.query(User).filter(User.dept_id==dept.dept_id, User.shift_id == shift.shift_id, User.usr_status != "resigned").count()

            data[dept.dept_name][shift.shift_name]['total_dl'] = db.session.query(User).filter(User.dept_id==dept.dept_id, User.shift_id==shift.shift_id, User.usr_type=="dl", User.usr_status != "resigned").count()

            data[dept.dept_name][shift.shift_name]['total_idl'] = db.session.query(User).filter(User.dept_id==dept.dept_id, User.shift_id==shift.shift_id, User.usr_type=="idl", User.usr_status != "resigned").count()

            data[dept.dept_name][shift.shift_name]['present'] = 0
            data[dept.dept_name][shift.shift_name]['present_dl'] = 0
            data[dept.dept_name][shift.shift_name]['present_idl'] = 0

            data[dept.dept_name][shift.shift_name]['absent'] = 0
            data[dept.dept_name][shift.shift_name]['absent_dl'] = 0
            data[dept.dept_name][shift.shift_name]['absent_idl'] = 0

    records = db.session.query(Roster).filter(Roster.rst_date == datetime.strptime(reoprt_date, r"%Y-%m-%d")).join(User, User.usr_miId == Roster.usr_miId).all()
    for record in records:
        if (record.rst_status == "present"):
            data[record.rst_user.usr_department.dept_name][record.rst_user.usr_shift.shift_name]['present'] += 1
            data[record.rst_user.usr_department.dept_name][record.rst_user.usr_shift.shift_name]['present_'+record.rst_user.usr_type] += 1
        else:
            data[record.rst_user.usr_department.dept_name][record.rst_user.usr_shift.shift_name]['absent'] += 1
            data[record.rst_user.usr_department.dept_name][record.rst_user.usr_shift.shift_name]['absent_'+record.rst_user.usr_type] += 1


    for dept in depts:
        for shift in shifts:
            data[dept.dept_name][shift.shift_name]['percentage_present'] = round((data[dept.dept_name][shift.shift_name]['present'] / data[dept.dept_name][shift.shift_name]['total'] * 100) if data[dept.dept_name][shift.shift_name]['total'] else 0)
            data[dept.dept_name][shift.shift_name]['percentage_present_dl'] = round((data[dept.dept_name][shift.shift_name]['present_dl'] / data[dept.dept_name][shift.shift_name]['total_dl'] * 100) if data[dept.dept_name][shift.shift_name]['total_dl'] else 0)
            data[dept.dept_name][shift.shift_name]['percentage_present_idl'] = round((data[dept.dept_name][shift.shift_name]['present_idl'] / data[dept.dept_name][shift.shift_name]['total_idl'] * 100) if data[dept.dept_name][shift.shift_name]['total_idl'] else 0)

            data[dept.dept_name][shift.shift_name]['percentage_absent'] = round((data[dept.dept_name][shift.shift_name]['absent'] / data[dept.dept_name][shift.shift_name]['total'] * 100) if data[dept.dept_name][shift.shift_name]['total'] else 0)
            data[dept.dept_name][shift.shift_name]['percentage_absent_dl'] = round((data[dept.dept_name][shift.shift_name]['absent_dl'] / data[dept.dept_name][shift.shift_name]['total_dl'] * 100) if data[dept.dept_name][shift.shift_name]['total_dl'] else 0)
            data[dept.dept_name][shift.shift_name]['percentage_absent_idl'] = round((data[dept.dept_name][shift.shift_name]['absent_idl'] / data[dept.dept_name][shift.shift_name]['total_idl'] * 100) if data[dept.dept_name][shift.shift_name]['total_idl'] else 0)

    data1['total'] = 0
    data1['total_dl'] = 0
    data1['total_idl'] = 0
    data1['present'] = 0
    data1['present_dl'] = 0
    data1['present_idl'] = 0
    data1['absent'] = 0
    data1['absent_dl'] = 0
    data1['absent_idl'] = 0

    for dept in depts:
        for shift in shifts:
            data1['total'] += data[dept.dept_name][shift.shift_name]['total']
            data1['total_dl'] += data[dept.dept_name][shift.shift_name]['total_dl']
            data1['total_idl'] += data[dept.dept_name][shift.shift_name]['total_idl']
            data1['present'] += data[dept.dept_name][shift.shift_name]['present']
            data1['present_dl'] += data[dept.dept_name][shift.shift_name]['present_dl']
            data1['present_idl'] += data[dept.dept_name][shift.shift_name]['present_idl']
            data1['absent'] += data[dept.dept_name][shift.shift_name]['absent']
            data1['absent_dl'] += data[dept.dept_name][shift.shift_name]['absent_dl']
            data1['absent_idl'] += data[dept.dept_name][shift.shift_name]['absent_idl']

    data1['percentage_present'] = round((data1['present'] / data1['total'] * 100) if data1['total'] else 0)
    data1['percentage_present_dl'] = round((data1['present_dl'] / data1['total_dl'] * 100) if data1['total_dl'] else 0)
    data1['percentage_present_idl'] = round((data1['present_idl'] / data1['total_idl'] * 100) if data1['total_idl'] else 0)
    
    data1['percentage_absent'] = round((data1['absent'] / data1['total'] * 100) if data1['total'] else 0)
    data1['percentage_absent_dl'] = round((data1['absent_dl'] / data1['total_dl'] * 100) if data1['total_dl'] else 0)
    data1['percentage_absent_idl'] = round((data1['absent_idl'] / data1['total_idl'] * 100) if data1['total_idl'] else 0)

    return render_template('dashboard.html', data=data, data1=data1, form=form)