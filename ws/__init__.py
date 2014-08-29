from flask import Flask
from flask.ext.restless import APIManager

manager = APIManager()

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

import ws.schema

def add_cors_header(response):
    # https://github.com/jfinkels/flask-restless/issues/223
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'HEAD, GET, POST, PATCH, PUT, OPTIONS, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
    response.headers['Access-Control-Allow-Credentials'] = 'true'

    return response


def create_app(config):
    app = Flask(__name__)

    app.config.update(config)
    app.after_request(add_cors_header)

    global db
    db.app = app
    db.init_app(app)

    global manager
    manager.init_app(app, flask_sqlalchemy_db=db)

    manager.create_api(ws.schema.Annotation, methods=['GET'])
    manager.create_api(ws.schema.Application, methods=['GET'])

    manager.create_api(ws.schema.Area, methods=['GET'], primary_key='gid')
    manager.create_api(ws.schema.AreaType, methods=['GET'])

    manager.create_api(ws.schema.Artist, methods=['GET'], primary_key='gid')
    manager.create_api(ws.schema.ArtistType, methods=['GET'])
    manager.create_api(ws.schema.ArtistCredit, methods=['GET'])


    manager.create_api(ws.schema.Edit, methods=['GET'])
    manager.create_api(ws.schema.Editor, methods=['GET'])

    manager.create_api(ws.schema.Gender, methods=['GET'])

    manager.create_api(ws.schema.Language, methods=['GET'])

    manager.create_api(ws.schema.Recording, methods=['GET'])

    manager.create_api(ws.schema.Release, methods=['GET'], primary_key='gid', include_methods=['url'])
    manager.create_api(ws.schema.ReleasePackaging, methods=['GET'])
    manager.create_api(ws.schema.ReleaseStatus, methods=['GET'])

    manager.create_api(ws.schema.ReleaseGroup, methods=['GET'], primary_key='gid')
    manager.create_api(ws.schema.ReleaseGroupPrimaryType, methods=['GET'], primary_key='gid')

    manager.create_api(ws.schema.Script, methods=['GET'])

    manager.create_api(ws.schema.Work, methods=['GET'])
    manager.create_api(ws.schema.WorkType, methods=['GET'])

    return app
