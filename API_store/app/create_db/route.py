from flask_restful import Resource
from sqlalchemy_utils import create_database, drop_database, database_exists
from models.models import User, Good, Store
from create_db.populate_data import get_users, get_store, get_goods
from db import db



class CreateDB(Resource):
    '''works'''
    def get(self):
        if database_exists(db.engine.url):
            db.create_all()
            db.session.commit()
            print('database_exists')
        else:
            print(f'Database does not exists {db.engine.url}')
            create_database(db.engine.url)
            db.create_all()
            db.session.commit()
            print('Database_created')

class CreateData(Resource):
    '''works'''
    def get(self):
        users = get_users()
        goods = get_goods()
        stores = get_store()
        for user in users:
            db.session.add(User(**user))
        for good in goods:
            db.session.add(Good(**good))
        for store in stores:
            db.session.add(Store(**store))
        db.session.commit()
        return 'Date written in data_base successfully'
