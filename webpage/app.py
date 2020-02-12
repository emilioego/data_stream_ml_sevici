from flask import Flask, render_template, g
import json
import sqlite3

# Static files are served from '/static' directory
app = Flask(__name__, static_url_path='')
app.config.from_object('config')

# Connect to database using config.py file
# This contains API key and name of our database file
def db_connect():
    database = "../"+app.config["DATABASE"]
    return sqlite3.connect(database)

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
    names=[]
    numbers=[]
    frec=[]
    frec2=[]
    stations=[]
    hours=[]
    con=get_db()
    cur=con.cursor()
    cur.execute("SELECT DISTINCT address,number FROM seviBikes")
    data1=cur.fetchall()
    for row in data1:
        names.append(row[0])
        numbers.append(row[1])
    cur.execute("SELECT address ,hour,available_bikes,available_bike_stands from seviBikes where day = 'Sunday' and address = 'GLORIETA PLUS ULTRA - Aprox. Estadio Manuel Ruiz de Lopera' group by hour order by hour desc limit 10")
    data2=cur.fetchall()
    for row in data2:
        frec.append(row[2])
        frec2.append(row[3])
        stations.append(row[0])
        hours.append(row[1])
    return render_template('index.html', MAPS_APIKEY = app.config["MAPS_APIKEY"],len = len(data1),names = names,numbers=numbers,stations=stations,frec=frec,hours=hours,frec2=frec2)

# Function to return the average number of available bikes each day during the week for
# a specified station
@app.route('/weekly/<int:number>')
def get_weekly_info(number):
    con=get_db()
    cur=con.cursor()
    cur.execute("SELECT day, AVG(available_bikes) FROM seviBikes \
            WHERE number = {} GROUP BY day".format(number))
    data=cur.fetchall()
    # Return as JSON so that it may be parsed and accessed as required to generate graphs on the page
    return json.dumps(data)

# Function to return hourly averages for a specified station on a particular day
@app.route('/daily/<int:number>/<weekday>')
def get_hourly_info(number, weekday):
    con=get_db()
    cur=con.cursor()
    cur.execute("SELECT AVG(available_bikes), hour FROM seviBikes \
            WHERE number = {} AND day = \"{}\" GROUP BY hour".format(number, weekday))
    data=cur.fetchall()
    return json.dumps(data)

#SELECT AVG(available_bikes), address FROM seviBikes
            #WHERE day = 'Saturday' GROUP BY address ORDER BY AVG(available_bikes) DESC limit 10
			
#SELECT count(address),day  FROM seviBikes
            #WHERE address = 'GLORIETA PLUS ULTRA - Aprox. Estadio Manuel Ruiz de Lopera' GROUP BY day  
			
#SELECT count(address),hour  FROM seviBikes
            #WHERE address = 'GLORIETA PLUS ULTRA - Aprox. Estadio Manuel Ruiz de Lopera' GROUP BY hour
if __name__ == "__main__":
    app.run(debug=True)
