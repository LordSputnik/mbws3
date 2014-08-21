import datetime

from sqlalchemy.dialects.postgresql import UUID

from ws.schema import db

class Area(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(UUID, unique=True, nullable=False)
    name = db.Column(db.UnicodeText, nullable=False)

    type_id = db.Column('type', db.Integer, db.ForeignKey('area_type.id'))

    edits_pending = db.Column(db.Integer, default=0, nullable=False)
    last_updated = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)

    begin_date_year = db.Column(db.SmallInteger)
    begin_date_month = db.Column(db.SmallInteger)
    begin_date_day = db.Column(db.SmallInteger)

    end_date_year = db.Column(db.SmallInteger)
    end_date_month = db.Column(db.SmallInteger)
    end_date_day = db.Column(db.SmallInteger)

    ended = db.Column(db.Boolean, default=False, nullable=False)
    comment = db.Column(db.Unicode(255), default=u'', nullable=False)

    type = db.relationship('AreaType')

    @property
    def begin_date(self):
        pass

    @property
    def end_date(self):
        pass
