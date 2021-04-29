from sqlalchemy.sql import func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import engine
from sqlalchemy import create_engine, func, MetaData, Table

DATABASE_URI = 'postgres://postgres:c1W9d9Cx$@localhost:5432/aviation'
engine = create_engine(DATABASE_URI)
Base = automap_base()
metadata = MetaData()

class airlines(Base):
    
    Base.prepare(engine, reflect=True)
    airlines = Table('airlines', Base.metadata, autoload = True, autoload_with = engine)

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key = True)
#     email = db.Column(db.String(150), unique = True)
#     password = db.Column(db.String(150))
#     first_name = db.Column(db.String(150))
#     notes = db.relationship('Note')