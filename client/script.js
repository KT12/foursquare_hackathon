$(document).ready(function(){

  var mapObj = new GMaps({
    el: '#map',
    lat: 40.758896,
    lng: -73.985130,
    zoom: 13,
  });
  
  var latlng1;
  var latlng2;

  $('#loc1').keypress(function(e){
    if (e.which == 13) {
      var address = $('#loc1').val();
      GMaps.geocode({
        address: address,
        callback: function(results, status) {
          if (status == 'OK') {
            latlng1 = results[0].geometry.location;

            console.log( e.target.value + " " + latlng1.lat());
            console.log( e.target.value + " " + latlng1.lng());

            mapObj.addMarker({
              lat: latlng1.lat(),
              lng: latlng1.lng()
            })

            mapObj.setCenter(latlng1.lat(), latlng1.lng());
            mapObj.setZoom(13);
          } else if (status == 'ZERO_RESULTS') {
            alert('Sorry, no location named ' + address);
          }
        }
      });

    }
  });

  $('#loc2').keypress(function(e){
    if (e.which == 13) {
      var address = $('#loc2').val();
      GMaps.geocode({
        address: address,
        callback: function(results, status) {
          if (status == 'OK') {
            latlng2 = results[0].geometry.location;

            mapObj.addMarker({
              lat: latlng2.lat(),
              lng: latlng2.lng()
            })

            mapObj.setCenter(latlng2.lat(), latlng2.lng());
            mapObj.setZoom(13);
          } else if (status == 'ZERO_RESULTS') {
            alert('Sorry, no location named ' + address);
          }
        }
      });
    }
  });




});