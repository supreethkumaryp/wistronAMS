# -*- encoding: utf-8 -*-

from config import config_dict
from app import create_app

app_config = config_dict['Debug']

app = create_app(app_config)

app.run()