
Biking Dublin
-----------------

<img src="http://www.transportforireland.ie/assets/dublin-bikes2.png"
 alt="Biking Dublin" title="BikingDublin" align="right" />
Contributors:  
Brendan Dwyer,   
Michael McNulty,   
Romain Ducarrouge   
 
This program was designed to collect dynamic data from the JCDecaux API about Dublin City Bikes
usage on a daily basis. The data collection was processed on an Amazon Web Service instance, EC2, 
and the data was saved to a SQLite database.  
This is used to predict which time and which bike stations are likely to have available bikes 
when a user is trying to rent or return the bicycle.

This program is intended to collect dynamic data from the JCDecaux API about Dublin City Bikes
usage on a daily basis. 
This is used to predict which bike stations and at which times are likely to have available bikes 
when a user is trying to rent or return a bicycle.



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
The 'Biking Dublin' application is intended for users to get real time information regarding
bikes availability for hiring and returning at various bike stations throughout Dublin city.
The application also offers historical data regarding the daily and hourly availability of bikes 
based on stations.

 * For a full description of the module, visit the project page:
   https://github.com/DucarrougeR/DublinBikes

 * To submit bug reports and feature suggestions, or to track changes:
   https://github.com/DucarrougeR/DublinBikes
 
![Alt text](/Documentation/Process.jpg?raw=true "Data Collection Process")
 
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
 
 
TROUBLESHOOTING
-----------------
 * If the application does not display, check the following:

   - the HTML file is in the same folder as the CSS file and the Python File and SQLITE databases

   - is your browser older than:   
		Internet Explorer 7?   
		Firefox 43?   
		Safari 9.1?   
		Chrome 48?  

FAQ
-----------------

Q: 	Why are there three colors for the circles on the map?

A: 	Each circle represents a unique bike station. The color of that circle represents its
	current bike availability status.   
	-Red Color: the station has less than 25% of the bikes available for hire.  
	-Orange Color: the station has between 25% and 75% of bikes available for hire.  
	-Green Color: the station has over 75% of the bikes available for hire.  
 ----------------------------------------------------------------------------------------------------------
 Q:	What is the difference between the two graphs on the page?
 
 A:	The first graph (on the left side of the page) indicates the average occupancy of the station on a 
	daily basis for a week. The second graph (on the right side of the page) reflects the average occupancy 
	on an hourly basis for the specific day chosen. 
 ----------------------------------------------------------------------------------------------------------
 Q:	
 
 A:	
 
 LICENSE
-----------
 The MIT License (MIT)

Copyright (c) 2016 Nathan Epstein

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
