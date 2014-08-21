
from ws import create_app

config = {
    'SQLALCHEMY_DATABASE_URI':'postgresql://musicbrainz:musicbrainz@localhost/musicbrainz_db'
}

app = create_app(config)

run_config = {
    "debug":True,
    "port":19048,
    "host":"0.0.0.0"
}

if __name__ == '__main__':
    app.run(**run_config)
