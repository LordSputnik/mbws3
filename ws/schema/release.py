import datetime

from sqlalchemy.dialects.postgresql import UUID

from ws.schema import db

class Release(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(UUID, unique=True, nullable=False)
    name = db.Column(db.UnicodeText, nullable=False)

    artist_credit_id = db.Column('artist_credit', db.Integer, db.ForeignKey('artist_credit.id'), nullable=False)
    release_group_id = db.Column('release_group', db.Integer, db.ForeignKey('release_group.id'), nullable=False)
    status_id = db.Column('status', db.Integer, db.ForeignKey('release_status.id'))
    packaging_id = db.Column('packaging', db.Integer, db.ForeignKey('release_packaging.id'))
    language_id = db.Column('language', db.Integer, db.ForeignKey('language.id'))
    script_id = db.Column('script', db.Integer)

    barcode = db.Column(db.Unicode(255))
    comment = db.Column(db.Unicode(255), default=u'', nullable=False)

    edits_pending = db.Column(db.Integer, default=0, nullable=False)
    quality = db.Column(db.SmallInteger, default=-1, nullable=False)

    last_updated = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)

    packaging = db.relationship('ReleasePackaging')
    status = db.relationship('ReleaseStatus')
    language = db.relationship('Language')
    artist_credit = db.relationship('ArtistCredit')
    release_group = db.relationship('ReleaseGroup')

    @property
    def begin_date(self):
        pass

    @property
    def end_date(self):
        pass

    def url(self):
        return '/api/release/'+self.gid
