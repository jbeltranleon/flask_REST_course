from db import db
from payer import Payer


def find_by_id(_id):
    return Payer.query.filter_by(id=_id).first()


def find_all():
    return Payer.query.all()


def find_all_json():
    return [payer.to_json() for payer in find_all()]


def save(payer):
    db.session.add(payer)
    db.session.commit()


# is not necessary if we find the user and then use the save function
"""def update(payer):
    db.session.merge(payer)
    db.session.commit()"""


def delete(payer):
    db.session.add(payer)
    db.session.commit()
