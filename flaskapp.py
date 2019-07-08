import sqlalchemy
import numpy as np
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from flask import Flask, jsonify
from sqlalchemy.orm import Session



app = Flask(__name__)

# Create an engine 
engine = create_engine("sqlite:///hawaiicopy.sqlite")

# reflect 
Base = automap_base()

# tables reflect
Base.prepare(engine, reflect=True)

# reference tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session
session = Session(engine)


@app.route("/")
def home():
    print("Links available are:")
    print("/api/v1.0/prec")
    print("/api/v1.0/station")
    print("/api/v1.0/tobs")
    print("/api/v1.0/<start>")
    print("/api/v1.0/<start>/<end>")

@app.route("/api/v1.0/prec")
def precipitation():
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').order_by(Measurement.date)
    
    precipitation_values = []
    for p in results:
        prcp_dict = {}
        prcp_dict["date"] = p.date
        prcp_dict["prcp"] = p.prcp
        precipitation_values.append(prcp_dict)

    return jsonify(precipitation_values)


@app.route("/api/v1.0/station")
def stations():
    results = session.query(Station.name).all()

    station_names = list(np.ravel(results))

    return jsonify(station_names)

@app.route("/api/v1.0/tobs")
def tobs():
    results = session.query(Measurement.tobs).all()

    tobs_values = list(np.ravel(results))

    return jsonify(tobs_values)


@app.route("/api/v1.0/<start>")
def temperatures_start(start):
 
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).all()
    
    temperatures_start = list(np.ravel(results))

    return jsonify(temperatures_start)

@app.route("/api/v1.0/<start>/<end>")
def temperatures_start_end(start, end):

    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).\
                filter(Measurement.date <= end).all()
    
    temperatures_start_end = list(np.ravel(results))

    return jsonify(temperatures_start_end)


if __name__ == "__main__":
    app.run(debug=True)
