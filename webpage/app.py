from flask import Flask, render_template, g
import json
import sqlite3

# Static files are served from '/static' directory
app = Flask(__name__, static_url_path='')
app.config.from_object('config')

# Connect to database using config.py file
# This contains API key and name of our database file
def db_connect():
    return sqlite3.connect(app.config["DATABASE"])

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = db_connect()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# This route serves '/static/bikes.html'
@app.route('/')
def begin():
    return render_template('index.html', MAPS_APIKEY = app.config["MAPS_APIKEY"])

# Function to return the average number of available bikes each day during the week for
# a specified station
@app.route('/weekly/<int:number>')
def get_weekly_info(number):
    con=get_db()
    cur=con.cursor()
    cur.execute("SELECT day, AVG(available_bikes) FROM dublinBikes \
            WHERE number = {} GROUP BY day".format(number))
    data=cur.fetchall()
    # Return as JSON so that it may be parsed and accessed as required to generate graphs on the page
    return json.dumps(data)

# Function to return hourly averages for a specified station on a particular day
@app.route('/daily/<int:number>/<weekday>')
def get_hourly_info(number, weekday):
    con=get_db()
    cur=con.cursor()
    cur.execute("SELECT AVG(available_bikes), hour FROM dublinBikes \
            WHERE number = {} AND day = \"{}\" GROUP BY hour".format(number, weekday))
    data=cur.fetchall()
    return json.dumps(data)

if __name__ == "__main__":
    app.run(debug=True)
