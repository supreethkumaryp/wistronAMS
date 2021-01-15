# -*- encoding: utf-8 -*-

from sys import exit

from config import config_dict
from app import create_app

from pyfladesk import init_gui

app_config = config_dict['Production']

app = create_app(app_config)

init_gui(app, port=5000, width=1280, height=800, window_title="Wistron AMS", icon="app/base/static/app-assets/images/logo/android-chrome-512x512.png")