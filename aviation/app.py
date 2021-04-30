from flask import Flask
import os.path
from config import conn_str
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy.sql import func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import engine
from sqlalchemy import create_engine, func, MetaData, Table
from flask import Flask, jsonify
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URI = conn_str
engine = create_engine(DATABASE_URI)
Base = declarative_base()

# bp = Blueprint('app.py', __name__)

app = Flask(__name__)
app.config['DATABASE_URL'] = conn_str
app.config['SECRET_KEY'] ='C\xcd\x15t\xaf-\xa3\x80`\xf1!u\xbaBE\x03K\x9d\xdf\xc1\x90H\xf2\xf2/'

db = SQLAlchemy(app)


    
Base.metadata.create_all(engine)

def create_session():
    session = sessionmaker(bind=engine)
    return session()

@app.route('/')
def Base():
    return ("base.html")

app.run(debug=True, host="127.0.0.1", port=5000)

    