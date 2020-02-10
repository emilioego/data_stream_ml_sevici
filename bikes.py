import requests
import pandas as pd
import sqlite3
import traceback
import time
import datetime

# Setting up
NAME = "seville"
STATIONS = "https://api.jcdecaux.com/vls/v1/stations"
APIKEY = "2513ba8c201960d6193114b29d9be3e78dfce408"
    
conn = sqlite3.connect("seviBikes.db") # Connect to database (creates if it does not exist)
cursor = conn.cursor()

# Create a new table in the current database
# Specify column names and data types
cursor.execute("CREATE TABLE IF NOT EXISTS seviBikes (address text, available_bike_stands integer, available_bikes integer, banking integer, bike_stands integer, bonus integer, contract_name text, last_update integer, name text, number integer, position_lat real, position_lng real, status text,day varchar(10), date_time varchar(15),hour varchar(5))")
conn.commit() # Save the changes

def add_to_database(dataframe):
    """ Function to add information to the database """
    
    # df.shape returns the number of columns and rows in a dataframe
    # So using the first value returned, we can cycle through each row in the dataframe (where each row has information on a specific station)
    for i in range(0, (dataframe.shape[0]-1)):
        data = dataframe.iloc[i] # df.iloc[] just allows us to access elements via normal indexing of a pandas dataframe
        date_time = pd.to_datetime(data["last_update"]/1000,unit='s')
        day = str(date_time.day_name())
        hour = str(date_time.hour)
        # Store all the information from the dataframe in a list
        elements = [data.get("address"), int(data.get("available_bike_stands")), int(data.get("available_bikes")), int(data.get("banking")), int(data.get("bike_stands")), int(data.get("bonus")), data.get("contract_name"), float(data.get("last_update")), data.get("name"), int(data.get("number")), data.get("position").get("lat"), data.get("position").get("lng"), data.get("status"),day,str(date_time),str(hour)]
        
        # Add each of these elements to the table in our database
        cursor.execute("INSERT INTO seviBikes VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", elements)
    conn.commit()
    
# Always run
while True:

    try:
        # Access info on JCDecaux website using API key
        # Convert the JSON information into a pandas dataframe format
        df = pd.read_json("https://api.jcdecaux.com/vls/v1/stations?contract=" + NAME + "&apiKey=" + APIKEY)

        # Add the information to the database
        add_to_database(df)
        print("Insert")
        # Sleep for 5 minutes
        time.sleep(300)

    except:
        # Print traceback if there is an error
        print(traceback.format_exc())
