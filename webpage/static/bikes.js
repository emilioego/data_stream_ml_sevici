// Function to create a map (called when page loads)
function initialize() {
    // Define properties of the map
    var mapOptions = {
        center:new google.maps.LatLng(37.3750091,-5.9979764),
        zoom:13,
        mapTypeId:google.maps.MapTypeId.ROADMAP,
        scrollwheel:false
    };

    // Choose where in the page to display the map
    var map=new google.maps.Map(document.getElementById("googleMap"),mapOptions);

    // Information for API call
    var NAME="seville";
    var APIKEY="2513ba8c201960d6193114b29d9be3e78dfce408";
    var url="https://api.jcdecaux.com/vls/v1/stations?contract=" + NAME + "&apiKey=" + APIKEY;
	

    // During initialization gather JSON data with station coordinates and add markers/circles
    var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange=function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                // Parse the JSON response
                data = JSON.parse(xmlhttp.responseText);

                // Style the circle/infowindow for each station
                for (i=0;i<101;i++) {
                    // Georges Quay station has closed, so do not gather data for station 16
                    if (data[i].number==16) {continue;}
                    var color;
                    // Set color based on the percentage of bike spaces available 
                    if (data[i].available_bikes/data[i].bike_stands == 0.00) {
                        color = 'black';
                    } else if (data[i].available_bikes/data[i].bike_stands < 0.25) {
                        color = 'red';
                    } else if (data[i].available_bikes/data[i].bike_stands > 0.75) {
                        color = 'green';
                    } else {
                        color = 'orange';
                    };
                     
                    // Properties for map circles
                    circle = new google.maps.Circle({
                        strokeColor: color,
                        strokeOpacity: '0.8',
                        strokeWeight: 0,
                        fillColor: color,
                        fillOpacity: 0.55,
                        map: map,
                        radius: 150,
                        clickable:true,
                        center: {lat: data[i].position.lat, lng: data[i].position.lng},
                    });

                    // Create information to display in infoWindow
                    // Infowindow contents created as a string including HTML tags for formatting
                    // Add a link that takes the user to that location on the Google Maps main page
                    var displayInfo = "<h3 style=\"margin:2px;\">" + data[i].address + "</h3><span style=\"text-align:center;font-size:20px;color:navy;\">Bikes Available: " + data[i].available_bikes + "</br>Bike Stands Free: " + data[i].available_bike_stands+"</span></br></br><a style=\"font-size:16px;text-align:center;\" href=\"http://maps.google.com/maps?q="+data[i].position.lat+","+data[i].position.lng+"\" target=\"_blank\">View full map in new tab</a></span>";


                    // Generate infoWindow
                    makeClickable(map, circle, displayInfo);
                    
                    // OPTIONAL
                    /*
                    --------INSERT MARKERS RATHER THAN CIRCLES-------

                       new google.maps.Marker({
                           position: {lat: data[i].position.lat, lng: data[i].position.lng},
                           map:map,
                           title:data[i].address
                       });
                   */

                } 
            }
        }
        xmlhttp.open("GET", url, true);
        xmlhttp.send();
}

// Create a clickable circle
 function makeClickable(map, circle, info) {
     var infowindow = new google.maps.InfoWindow({
         content: info
     });
 
     // Display information on click
     google.maps.event.addListener(circle, 'click', function(ev) {
         infowindow.setPosition(circle.getCenter());
         infowindow.open(map);
     });
 }

/////////////////////////////////////////////////////////////////////
/////////////      HISTORICAL DATA AND GRAPHS      //////////////////
/////////////////////////////////////////////////////////////////////

// Define global variables to be used in graph generation
var weekly_json_data;
var daily_json_data;

// Runs when "Go!" button is clicked
// Sends a request to '/weekly/...' that triggers a flask function.
// Function queries the database based on selected station, and returns averages as JSON
function toggleInfo() {
	document.getElementById("tabla").style.display="none";
	document.getElementById("boton_tabla").style.display="none";
    document.getElementById("station_title").innerHTML = document.getElementById("stations").options[document.getElementById("stations").selectedIndex].text;
    document.getElementById("more_info").style.display="block";

    var path = '/weekly/'+document.getElementById("stations").value;
    var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange=function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                // Parse the JSON response
                weekly_json_data = JSON.parse(xmlhttp.responseText);
                // Draw the graph
                drawStuff();
            }
        }
        xmlhttp.open("GET", path, true);
        xmlhttp.send();
}

///////////////////////////////////////////////////////////////////////

function drawStuff() {

    var arr = [['Day', 'Available Bikes']];
    for (let i = 0; i < weekly_json_data.length; i++) {
        var arr2 = [weekly_json_data[i][0],weekly_json_data[i][1]];
        arr.push(arr2);
      }
    // Create a new Google Chart
    var data = new google.visualization.arrayToDataTable(arr);

    // Set display options for the chart
        var options = {
            title: 'Average Daily Availability',
            width: 450,
            height:400,
            legend: { position: 'none' },
            chart: { title: 'Average Daily Availability'},
            bars: 'vertical', //or 'horizontal'
            axes: {
                y: {
                    0: { side: 'left', label: 'Average Number of Bikes Available'} // Top x-axis.
                }
            }
        }

        // Select the HTML div element to display the chart in, and draw it
        var chart = new google.charts.Bar(document.getElementById('chart_daily'));
        chart.draw(data, options);
}

///////////////////////////////////////////////////////////////////////

function drawChart(x) {
    // Take in a day as the argument, and pass that to the url to activate the appropriate
    // database query via flask

    var path = '/daily/'+document.getElementById("stations").value+'/'+x;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            // Parse the JSON response
            daily_json_data = JSON.parse(xmlhttp.responseText);

            // Format data for Google Chart
            // In each array element, the first value is the x value (time)
            // The second value is the y value (average bikes available during any given hour)
            var arr = [['Time of Day (Hourly)', 'Available Bikes']];
            for (let i = 0; i < daily_json_data.length; i++) {
                var arr2 = [daily_json_data[i][1],daily_json_data[i][0]];
                arr.push(arr2);
              }
            var DATA = google.visualization.arrayToDataTable(arr);

            // Display options for the chart
            var OPTIONS = {
                chart: {title:x+': '+'Hourly Availability'},
                width:450,
                height:400,
                legend: { position: 'none' },
                axes: {
                    y: {
                        0: { side: 'left', label: 'Average Number of Bikes Available'} // Top x-axis.
                    }
                }
            };
            // Select the HTML div element to display the chart, and draw the chart
            var CHART = new google.charts.Bar(document.getElementById('columnchart_material'));
            CHART.draw(DATA, OPTIONS);
        }
    }
    // Run the above function using the specified URL
    xmlhttp.open("GET", path, true);
    xmlhttp.send();
}
