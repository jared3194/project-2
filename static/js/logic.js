var count = ('country_count.csv')
d3.csv(count, function(data) {
  createFeatures(data.features);
});
function createFeatures(countryData) {
  var arrival = (countryData, {
    onEachFeature: function(feature,layer){
      layer.bindPopup("<h1>Airport: "+ feature.Arrive + 
      "<h1>Number of Flights:  " + feature.Count )
  }})}
  createMap(arrival);
function createMap(arrival) {
  var lightmap =L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY,
  });

  var layers = {
    ATL: new L.LayerGroup(),
    LAX: new L.LayerGroup(),
    BOTH: new L.LayerGroup(),
  };
  
  var overlays = {
    "Atlanta": layers.ATL,
    "Los Angeles": layers.LAX,
    "Both": layers.BOTH,

  };
  var myMap = L.map("map", {
    center: [40.7, -94.5],
    zoom: 5,
    layers: [
      layers.ATL,
      layers.LAX,
      layers.BOTH,
    ]
  });
lightmap.addTo(map);

// Creating map object
var myMap = L.map("map", {
  center: [40.7, -94.5],
  zoom: 5,
  layers: [
    layers.ATL,
    layers.LAX,
    layers.BOTH,

  ]

});
L.control.layers(null, overlays).addTo(myMap);

var legend = L.control({
  position: "bottomright"
});
function getColorGrades(Airport) {
  if (Airport = "LAX") {
      return 'blue'
  } else if (Airport = "ATL") {
      return 'red'
  } else if (Airport = "BOTH") {
      return 'purple'
  }
};

legend.onAdd = function(myMap) {
  var div = L.DomUtil.create("div", "info legend"),
  Airport = ["LAX", "ATL", "BOTH"]
  div.innerHTML += "<h3 style='text-align: center'>Airport</h3>"

for (var i = 0; i <Airport.length; i++) {
  div.innerHTML +=
  '<i style="background:' + getColorGrades(Airport[i] + 1) + '"></i> ' +
  Airport[i] + (Airport[i + 1] ? '&ndash;' + Airport[i + 1] + '<br>' : '+');
}
    return div;
}
  legend.addTo(myMap);
}
// // Adding tile layer
// L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
//   attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
//   tileSize: 512,
//   maxZoom: 18,
//   zoomOffset: -1,
//   id: "mapbox/streets-v11",
//   accessToken: API_KEY
// }).addTo(myMap);

// var layers = {
//   ATL: new L.LayerGroup(),
//   LAX: new L.LayerGroup(),
//   BOTH: new L.LayerGroup(),
// };

// var overlays = {
//   "Atlanta": layers.ATL,
//   "Los Angeles": layers.LAX,
//   "Both": layers.BOTH,
// };
// L.control.layers(null, overlays).addTo(myMap);

// var icons = {
//   ATL: L.ExtraMarkers.icon({
//     icon: "ion-android-airplane",
//     iconColor: "white",
//     markerColor: "red",
//     shape: "star"
//   }),
//   LAX: L.ExtraMarkers.icon({
//     icon: "ion-android-airplane",
//     iconColor: "white",
//     markerColor: "blue",
//     shape: "circle"
//   }),
//   BOTH: L.ExtraMarkers.icon({
//     icon: "ion-android-airplane",
//     iconColor: "white",
//     markerColor: "purple",
//     shape: "penta"
//   })
// };
// var count = ('country_count.csv')

// d3.csv(count).then(function(data) {
//   for (var i = 0; i < data.length; i++) {
//     Markers = []
//     // console.log(data[i].Count);
//     // console.log(data[i].Country);
//     Markers.push(
//       L.marker(data[i].Lat, data[i].Long).bindPopup("<h1>Airport: "+ data.Arrive + 
//     "<h1>Number of Flights:  " + data.Count )
//   })
// var Layer = L.layerGroup(Markers)
// });








// // // console.log(link)
// var country = d3.csv("unique_countries.csv").then(data => {
//   console.log(data)
// })
// function chooseColor(countries) {
//   switch (countries) {
//     case 'Los Angeles International':
//       return "blue";
//     case 'Hartsfield-jackson Atlanta International':
//       return "red";
//     default:
//       return "black";
//   }
// }

// // // // Grabbing our GeoJSON data..
// var csv = d3.csv('international_clean.csv').then(data => {
//   console.log(data)
// });
// //
// var borders = "static/js/countries.geojson"
// var csv = 'international_clean.csv'

// function filterForISO(feature) {
//   for (var i = 0, len = csv.length; i < len; i++) {
//     if (csv[i]["ISO3"] == feature.properties["ISO3"]) return true;
//   };
//   var border_polygons = L.geoJSON(borders, { filter: filterForISO }).addTo(map);

// // })});
// }
