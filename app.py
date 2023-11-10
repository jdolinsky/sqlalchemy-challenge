# Import the dependencies.
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from numpy import array
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    """List all available routes"""
    return (
        """
            <h1>Available Routes:</h1>
            <ul>
                <li>Precipitation in last 12 months: <a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a></li>
                <li>List of stations: <a href='/api/v1.0/stations'>/api/v1.0/stations</a></li>
                <li>Temperatures in last 12 months: <a href='/api/v1.0/tobs'>/api/v1.0/tobs</a></li>
                <li>Temperature stats from the start date yyyy-mm-dd: <a href='/api/v1.0/start'>/api/v1.0/{yyyy-mm-dd}</a></li>
                <li>Temperature stats from the beginning to the end time period: <a href='/api/v1.0/start/end'>/api/v1.0/{yyyy-mm-dd}/{yyyy-mm-dd}</a></li>
            </ul>
        """
    )

@app.route("/api/v1.0/precipitation")
def precip():
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    last_date = dt.datetime.strptime(last_date, '%Y-%m-%d')
    query_date = dt.date(last_date.year -1, last_date.month, last_date.day)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= query_date).all()
    session.close()
    response = []
    # Convert results into a list
    results = list(np.ravel(results))
    print(results)
    for i in range(0, len(results), 2):
        # Create a new dictionary.
        dictionary = {}
        dictionary["date"] = results[i]
        dictionary["prcp"] = results[i+1]
        response.append(dictionary)
    return jsonify(response)