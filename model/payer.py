from db import db


class Payer(db.Model):

    __tablename__ = 'payer'

    id = db.Column(db.Integer, primary_key=True)
    extra_data = db.Column(db.String(80))
    # foreign key
    merchant_id = db.Column(db.String(80), db.ForeignKey('merchant.id'))
    merchant = db.relationship('Merchant')

    def __init__(self, _id, extra_data, merchant_id):
        self.id = _id
        self.extra_data = extra_data
        self.merchant_id = merchant_id

    def to_json(self):
        return {'payer_id': self.id, 'extra_data': self.extra_data}
