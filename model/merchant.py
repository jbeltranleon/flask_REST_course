from db import db


class Merchant(db.Model):

    __tablename__ = 'merchant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # Back Reference
    # Use lazy='dynamic' to avoid to create payers objects for each query to merchant
    # the payers should be called using payers.all() (payers wll be a query builder, not a payers list)
    payers = db.relationship('Payer',   lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def to_json(self):
        return {'merchant_id': self.id, 'name': self.name, 'payers': [payer.to_json() for payer in self.payers]}
