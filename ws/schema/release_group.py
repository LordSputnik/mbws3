import datetime

from sqlalchemy.dialects.postgresql import UUID

from ws.schema import db

class ReleaseGroup(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(UUID, unique=True, nullable=False)
    name = db.Column(db.UnicodeText, nullable=False)

    artist_credit_id = db.Column('artist_credit', db.Integer, db.ForeignKey('artist_credit.id'), nullable=False)
    type_id = db.Column('type', db.Integer, db.ForeignKey('release_group_primary_type.id'))

    comment = db.Column(db.Unicode(255), default=u'', nullable=False)

    edits_pending = db.Column(db.Integer, default=0, nullable=False)

    last_updated = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)

    type = db.relationship('ReleaseGroupPrimaryType')
