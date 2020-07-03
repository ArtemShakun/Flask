from flask import Blueprint
from flask_restful import Api
from route.route import CreateUser, CreateGood, CreateStore

create_users = Blueprint('create_users', __name__)
create_store = Blueprint('create_store', __name__)
create_goods = Blueprint('create_goods', __name__)

api_create_users = Api(create_users)
api_create_store = Api(create_store)
api_create_goods = Api(create_goods)

api_create_users.add_resource(CreateUser, '/create_users', '/create_users/<id_user>')
api_create_goods.add_resource(CreateGood, '/create_goods', '/create_goods/<id_goods>')
api_create_store.add_resource(CreateStore,'/create_store', '/create_store/<id_stroes>')
