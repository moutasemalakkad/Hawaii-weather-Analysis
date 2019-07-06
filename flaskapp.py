from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from flask import Flask
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import numpy as np
import sqlalchemy





engine = create_engine("sqlite:///hawaiicopy.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)


max_date = engine.execute("SELECT max(date) FROM measurement").fetchall()
max_date = max_date[0][0]
max_date


today = dt.date.today()
max_dateformat = today.replace(year=int(max_date[:4]),month=int(max_date[5:7]),day=int(max_date[8:]))
Last_date_year = max_dateformat - dt.timedelta(days=365)    
Start_Date = Last_date_year.strftime("%Y-%m-%d")
print(Start_Date)


prec = session.query(Measurement.prcp)\
             .filter(Measurement.date >= Start_Date)\
             .filter(Measurement.date <= max_date)\
             .order_by(Measurement.date.desc())\
             .all()

dates = session.query(Measurement.date)\
             .filter(Measurement.date >= Start_Date)\
             .filter(Measurement.date <= max_date)\
             .order_by(Measurement.date.desc())\
             .all()


dic = {dates:prec}



app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/passengers"
    )



if __name__ == '__main__':
    app.run(debug=True)
