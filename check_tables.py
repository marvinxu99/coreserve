from app import create_app, db
from sqlalchemy import inspect

app = create_app("development")  # Ensure 'development' configuration is loaded

with app.app_context():

    print(app.config["SQLALCHEMY_DATABASE_URI"])
    print("db.engine.url=", db.engine.url)
    engine = db.engine
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("Tables in the coreserve1 database:", tables)
