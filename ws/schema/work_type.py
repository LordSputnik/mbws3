from ws import db

class WorkType(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(255), nullable=False)

    parent = db.Column(db.Integer, db.ForeignKey('work_type.id'))

    child_order = db.Column(db.Integer, default=0, nullable=False)

    description = db.Column(db.UnicodeText)

    children = db.relationship('WorkType')
