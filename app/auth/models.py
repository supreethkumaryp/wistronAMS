# -*- encoding: utf-8 -*-

from flask_login import UserMixin
from sqlalchemy import Column, Binary, Integer, Float, String, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app import db, login_manager
from app.auth.utils import hash_pass

class User(db.Model, UserMixin):

    __tablename__ = 'AMS_Users'

    usr_miId = Column(String(10), primary_key=True, unique=True)
    usr_alternateMiId = Column(String(10))
    usr_name = Column(String(128))
    dept_id = Column(Integer, ForeignKey("AMS_Departments.dept_id"))
    func_id = Column(Integer, ForeignKey("AMS_Functions.func_id"))
    usr_type = Column(String(4))
    plant_id = Column(Integer, ForeignKey("AMS_Plants.plant_id"))
    usr_designation = Column(String(16))
    usr_gender = Column(String(8))
    branch_id = Column(Integer, ForeignKey("AMS_Branches.branch_id"))
    usr_experience = Column(Float)
    usr_dob = Column(Date)
    project_id = Column(Integer, ForeignKey("AMS_Projects.project_id"))
    usr_permanentAddress = Column(String(256))
    usr_currentAddress = Column(String(256))
    usr_pickUpRoute = Column(String(128))
    usr_pickUpPoint = Column(String(128))
    usr_contactNumber = Column(String(16))
    usr_emergencyContactNumber = Column(String(16))
    usr_bloodGroup = Column(String(4))
    usr_doj = Column(Date)
    usr_status = Column(String(16))
    shift_id = Column(Integer, ForeignKey("AMS_Shifts.shift_id"))
    usr_isProxy = Column(Boolean, default=False)
    usr_password = Column(Binary)
    usr_isFirstLogin = Column(Boolean, default=True)
    usr_authorized = Column(Boolean, default=False)
    usr_authorizedFrom = Column(Date, default=None)
    usr_authorizedTill = Column(Date, default=None)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Relationships
    usr_department = relationship("Department")
    usr_function = relationship("Function")
    usr_plant = relationship("Plant")
    usr_branch = relationship("Branch")
    usr_project = relationship("Project")
    usr_shift = relationship("Shift")

    def __init__(self, **kwargs):
        for property, value in kwargs.items():

            if (hasattr(value, '__iter__') and not isinstance(value, str)):
                value = value[0]

            if property == 'password':
                value = hash_pass(value)

            setattr(self, property, value)

    def __repr__(self):
        return "<User {}>".format(self.usr_miId)

    def get_id(self):
        return (self.usr_miId)

@login_manager.user_loader
def user_loader(usr_miId):
    return User.query.filter_by(usr_miId=usr_miId).first()

@login_manager.request_loader
def request_loader(request):
    usr_miId = request.form.get('usr_miId')
    user = User.query.filter_by(usr_miId=usr_miId).first()
    return user if user else None