import requests
import sqlite3
import traceback
import time

# Setting up
NAME = "Dublin"
STATIONS = "https://api.jcdecaux.com/vls/v1/stations"
APIKEY = "1c8d24323042b11c89877648adfe3c180f15fa3c"

r = requests.get("https://api.jcdecaux.com/vls/v1/stations?contract=" + NAME + "&apiKey=" + APIKEY)

conn = sqlite3.connect("dublinBikes.db") # Connect to database (creates if it does not exist)
cursor = conn.cursor()

# Create a new table in the current database
# Specify column names and data types
cursor.execute("CREATE TABLE IF NOT EXISTS dublinBikes (address text, available_bike_stands integer, available_bikes integer, banking integer, bike_stands integer, bonus integer, contract_name text, last_update integer, name text, number integer, position_lat real, position_lng real, status text)")
conn.commit() # Save the changes

def add_to_database(json_data):
    """ Function to add information to the database """
    
    # Cycle through each element in the json file relating to individual stations
    for i in range(0, (len(json_data)-1)):
        data = json_data[i]
        # Store all the information in a list
        elements = [data.get("address"), int(data.get("available_bike_stands")), int(data.get("available_bikes")), int(data.get("banking")), int(data.get("bike_stands")), int(data.get("bonus")), data.get("contract_name"), float(data.get("last_update")), data.get("name"), int(data.get("number")), data.get("position").get("lat"), data.get("position").get("lng"), data.get("status")]
        
        # Add each of these elements to the table in our database
        cursor.execute("INSERT INTO dublinBikes VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", elements)
    conn.commit()
    
# Always run
while True:

    try:
        # Access info on JCDecaux website using API key
        # Convert the JSON information into a response object using requests.get()
        r = requests.get("https://api.jcdecaux.com/vls/v1/stations?contract=" + NAME + "&apiKey=" + APIKEY)
        
        
        # Add the information to the database
        add_to_database(r.json())

        # Sleep for 5 minutes
        time.sleep(5*60)

    except:
        # Print traceback if there is an error
        print traceback.format_exc()
