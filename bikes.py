import pandas as pd
import requests
import json
import time
import os


NAME = "Dublin"
STATIONS = "https://api.jcdecaux.com/vls/v1/stations"
APIKEY = "1c8d24323042b11c89877648adfe3c180f15fa3c"

r = requests.get(STATIONS, params={"apiKey": APIKEY, "contract": NAME})
  
# Store json data as python list
json = r.json()

# Convert list to pandas dataframe
df = pd.DataFrame(json)
df['scrape_time'] = time.strftime('%H:%M:%S', time.gmtime())
df['scrape_date'] = time.strftime('%Y-%m-%d', time.gmtime())

# Convert to csv
if os.path.isfile("test.csv"): # exectuted if file exists
    with open("test.csv", "a") as f:
        # header=false so that column names are not reprinted
        df.to_csv(f, header=False)
else: # creates file if it does not exist
     with open("test.csv", "a") as f:
        df.to_csv(f)
