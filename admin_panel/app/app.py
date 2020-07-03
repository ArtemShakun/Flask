from flask import Flask
from login import login
from db import db
from config import Configuration
from route.homePage import homePage
from route.goods import goods
from route.managers import managers
from route.stores import stores
from create_db import create_db, create_data



def run_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)
    db.init_app(app)
    login.init_app(app)
    app.register_blueprint(create_db)
    app.register_blueprint(create_data)
    app.register_blueprint(goods, url_prefix='/goods')
    app.register_blueprint(managers, url_prefix='/managers')
    app.register_blueprint(stores, url_prefix='/stores')
    app.register_blueprint(homePage)
    return app
