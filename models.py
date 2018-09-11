from datetime import datetime
from app import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(64), index=True)
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    comment = db.Column(db.String(128))

    def __repr__(self):
        return '<Comment {}>'.format(self.ip)
