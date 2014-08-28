
from ws.schema import db

class Script(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    iso_code = db.Column(db.CHAR(4, convert_unicode=True), nullable=False)
    iso_number = db.Column(db.CHAR(3, convert_unicode=True), nullable=False)

    name = db.Column(db.Unicode(100), nullable=False)
    frequency = db.Column(db.Integer, default=0, nullable=False)
