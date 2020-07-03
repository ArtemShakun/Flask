from flask import Flask
from db import db
from config import Configuration
from route import create_users, create_store, create_goods
from create_db import create_db, create_data

def run_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)
    db.init_app(app)
    app.register_blueprint(create_users)
    app.register_blueprint(create_store)
    app.register_blueprint(create_goods)
    app.register_blueprint(create_db)
    app.register_blueprint(create_data)
    return app
