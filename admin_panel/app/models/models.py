from db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from login import login


class Store(db.Model):
    __tablename__ = 'stores'

    id_store = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    city = db.Column(db.String)
    address = db.Column(db.String)
    managers = db.relationship('Manager', backref='stores')

class Manager(db.Model):
    __tablename__ = 'managers'

    id_manager = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    position = db.Column(db.String)
    phone = db.Column(db.Integer)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id_store'))

class Good(db.Model):
    __tablename__ = 'goods'

    id_goods = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    name = db.Column(db.String)
    price = db.Column(db.Float)


class User(db.Model,UserMixin):
    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), index=True, unique=True)
    email = db.Column(db.String(30), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.id_user

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))
