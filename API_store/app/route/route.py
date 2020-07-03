from db import db
from flask_restful import Resource, marshal
from models.models import User, Good, Store
from route.marshal_structure import users_structure, goods_structure, stores_structure
from flask import request


class CreateUser(Resource):
    def get(self, id_user=None):
        if id_user:
            user = User.query.get(id_user)
            if user:
                return marshal(user, users_structure)
            return f'No such user with id: {id_user}'
        return marshal(User.query.all(), users_structure)

    def post(self):
        user = User(**request.json)
        db.session.add(user)
        db.session.commit()
        return f"Successfully added a new user {user}"

    def put(self, id_user):
        user = User.query.get(id_user)
        user.name = request.json.get('name', user.name)
        user.email = request.json.get('email', user.email)
        user.password = request.json.get('password', user.password)
        db.session.commit()
        return f'Successfully updated User with id: {id_user}'

    def delete(self, id_user):
        user = User.query.get(id_user)
        db.session.delete(user)
        db.session.commit()
        return f"Successfully deleted User with id: {id_user}"


class CreateGood(Resource):
    def get(self, id_goods=None):
        if id_goods:
            good = Good.query.get(id_goods)
            if good:
                return marshal(good, goods_structure)
            return f'No such goods with id: {good}'
        return marshal (Good.query.all(), goods_structure)

    def post(self):
        '''Works'''
        goods = Good(**request.json)
        db.session.add(goods)
        db.session.commit()
        return f"Successfully added a new goods {goods}"

    def put(self, id_goods):
        '''Works'''
        good = Good.query.get(id_goods)
        good.name = request.json.get('name', good.name)
        good.brand = request.json.get('brand', good.brand)
        db.session.commit()
        return f'Successfully updated Good with id: {id_goods}'

    def delete(self, id_goods):
        '''Works'''
        good = Good.query.get(id_goods)
        db.session.delete(good)
        db.session.commit()


class CreateStore(Resource):
    def get(self, id_stroes=None):
        if id_stroes:
            store = Store.query.get(id_stroes)
            if store:
                return marshal(store, stores_structure)
            return f'No such store with id: {id_stroes}'
        return marshal(Store.query.all(), stores_structure)

    def post(self):
        store = Store(**request.json)
        users = User.query.all()
        users_id = []
        for user in users:
            users_id.append(int(user.id_user))
        if store.manager_id in users_id:
            db.session.add(store)
            db.session.commit()
            return f"Successfully added a new store {store}"
        else:
            return f'Manager with such id does not exist'

    def put(self, id_stroes):
        store = Store.query.get(id_stroes)
        users = User.query.all()
        users_id = []
        store.name = request.json.get('name', store.name)
        store.city = request.json.get('city', store.city)
        store.address = request.json.get('address', store.address)
        store.manager_id = request.json.get('manager_id', store.manager_id)
        for user in users:
            users_id.append(int(user.id_user))
        if store.manager_id in users_id:
            db.session.commit()
            return f"Successfully update store"
        else:
            return f'Manager with such id does not exist'

    def delete(self, id_stroes):
        store  = Store.query.get(id_stroes)
        db.session.delete(store)
        db.session.commit()
