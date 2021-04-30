import sqlalchemy
from sqlalchemy.sql import func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import engine
from sqlalchemy import create_engine, func, MetaData, Table
from flask import Flask, jsonify
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from config import conn_str

DATABASE_URI = conn_str
engine = create_engine('DATABASE_URI', isolation_level="AUTOCOMMIT")
Base = declarative_base()
Base.metadata = reflect()

# with engine.connect() as connection:
#     meta = MetaData(engine)
#     airlines_table = Table('airlines', metadata, autoload=True, autoload_with=engine)

class airports(Base):
    __tablename__ = 'airports'

    airport_id = Column(Integer, primary_key=True)
    airport = Column(String(length=50))
    iata = Column(String(length=5))
    icao = Column(String(length=5))
    timezone = Column(String(length = 25))

    def __repr__(self):
        return '''<airports(airport_id='{0}', airport='{1}', iata='{2}', icao='{3}', timezone='{4}')>'''.format(self.airport_id, self.airport, self.iata, self.icao, self.timezone)

class airlines(Base):
    __tablename__ = 'airlines'

    airlines_id = Column(Integer, primary_key=True)
    airline = Column(String(length=50))
    iata = Column(String(length=5))
    icao = Column(String(length=5))

    def __repr__(self):
        return '''<airlines(airline_id='{0})', airline='{1}', iata='{2}', icao='{3}')>'''.format(self.airline_id, self.airline, self.iata, self.icao)

class flights(Base):
    __tablename__ = 'flights'

    flight_id = Column(Integer, primary_key=True)
    flight_number = Column(String(length=5))
    flight_type = Column(String(length=15))
    iata = Column(String(length=5))
    icao = Column(String(length=5))
    airport_id = Column(String(length=5))
    terminal = Column(String(length=5))
    gate = Column(String(length=5))
    baggage = Column(String(length=5))
    delay = Column(String(length=8))
    scheduled= Column(String(length = 15))
    estimated = Column(String(length = 15))
    actual = Column(String(length = 15))
    estimated_runway = Column(String(length = 15))
    actual_runway = Column(String(length = 15))

    def __repr__(self):
        return '''<flights(flight_id='{0}', flight_number='{1}', flight_type='{2}', iata='{3}', icao='{4}', airport_id='{5}', terminal='{6}', gate='{7}', baggage='{8}', delay='{9}', scheduled='{10}', estimated='{11}', actual='{12}', estimated='{13}', estimated_runway='{14}', actual_runway='{15}')>'''.format(self.flight_id, self.flight_number, self.flight_type, self.iata, self.icao, self.airline_id, self.terminal, self.gate, self.baggage, self.delay, self.scheduled, self.estimated, self.actual, self.estimated_runway, self.actual_runway)

    Base.metadata.create_all(engine)

    def create_session():
        session = sessionmaker(bind=engine)
        return session()
