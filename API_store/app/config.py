class Configuration:
    PG_USER = "shakun"
    PG_PASSWORD = 'qwerty'
    PG_HOST = "db"
    PG_PORT = 5432
    DB_NAME = "work_sql"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
