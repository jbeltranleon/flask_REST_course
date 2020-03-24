from db import db


class Payer(db.Model):

    __tablename__ = 'payer'

    id = db.Column(db.Integer, primary_key=True)
    extra_data = db.Column(db.String(80))

    def __init__(self, _id, extra_data):
        self.id = _id
        self.extra_data = extra_data
