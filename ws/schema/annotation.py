import datetime

from ws import db

class Annotation(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    editor_id = db.Column('editor',db.Integer, db.ForeignKey('editor.id'))
    text = db.Column(db.UnicodeText)
    changelog = db.Column(db.Unicode(255))
    created = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)

    editor = db.relationship('Editor')

    @property
    def begin_date(self):
        pass

    @property
    def end_date(self):
        pass
