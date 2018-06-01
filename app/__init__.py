from flask import Flask

from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from config import config

db = SQLAlchemy()
ma = Marshmallow()

from .api.UserResource import UserResource
from .models import User

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config['default'])
    db.init_app(app)
    ma.init_app(app)

    api = Api(app)

    api.add_resource(HelloWorld,'/')
    api.add_resource(UserResource, '/users', '/users/<int:id>')
    #api.add_resource(UserResource, '/users/<int:id>', methods = ['GET','PUT','DELETE'])

    return app