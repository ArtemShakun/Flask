from flask import Blueprint
from flask_restful import Api
from create_db.route import CreateDB, CreateData

create_db = Blueprint('create_db', __name__)
api_create_db = Api(create_db)
api_create_db.add_resource(CreateDB, '/create_db')


create_data = Blueprint('create_data', __name__)
api_create_data = Api(create_data)
api_create_data.add_resource(CreateData, '/create_data')
