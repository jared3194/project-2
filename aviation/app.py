from app import create_app
from sqlalchemy import engine
from sqlalchemy import create_engine, func, MetaData, Table
from flask import Flask, jsonify
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

app = create_app()

if __name__== '__main__':
    app.run(debug=True)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base = declarative_base()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
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