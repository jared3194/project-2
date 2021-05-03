<<<<<<< HEAD
import numpy as np
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import datetime as dt
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template, redirect
from config import password, user
=======
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import engine
from sqlalchemy import log
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, Table
from sqlalchemy.sql.schema import MetaData
import pandas as pd
from flask import Blueprint, render_template, Flask, jsonify



#connect to database
# engine = create_engine("postgres://postgres:welcome1$@localhost:5432/aviation")

# DATABASE_URL = f'postgresql://postgres:welcome1@localhost:5432/aviation'
#conn = create_engine(f'postgresql://postgres:{sqlkey}@localhost:5432/aviation').connect()
>>>>>>> 84942b0f9f605ce96509aef6db26eaa93d59e9e7


#################################################
# Database Setup
#################################################
<<<<<<< HEAD
engine = create_engine(
    "postgres://postgres:#babyHugo17@localhost:5432/aviation")

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)

# Save reference to the table
# flights = Base.classes.flights
# airports = Base.classes.airports

# print(Base.classes.keys())

session = Session(bind=engine)
# query1 = f"select {column} from {table};"
# try:
#     for row in pd.read_sql_query('SELECT * FROM flights', engine.connect()):
#         result = dict(row.items())
# for row in pd.read_sql_query('SELECT * FROM flights', engine.connect()):
#     print(row)
#################################################
# Flask Routes
#################################################
# * `/`
#   * Home page.
#   * List all routes that are available.
app = Flask(__name__)

# for rows in pd.read_sql_query('SELECT * FROM flights', engine.connect()):
#     print(rows)


@app.route("/")
def welcome():
    # flight_details = pd.read_sql_query(
    #     'SELECT * FROM flight_details', engine.connect())
    # print(flight_details)
    return render_template("index.html")

# # # #   * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
# # # #   * Return the JSON representation of your dictionary.


@app.route("/aviation")
def aviation():
    results = pd.read_sql_query('SELECT * FROM international', engine.connect()).to_dict()
    return results 
    # print(results)


# #     # session.close()
if __name__ == '__main__':
    app.run(debug=True)
=======
# engine = create_engine(DATABASE_URL)


# flight_details = pd.read_sql_query('SELECT * FROM flight_details', engine.connect()).to_dict()

# Create app

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/chart1')
def chart1():
    return render_template("base1.html")   #bar chart

@app.route('/chart2')
def chart2():
    return render_template("base2.html")       #scatter

@app.route('/chart3')
def chart3():
    return render_template("base3.html")       #scatter

# @app.route('/api/data')
# def api():
#     return flight_details

if __name__ == '__main__':
    app.run(debug = True)

   
# d3.json('/api/data').then(data=>{
#     console.log(data)
# }) 
>>>>>>> 84942b0f9f605ce96509aef6db26eaa93d59e9e7
