import imp
from flask import Flask
import os
from flask import Flask
from flask.json import JSONEncoder
from bson import json_util, ObjectId
from datetime import datetime

from BackendRestaurants.api import api_v1

class MongoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)

def create_app():
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    #STATIC_FOLDER = os.path.join(APP_DIR, 'build/static')
    #TEMPLATE_FOLDER = os.path.join(APP_DIR, 'build')

    app = Flask(__name__)
    app.json_encoder = MongoJsonEncoder
    
    # API
    app.register_blueprint(api_v1)

    @app.route('/')
    def serve():
       return "<p>Welcome to Backend Restaurants Service!</p>"

    return app