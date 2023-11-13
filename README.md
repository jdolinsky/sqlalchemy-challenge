# SQLAlchemy Challenge
# Climate analysis on the Honolulu area

## Part 1 - Climate Analysis and Exploration
Use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate [database](resources/hawaii.sqlite). The analysis include Precipitation Analysis, Station Analysis, and Temperature Observation Analysis.
## Part 2 - Design Your Climate Web App
Create an API with the following routes:
* /api/v1.0/precipitation  - returns last 12 months of data of precipitation data
* /api/v1.0/stations - returns a list of stations from the dataset
* /api/v1.0/tobs - returns a list of temperature observations for the previous year
* /api/v1.0/&lt;start>  and  /api/v1.0/&lt;start>/&lt;end> - returns a list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range

## Data Source
[Database - hawaii.sqllite](resources/hawaii.sqlite)

Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910

## Technologies
Python, SQLAlchemy, Pandas, Matplotlib, Numpy, and Flask.