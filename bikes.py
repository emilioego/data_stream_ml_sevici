import requests
import pandas as pd
import sqlite3
import traceback
import time

# Setting up
NAME = "Dublin"
STATIONS = "https://api.jcdecaux.com/vls/v1/stations"
APIKEY = "1c8d24323042b11c89877648adfe3c180f15fa3c"
    
conn = sqlite3.connect("dublinBikes.db") # Connect to database (creates if it does not exist)
cursor = conn.cursor()

# Create a new table in the current database
# Specify column names and data types
cursor.execute("CREATE TABLE IF NOT EXISTS dublinBikes (address text, available_bike_stands integer, available_bikes integer, banking integer, bike_stands integer, bonus integer, contract_name text, last_update integer, name text, number integer, position_lat real, position_lng real, status text)")
conn.commit() # Save the changes

def add_to_database(dataframe):
    """ Function to add information to the database """
    
    # df.shape returns the number of columns and rows in a dataframe
    # So using the first value returned, we can cycle through each row in the dataframe (where each row has information on a specific station)
    for i in range(0, (dataframe.shape[0]-1)):
        data = dataframe.iloc[i] # df.iloc[] just allows us to access elements via normal indexing of a pandas dataframe
        
        # Store all the information from the dataframe in a list
        elements = [data.get("address"), int(data.get("available_bike_stands")), int(data.get("available_bikes")), int(data.get("banking")), int(data.get("bike_stands")), int(data.get("bonus")), data.get("contract_name"), float(data.get("last_update")), data.get("name"), int(data.get("number")), data.get("position").get("lat"), data.get("position").get("lng"), data.get("status")]
        
        # Add each of these elements to the table in our database
        cursor.execute("INSERT INTO dublinBikes VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", elements)
    conn.commit()
    
# Always run
while True:

    try:
        # Access info on JCDecaux website using API key
        # Convert the JSON information into a pandas dataframe format
        df = pd.read_json("https://api.jcdecaux.com/vls/v1/stations?contract=" + NAME + "&apiKey=" + APIKEY)

        # Add the information to the database
        add_to_database(df)

        # Sleep for 5 minutes
        time.sleep(15)

    except:
        # Print traceback if there is an error
        print(traceback.format_exc())
