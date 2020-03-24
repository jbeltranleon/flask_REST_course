from db import db
from merchant import Merchant


def find_by_name(name):
    return Merchant.query.filter_by(name=name).first()


def find_all():
    return Merchant.query.all()


def find_all_json():
    return [merchant.to_json() for merchant in find_all()]


def save(merchant):
    db.session.add(merchant)
    db.session.commit()


def delete(merchant):
    db.session.add(merchant)
    db.session.commit()
