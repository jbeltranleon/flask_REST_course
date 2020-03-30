from db import db
from user import User


def find_by_username(username):
    return User.query.filter_by(username=username).first()


def find_by_id(_id):
    return User.query.filter_by(id=_id).first()


def save(user):
    db.session.delete(user)
    db.session.commit()
