## Climate analysis using SQLAlchemy (sqlite) & Flask data endpoints

![surfs-up.jpeg](Images/surfs-up.jpeg)


__Technology stack__ : Python, SQLAlchemy ORM, SQLite, Pandas, Matplotlib, Flask (JSON API endpoints)

# Data Preparation
Climate data for Hawaii was provided in two CSV files. The content of these files was scrubbed.

* Jupyter Notebook data_engineering.ipynb takes care of data preparation / cleanup tasks.
* Pandas dataframes are created from the measurement and station CSV files.
* NaNs / missing values are cleaned from the data, and cleaned CSV files are saved.
# Database Engineering
Using SQLAlchemy to model database schema, sqlite tables for "measurements" and "stations" are created.

- Jupyter Notebook database_engineering.ipynb used for database engineering work.
- Pandas used to read cleaned measurements and stations CSV data.
- Database called hawaii.sqlite created, using declarative_base to create ORM classes for each table, and used create_all to  populate database.
# Climate Analysis
- Climate analysis and data exploration on new weather tables.

- Jupyter Notebook file called climate_analysis.ipynb used to complete climate analysis and data exporation.
- Start date and end date determine "vacation" range.
- Used SQLAlchemy create_engine to connect to sqlite database, and automap_base() to reflect tables into classes. Referenced those classes as Station and Measurement.

# Precipitation analysis
- Queries retrieve the last 12 months of precipitation data, and results are plotted using matplotlib
- Pandas dataframes house the summary statistics for the precipitation data.
# Station analysis
- Calculations of the total number of stations, and most active stations.
- Retrieval of the last 12 months of temperature observation data (tobs), filtered by the station with the highest number of observations.
- Plotted results as a histogram with bins=12.
# Temperature analysis
- Function calc_temps accepts a start date and end date in the format %Y-%m-%d, returns the minimum, average, and maximum temperatures for that range of dates.
- Function calculates min, avg, and max temperatures for trip using the matching dates from the previous year (i.e. use "2017-01-01" if trip start date was "2018-01-01")
- Plotted the min, avg, and max temperature from previous query as a bar chart.
  - Used the average temperature as the bar height.
  - Used the peak-to-peak (tmax-tmin) value as the y error bar (yerr).
 # Flask Web Application
  - Flask web app with routes (endpoints) displaying JSON data results from each of the above queries.

# Routes (API endpoints)
* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * query for the dates and temperature observations from a year from the last data point.
  * Return a JSON list of Temperature Observations (tobs) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.


## Images From the Analysis


![station-histogram.png](Images/station-histogram.png)

![daily-normals.png](daily-normals.png)

