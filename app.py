from flask import Flask, render_template, g, jsonify
import json
import pandas as pd
import sqlite3

# Static files are served from '/static' directory
app = Flask(__name__, static_url_path='')
app.config.from_object('config')

# Connect to database using config.py file
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

@app.route('/station/<int:number>')
def display_info(number):
    con=get_db()
    cur=con.cursor()
    cur.execute("SELECT last_update, available_bikes FROM dublinBikes WHERE number ={}".format(number))
    data=cur.fetchall()
    cur.execute("SELECT address FROM dublinBikes WHERE number={}".format(number))
    name=cur.fetchone()
    return render_template('bikes_info.html', station_name=name[0])

if __name__ == "__main__":
    app.run(debug=True)
