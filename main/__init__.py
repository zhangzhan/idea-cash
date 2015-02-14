#-*- coding: utf-8 -*-
__author__ = 'andy'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from utils.log import config_log
import settings

db = SQLAlchemy()

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('main.settings')

db.init_app(app)

logger = config_log(app.config.get("LOGGER_NAME"), app.config.get("LOGGER_LEVEL", "DEBUG"), app.config.get("LOGGER_PATH", None))