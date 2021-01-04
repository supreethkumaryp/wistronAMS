# -*- encoding: utf-8 -*-

import os

class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    SECRET_KEY = 'ZjNiZmZiM2QxNjE0Y2U4NTc3NzI5NTJmMDczMzczNWVlMWEx'

    # SQLALCHEMY Settings
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        'mysql',            # DB_ENGINE
        'root',             # DB_USERNAME
        '',                 # DB_PASS
        'localhost',        # DB_HOST
        3306,               # DB_PORT
        'wistronAMS',       # DB_NAME
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600
    
class ProductionConfig(Config):
    DEBUG = False

class DebugConfig(Config):
    DEBUG = True

# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}