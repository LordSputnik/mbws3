import datetime

from sqlalchemy.dialects.postgresql import UUID

from ws import db

class Recording(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(UUID, unique=True, nullable=False)
    name = db.Column(db.UnicodeText, nullable=False)

    artist_credit_id = db.Column('artist_credit', db.Integer, db.ForeignKey('artist_credit.id'), nullable=False)

    length = db.Column(db.Integer)

    comment = db.Column(db.Unicode(255), default=u'', nullable=False)
    edits_pending = db.Column(db.Integer, default=0, nullable=False)

    last_updated = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)

    video = db.Column(db.Boolean, default=False)

    artist_credit = db.relationship('ArtistCredit')
