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
    import ws.schema.release
    import ws.schema.release_packaging
    import ws.schema.release_status
    import ws.schema.language
    import ws.schema.release_group
    import ws.schema.release_group_primary_type
    import ws.schema.script

    import ws.schema.artist_credit

    manager.create_api(ws.schema.artist.Artist, methods=['GET'], primary_key='gid')
    manager.create_api(ws.schema.artist_type.ArtistType, methods=['GET'])
    manager.create_api(ws.schema.gender.Gender, methods=['GET'])
    manager.create_api(ws.schema.area.Area, methods=['GET'], primary_key='gid')
    manager.create_api(ws.schema.area_type.AreaType, methods=['GET'])
    manager.create_api(ws.schema.release.Release, methods=['GET'], primary_key='gid', include_methods=['url'])
    manager.create_api(ws.schema.release_packaging.ReleasePackaging, methods=['GET'])
    manager.create_api(ws.schema.release_status.ReleaseStatus, methods=['GET'])
    manager.create_api(ws.schema.language.Language, methods=['GET'])
    manager.create_api(ws.schema.release_group.ReleaseGroup, methods=['GET'], primary_key='gid')
    manager.create_api(ws.schema.release_group_primary_type.ReleaseGroupPrimaryType, methods=['GET'], primary_key='gid')
    manager.create_api(ws.schema.script.Script, methods=['GET'])

    manager.create_api(ws.schema.artist_credit.ArtistCredit, methods=['GET'])

    return app
