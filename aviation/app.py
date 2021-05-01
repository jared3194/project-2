import numpy as np
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import datetime as dt
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template, redirect
from config import DATABASE_URL


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

print(Base.classes.keys())

session = Session(bind=engine)

for row in pd.read_sql_query('SELECT * FROM flights', engine.connect()):
    print(row)

#################################################
# Flask Routes
#################################################
# * `/`
#   * Home page.
#   * List all routes that are available.
app = Flask(__name__)

# for rows in pd.read_sql_query('SELECT * FROM flight_details', engine.connect()):
#         print rows

@app.route("/")
def welcome():
    return render_template("base.html")

# #   * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
# #   * Return the JSON representation of your dictionary.


@app.route("/api/aviation")
def aviation():
    flight_details = pd.read_sql_query('SELECT * FROM flight_details', engine.connect())
    print(flight_details)


    # session.close()
if __name__ == '__main__':
    app.run(debug=True)