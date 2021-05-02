import numpy as np
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import datetime as dt
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template, redirect
#from config import conn_str#DATABASE_URL

DATABASE_URL = f'postgresql://postgres:welcome1@localhost:5432/aviation'
#conn = create_engine(f'postgresql://postgres:{sqlkey}@localhost:5432/aviation').connect()


#################################################
# Database Setup
#################################################
engine = create_engine(DATABASE_URL)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
flights = Base.classes.flights
airports = Base.classes.airports
arrivals = Base.classes.arrival

print(Base.classes.keys())

session = Session(bind=engine)

for row in pd.read_sql_query('SELECT * FROM arrivals', engine.connect()):
    print(row)
#################################################
# Flask Routes
#################################################
# * `/`
#   * Home page.
#   * List all routes that are available.
app = Flask(__name__)

# for rows in pd.read_sql_query('SELECT * FROM flight_details', engine.connect()):
#         return rows
@app.route("/")
def welcome():
    return render_template("base.html")

# # #   * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
# # #   * Return the JSON representation of your dictionary.


@app.route("/aviation")
def aviation():
    results = pd.read_sql_query('SELECT * FROM arrival', engine.connect()).to_dict()
    return results


    # session.close()
if __name__ == '__main__':
    app.run(debug=True)