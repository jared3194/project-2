import sqlalchemy
from sqlalchemy.sql import func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import engine
from sqlalchemy import create_engine, func, MetaData, Table
from flask import Flask, jsonify
from sqlalchemy.orm import Session
from config import conn_str

DATABASE_URI = conn_str
engine = create_engine('DATABASE_URI', isolation_leve="AUTOCOMMIT")
Base = declarative_base(engine)
Base.metadata = reflect(engine)

with engine.connect() as connection:
    meta = MetaData(engine)
    airlines_table = Table('airlines', metadata, autoload=True, autoload_with=engine)

class airports(Base):
    _table_ = Base.metadata.tables['airports']

    def _repr_(self):
        return '''<airlines(airport_id='{0}', airport='{1}', iata='{2}', icao='{3}', timezone='{4}'>'''.format(self.airport_id, self.airport, self.iata, self.icao, self.timezone)

if _name_ == "_base_":
    with engine.connect() as connection:
        connection.execute("COMMIT")
        connection.execute('CALL airports')