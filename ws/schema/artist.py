import datetime

from sqlalchemy.dialects.postgresql import UUID

from ws import db

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

    type_id = db.Column('type', db.Integer, db.ForeignKey('artist_type.id'))
    area_id = db.Column('area', db.Integer, db.ForeignKey('area.id'))
    gender_id = db.Column('gender',db.Integer, db.ForeignKey('gender.id'))
    comment = db.Column(db.Unicode(255), default=u'', nullable=False)

    edits_pending = db.Column(db.Integer, default=0, nullable=False)
    last_updated = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)

    ended = db.Column(db.Boolean, default=False, nullable=False)

    begin_area_id = db.Column('begin_area',db.Integer, db.ForeignKey('area.id'))
    end_area_id = db.Column('end_area',db.Integer, db.ForeignKey('area.id'))

    type = db.relationship('ArtistType')
    gender = db.relationship('Gender')
    area = db.relationship('Area', foreign_keys=area_id)
    begin_area = db.relationship('Area', foreign_keys=begin_area_id)
    end_area = db.relationship('Area', foreign_keys=end_area_id)

    @property
    def begin_date(self):
        pass

    @property
    def end_date(self):
        pass
