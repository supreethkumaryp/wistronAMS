# -*- encoding: utf-8 -*-

from flask_login import UserMixin
from sqlalchemy import Column, Binary, Integer, String, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app import db

class Department(db.Model):

    __tablename__ = 'AMS_Departments'

    dept_id = Column(Integer, primary_key=True, autoincrement="auto")
    dept_name = Column(String(128))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __init__(self, **kwargs):
        for property, value in kwargs.items():

            if (hasattr(value, '__iter__') and not isinstance(value, str)):
                value = value[0]

            setattr(self, property, value)

    def __repr__(self):
        return "<Department {}>".format(self.dept_id)

    def as_dict(self):
        data = {}
        for property, value in vars(self).items():

            if (hasattr(value, '__iter__') and not isinstance(value, str)):
                value = value[0]

            if property == "_sa_instance_state":
                continue

            data[property] = value

        return data

class Function(db.Model):

    __tablename__ = 'AMS_Functions'

    func_id = Column(Integer, primary_key=True, autoincrement="auto")
    func_name = Column(String(128))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __init__(self, **kwargs):
        for property, value in kwargs.items():

            if (hasattr(value, '__iter__') and not isinstance(value, str)):
                value = value[0]

            setattr(self, property, value)

    def __repr__(self):
        return "<Function {}>".format(self.dept_id)

    def as_dict(self):
        data = {}
        for property, value in vars(self).items():

            if (hasattr(value, '__iter__') and not isinstance(value, str)):
                value = value[0]

            if property == "_sa_instance_state":
                continue

            data[property] = value

        return data

class Plant(db.Model):

    __tablename__ = 'AMS_Plants'

    plant_id = Column(Integer, primary_key=True, autoincrement="auto")
    plant_name = Column(String(128))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __init__(self, **kwargs):
        for property, value in kwargs.items():

            if (hasattr(value, '__iter__') and not isinstance(value, str)):
                value = value[0]

            setattr(self, property, value)

    def __repr__(self):
        return "<Plant {}>".format(self.dept_id)

    def as_dict(self):
        data = {}
        for property, value in vars(self).items():

            if (hasattr(value, '__iter__') and not isinstance(value, str)):
                value = value[0]

            if property == "_sa_instance_state":
                continue

            data[property] = value

        return data

class Branch(db.Model):

    __tablename__ = 'AMS_Branches'

    branch_id = Column(Integer, primary_key=True, autoincrement="auto")
    branch_name = Column(String(128))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __init__(self, **kwargs):
        for property, value in kwargs.items():

            if (hasattr(value, '__iter__') and not isinstance(value, str)):
                value = value[0]

            setattr(self, property, value)

    def __repr__(self):
        return "<Branch {}>".format(self.dept_id)

    def as_dict(self):
        data = {}
        for property, value in vars(self).items():

            if (hasattr(value, '__iter__') and not isinstance(value, str)):
                value = value[0]

            if property == "_sa_instance_state":
                continue

            data[property] = value

        return data

class Project(db.Model):

    __tablename__ = 'AMS_Projects'

    project_id = Column(Integer, primary_key=True, autoincrement="auto")
    project_name = Column(String(128))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __init__(self, **kwargs):
        for property, value in kwargs.items():

            if (hasattr(value, '__iter__') and not isinstance(value, str)):
                value = value[0]

            setattr(self, property, value)

    def __repr__(self):
        return "<Project {}>".format(self.dept_id)

    def as_dict(self):
        data = {}
        for property, value in vars(self).items():

            if (hasattr(value, '__iter__') and not isinstance(value, str)):
                value = value[0]

            if property == "_sa_instance_state":
                continue

            data[property] = value

        return data

class Shift(db.Model):

    __tablename__ = 'AMS_Shifts'

    shift_id = Column(Integer, primary_key=True, autoincrement="auto")
    shift_name = Column(String(128))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __init__(self, **kwargs):
        for property, value in kwargs.items():

            if (hasattr(value, '__iter__') and not isinstance(value, str)):
                value = value[0]

            setattr(self, property, value)

    def __repr__(self):
        return "<Shift {}>".format(self.dept_id)

    def as_dict(self):
        data = {}
        for property, value in vars(self).items():

            if (hasattr(value, '__iter__') and not isinstance(value, str)):
                value = value[0]

            if property == "_sa_instance_state":
                continue

            data[property] = value

        return data

class Roster(db.Model):

    __tablename__ = 'AMS_Rosters'

    rst_id = Column(Integer, primary_key=True, autoincrement="auto")
    usr_miId = Column(String(10), ForeignKey("AMS_Users.usr_miId"))
    rst_date = Column(Date)
    rst_status = Column(String(16))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Relationships
    rst_user = relationship("User")

    def __init__(self, **kwargs):
        for property, value in kwargs.items():

            if (hasattr(value, '__iter__') and not isinstance(value, str)):
                value = value[0]

            setattr(self, property, value)

    def __repr__(self):
        return "<Roster {}>".format(self.dept_id)