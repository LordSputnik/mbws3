
from ws import db

class Language(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    iso_code_2t = db.Column(db.Unicode(3))
    iso_code_2b = db.Column(db.Unicode(3))
    iso_code_1 = db.Column(db.Unicode(2))

    name = db.Column(db.Unicode(100), nullable=False)

    frequency = db.Column(db.Integer, default=0, nullable=False)

    iso_code_3 = db.Column(db.Unicode(2))
