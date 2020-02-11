
Biking Seville
-----------------

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTKj4fPzPujSAxdx6mq6YG8xJQ-iUwoFyxxAvC-cLkbEuXKutHz"
 alt="Biking Dublin" title="BikingDublin" align="right" />
Authors:  
Lucía Falcón,
Emilio García
 
This program was designed to collect dynamic data from the JCDecaux API about Seville City Bikes
usage on a daily basis. The data collection was processed on an laptop locally and the data was 
saved to a SQLite database.  
This is used to predict which time and which bike stations are likely to have available bikes 
when a user is trying to rent or return the bicycle.


CONTENTS OF THIS FILE
-----------------
   
 * Introduction
 * Requirements
 * Recommended modules
 * Installation
 * Configuration
 * Troubleshooting
 * FAQ
 * License

 
INTRODUCTION
-----------------
The 'Biking Seville' application is intended for users to get real time information regarding
bikes availability for hiring and returning at various bike stations throughout Seville city.
The application also offers historical data regarding the daily and hourly availability of bikes 
based on stations.

 
REQUIREMENTS
-----------------
This module requires the following modules:

 * Python 3.X 
		https://www.python.org/downloads/
 * Pandas library for Python
		https://pypi.python.org/pypi/pandas/
 * Flask framework version 0.10.1
		https://pypi.python.org/pypi/Flask
 * SQLite to connect the web application to the database
		https://www.sqlite.org/download.html
 
 
RECOMMENDED MODULES
--------------------
 * Python 3.5.0
		https://www.python.org/downloads/release/python-350/
 * Pandas 0.18 library for Python
		https://pypi.python.org/pypi/pandas/0.18.0/#downloads
 
 
INSTALLATION
-----------------
 * 	Once all the required modules are installed on the computer, you may launch the html file which
	will integrate with the SQL database using the Flask framework to fetch the data based on user input.

![Alt text](/Documentation/Architecture.jpg?raw=true "Web App Architecture")
	
 * 	You may want to change the source code on the webpage (html, javascript files) if you would prefer to run 
	visualization using the pandas library to generate static graphs. Otherwise, keep the Google Charts script 
	as the default setup to allow for interactive graphs to be displayed.
 
CONFIGURATION
-----------------
 * 	The website application is designed to function without the need for configuration.

 * 	Select the stations in the drop down menu for information about a specific station.
	Additional information can be requested by selecting a particular day in order to access the 
	availability for the bike station on an hourly basis.

 * 	The graph displayed is interactive and displays the number of bikes when the mouse hovers above the 
	graph to offer more complete information.
 


FAQ
-----------------

Q: 	Why are there three colors for the circles on the map?

A: 	Each circle represents a unique bike station. The color of that circle represents its
	current bike availability status.
        -Black Color: the station hasn't got any bikes.
	-Red Color: the station has less than 25% of the bikes available for hire.  
	-Orange Color: the station has between 25% and 75% of bikes available for hire.  
	-Green Color: the station has over 75% of the bikes available for hire.  
 ----------------------------------------------------------------------------------------------------------

 
 
 LICENSE
-----------
 The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions 
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED 
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE.
