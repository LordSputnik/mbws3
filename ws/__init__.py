from flask import Flask
from flask.ext.restless import APIManager

manager = APIManager()

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

    from ws.schema import db
    db.app = app
    db.init_app(app)

    global manager
    manager.init_app(app, flask_sqlalchemy_db=db)

    import ws.schema.artist
    import ws.schema.artist_type
    import ws.schema.gender
    import ws.schema.area
    import ws.schema.area_type

    manager.create_api(ws.schema.artist.Artist, methods=['GET'], primary_key='gid')
    manager.create_api(ws.schema.artist_type.ArtistType, methods=['GET'])
    manager.create_api(ws.schema.gender.Gender, methods=['GET'])
    manager.create_api(ws.schema.area.Area, methods=['GET'])
    manager.create_api(ws.schema.area_type.AreaType, methods=['GET'])

    return app
