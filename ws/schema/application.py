from ws import db

class Application(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    owner_id = db.Column('owner', db.Integer, db.ForeignKey('editor.id'), nullable=False)

    name = db.Column(db.UnicodeText, nullable=False)
    oauth_id = db.Column(db.UnicodeText, nullable=False)
    oauth_secret = db.Column(db.UnicodeText, nullable=False)
    oauth_redirect_url = db.Column(db.UnicodeText, nullable=False)

    owner = db.relationship('Editor')
