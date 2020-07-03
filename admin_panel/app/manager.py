from app import run_app
from db import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = run_app()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
