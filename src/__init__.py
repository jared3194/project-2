from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, Table
from sqlalchemy.sql.schema import MetaData

engine = create_engine("postgres://postgres:c1W9d9Cx$@localhost:5432/aviation")
metadata = MetaData()
metadata.reflect(engine, only = ['airlines', 'airports', 'flights'])
Base = automap_base(metadata = metadata)
Base.prepare()

# print(Base.metadata.tables)
Airlines = Base.classes.airlines
print(Airlines)

def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:c1W9d9Cx$@localhost:5432/aviation'
    # db = SQLAlchemy(app)
    from .views import views

    app.register_blueprint(views, url_prefix = '/')
    # from .models import airlines
    

    return app