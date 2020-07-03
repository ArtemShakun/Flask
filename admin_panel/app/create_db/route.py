from flask_restful import Resource
from sqlalchemy_utils import create_database, drop_database, database_exists
from models.models import Manager, Good, Store
from create_db.populate_data import get_managers, get_store, get_goods
from db import db



class CreateDB(Resource):

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
    def get(self):
        stores = get_store()
        managers = get_managers()
        goods = get_goods()
        for store in stores:
            db.session.add(Store(**store))
        for good in goods:
            db.session.add(Good(**good))
        for manager in managers:
            db.session.add(Manager(**manager))
        db.session.commit()
        return 'Date written in data_base successfully'
