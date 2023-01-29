import logging
import os
import sys

#from celery import Celery
from flask import Flask
from celery import Celery


#initializing celery
# celery = Celery(__name__, include=["apps.mqtt_module.task"])

def create_app(config_type=None):
    
    # Create flask app object
    app = Flask(__name__)

    # Setting configuration for the project 
    app.config.from_object(config_type)

    # Adding log level
    app.logger.addHandler(logging.StreamHandler(stream=sys.stdout))
    app.logger.setLevel(logging.DEBUG)

    #Register blueprint
    from apps.test_module.controller import test_blueprint
    app.register_blueprint(test_blueprint)

    return app

