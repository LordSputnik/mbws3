import datetime

from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
db = SQLAlchemy(app)

class Artist(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(UUID, unique=True, nullable=False)
    name = db.Column(db.UnicodeText, nullable=False)
    sort_name = db.Column(db.UnicodeText, nullable=False)

    begin_date_year = db.Column(db.SmallInteger)
    begin_date_month = db.Column(db.SmallInteger)
    begin_date_day = db.Column(db.SmallInteger)

    end_date_year = db.Column(db.SmallInteger)
    end_date_month = db.Column(db.SmallInteger)
    end_date_day = db.Column(db.SmallInteger)

    type = db.Column(db.Integer, db.ForeignKey('artist_type.id'))
    area = db.Column(db.Integer, db.ForeignKey('area.id'))
    gender = db.Column(db.Integer, db.ForeignKey('gender.id'))
    comment = db.Column(db.Unicode(255), default=u'', nullable=False)

    edits_pending = db.Column(db.Integer, default=0, nullable=False)
    last_updated = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)

    ended = db.Column(db.Boolean, default=False, nullable=False)

    begin_area = db.Column(db.Integer, db.ForeignKey('area.id'))
    end_area = db.Column(db.Integer, db.ForeignKey('area.id'))


    @property
    def begin_date(self):
        pass

    @property
    def end_date(self):
        pass
