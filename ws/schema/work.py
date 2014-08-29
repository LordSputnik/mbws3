import datetime

from sqlalchemy.dialects.postgresql import UUID

from ws import db

class Work(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(UUID, unique=True, nullable=False)
    name = db.Column(db.UnicodeText, nullable=False)

    type_id = db.Column('type', db.Integer, db.ForeignKey('work_type.id'))

    comment = db.Column(db.Unicode(255), default=u'', nullable=False)
    edits_pending = db.Column(db.Integer, default=0, nullable=False)
    last_updated = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)

    language_id = db.Column('language', db.Integer, db.ForeignKey('language.id'))

    language = db.relationship('Language')
    type = db.relationship('WorkType')

