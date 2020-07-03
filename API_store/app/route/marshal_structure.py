from flask_restful import fields

users_structure = {
    "id_user": fields.Integer,
    "name": fields.String,
    "email": fields.String,
}

goods_structure = {
    'id_goods': fields.Integer,
    'name': fields.String,
    'brand': fields.String,
}

stores_structure = {
    'id_stroes': fields.Integer,
    'name': fields.String,
    'city': fields.String,
    'address': fields.String,
    'manager_id':fields.Integer
}
