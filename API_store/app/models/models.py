from db import db


class User(db.Model):
    __tablename__ = 'users'

    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    store = db.relationship('Store', backref = 'user')


class Good(db.Model):
    __tablename__ = 'goods'

    id_goods = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    name = db.Column(db.String)
    price = db.Column(db.Float)


class Store(db.Model):
    __tablename__ = 'stores'

    id_stroes = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    city = db.Column(db.String)
    address = db.Column(db.String)
    manager_id = db.Column(db.Integer, db.ForeignKey( 'users.id_user'))
