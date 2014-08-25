import datetime

from ws.schema import db

class ArtistCredit(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.UnicodeText, nullable=False)

    artist_count = db.Column(db.SmallInteger, nullable=False)

    ref_count = db.Column(db.Integer, default=0)

    created = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
