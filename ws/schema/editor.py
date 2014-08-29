import datetime

from ws import db
from sqlalchemy.sql import func, text

class Editor(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Unicode(64), nullable=False)
    privs = db.Column(db.Integer, server_default=text('0'))
    email = db.Column(db.Unicode(64), server_default=text('NULL'))
    website = db.Column(db.Unicode(255), server_default=text('NULL'))
    bio = db.Column(db.UnicodeText)

    member_since = db.Column(db.DateTime(timezone=True), server_default=func.now())
    email_confirm_date = db.Column(db.DateTime(timezone=True))
    last_login_date = db.Column(db.DateTime(timezone=True), server_default=func.now())

    edits_accepted = db.Column(db.Integer, server_default=text('0'))
    edits_rejected = db.Column(db.Integer, server_default=text('0'))
    auto_edits_accepted = db.Column(db.Integer, server_default=text('0'))
    edits_failed = db.Column(db.Integer, server_default=text('0'))

    last_updated = db.Column(db.DateTime(timezone=True), server_default=func.now())
    birth_date = db.Column(db.Date)
    gender_id = db.Column('gender',db.Integer, db.ForeignKey('gender.id'))
    area_id = db.Column('area', db.Integer, db.ForeignKey('area.id'))

    password = db.Column(db.Unicode(128), nullable=False)
    ha1 = db.Column(db.CHAR(32), nullable=False)

    deleted = db.Column(db.Boolean, server_default=text('FALSE'), nullable=False)


