
=== Plugin Name ===

Biking Dublin

Contributors: Brendan Dwyer, Michael McNulty, Romain Ducarrouge  
 

This program is intended to collect dynamic data from the JCDecaux API about Dublin City Bikes
usage on a daily basis. 
This is used to predict which time and which bike stations are likely to have available bikes 
when a user is trying to rent the bicycle.


==CONTENTS OF THIS FILE==
-------------------------
   
 * Introduction
 * Requirements
 * Recommended modules
 * Installation
 * Configuration
 * Troubleshooting
 * FAQ
 * Maintainers

 
==INTRODUCTION==
----------------
The Biking Dublin application is intended for users to get real time information regarding
bikes availability for hiring and returning at various bike stations throughout Dublin city.
The application also offers historical data regarding bikes availability based on stations,
daily and hourly.
 * For a full description of the module, visit the project page:
   https://github.com/DucarrougeR/DublinBikes

 * To submit bug reports and feature suggestions, or to track changes:
   https://github.com/DucarrougeR/DublinBikes
 
 
==REQUIREMENTS==
----------------
This module requires the following modules:

 * Python 3.X 
		https://www.python.org/downloads/
 * Pandas 0.18 library for Pyton
		https://pypi.python.org/pypi/pandas/0.18.0/#downloads
 * Flask framework.
		https://pypi.python.org/pypi/Flask
 * SQLite to connect the web application to the database
		https://www.sqlite.org/download.html
 
 
==RECOMMENDED MODULES==

 * Python 3.5
		https://www.python.org/downloads/release/python-350/
 
 
==INSTALLATION==
----------------
 * Once all the required modules are installed on the computer, you may launch the html file which
	will integrate with the SQL database using the Flask framework to fetch the data based on user input.

 * You may want to disable Toolbar module, since its output clashes with
   Administration Menu.
 
 
==CONFIGURATION==
-----------------
 * Configure user permissions in Administration » People » Permissions:

   - Use the administration pages and help (System module)

     The top-level administration categories require this permission to be
     accessible. The administration menu will be empty unless this permission
     is granted.

   - Access administration menu

     Users in roles with the "Access administration menu" permission will see
     the administration menu at the top of each page.

   - Display Drupal links

     Users in roles with the "Display drupal links" permission will receive
     links to drupal.org issue queues for all enabled contributed modules. The
     issue queue links appear under the administration menu icon.

 * Customize the menu settings in Administration » Configuration and modules »
   Administration » Administration menu.

 * To prevent administrative menu items from appearing twice, you may hide the
   "Management" menu block.
 
 
==TROUBLESHOOTING==
-------------------
 * If the menu does not display, check the following:

   - Are the "Access administration menu" and "Use the administration pages
     and help" permissions enabled for the appropriate roles?

   - Does html.tpl.php of your theme output the $page_bottom variable?

FAQ
---

Q: I enabled "Aggregate and compress CSS files", but admin_menu.css is still
   there. Is this normal?

A: Yes, this is the intended behavior. the administration menu module only loads
   its stylesheet as needed (i.e., on page requests by logged-on, administrative
   users).
 
 
 
 
 
 