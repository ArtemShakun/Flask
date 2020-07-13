from flask import Flask
from config import Configuration
from db import db

def run_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)
    db.init_app(app)
    return app
