import datetime

from ws import db

class Edit(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    editor_id = db.Column('editor', db.Integer, db.ForeignKey('editor.id'), nullable=False)

    type = db.Column(db.SmallInteger, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)
    data = db.Column(db.UnicodeText, nullable=False)
    yes_votes = db.Column(db.Integer, default=0, nullable=False)
    no_votes = db.Column(db.Integer, default=0, nullable=False)
    autoedit = db.Column(db.SmallInteger, default=0, nullable=False)
    open_time = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    close_time = db.Column(db.DateTime(timezone=True))
    expire_time = db.Column(db.DateTime(timezone=True), nullable=False)
    language_id = db.Column('language', db.Integer, db.ForeignKey('language.id'))
    quality = db.Column(db.SmallInteger, default=1, nullable=False)

    editor = db.relationship('Editor')
    language = db.relationship('Language')
