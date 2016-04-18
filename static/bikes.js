// Function to create a map
function initialize() {
    
    // Properties of the map
    var mapOptions = {
        center:new google.maps.LatLng(53.344007,-6.266802),
        zoom:13,
        mapTypeId:google.maps.MapTypeId.ROADMAP,
        scrollwheel:false
    };

    var map=new google.maps.Map(document.getElementById("googleMap"),mapOptions);

    var NAME="Dublin";
    var APIKEY="1c8d24323042b11c89877648adfe3c180f15fa3c";
    var url="https://api.jcdecaux.com/vls/v1/stations?contract=" + NAME + "&apiKey=" + APIKEY;

    // During initialization gather JSON data with station coordinates and add markers
    var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange=function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                // Parse the JSON response
                data = JSON.parse(xmlhttp.responseText);
                for (i=0;i<101;i++) {

                    var color;

                    if (data[i].available_bikes/data[i].bike_stands < 0.25) {
                        color = 'red';
                    } else if (data[i].available_bikes/data[i].bike_stands > 0.75) {
                        color = 'green';
                    } else {
                        color = 'orange';
                    };
                     
                    var circle = new google.maps.Circle({
                        strokeColor: color,
                        strokeOpacity: '0.8',
                        strokeWeight: 0,
                        fillColor: color,
                        fillOpacity: 0.55,
                        map: map,
                        radius: 150,
                        clickable:true,
                        center: {lat: data[i].position.lat, lng: data[i].position.lng}
                    });

                    // Create information to display in infoWindow
                    // Add a link that takes the user to that location on the Google Maps main page
                    var displayInfo = "<h3>" + data[i].address + "</h3><span style=\"font-size:18px;\">Bikes Available: " + data[i].available_bikes + "</br>Bike Stands Free: " + data[i].available_bike_stands+"</span></br><a style=\"font-size:14px;\" href=\"http://maps.google.com/maps?q="+data[i].position.lat+","+data[i].position.lng+"\" target=\"_blank\">View full map in new tab</a>";

                    makeClickable(map, circle, displayInfo);
                    
                 // INSERT MARKERS RATHER THAN CIRCLES
                 //    new google.maps.Marker({
                 //        position: {lat: data[i].position.lat, lng: data[i].position.lng},
                 //        map:map,
                 //        title:data[i].address
                 //    });
                }// 
            }
        }
        xmlhttp.open("GET", url, true);
        xmlhttp.send();
}

// ******* NOT NEEDED!!! Include callback for initialize function in the url, and map will load correctly ********
//
// On window load, initialize the Google Map
//google.maps.event.addDomListener(window, 'load', initialize);

// Create a clickable circle
function makeClickable(map, circle, info) {
    var infowindow = new google.maps.InfoWindow({
        content: info
    });

    // Display information on mouseover
    google.maps.event.addListener(circle, 'click', function(ev) {
        infowindow.setPosition(circle.getCenter());
        infowindow.open(map);
    });
}

// Toggle the display of the "more_info" div when the Go! button is clicked
function toggleInfo() {
    var name = document.getElementById("stations").value;
    window.location.href="/station/"+name;
}
