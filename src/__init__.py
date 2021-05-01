from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, Table
from sqlalchemy.sql.schema import MetaData
import pandas as pd



# print(Base.metadata.tables)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'adsfjkahdfkjlahoiuwncvejiasnd'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:c1W9d9Cx$@localhost:5432/aviation'
    # db = SQLAlchemy(app)
    engine = create_engine(
    "postgres://postgres:c1W9d9Cx$@localhost:5432/aviation")
    flight_details = pd.read_sql_query('SELECT * FROM flight_details', engine.connect())
    for rows in flight_details:
        print(rows) 
    
    from .views import views

    app.register_blueprint(views, url_prefix = '/')
   
    

    return app