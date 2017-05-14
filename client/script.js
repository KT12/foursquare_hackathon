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


  $('#find').click(function(){

    mapObj.addMarker({
      lat: 40.724450,
      lng: -73.978638,
      title: "Kafana",
      infoWindow: {
          content: '<h4>Pop Pub</h4>',
          maxWidth: 100
        }
    })

    mapObj.addMarker({
      lat: 40.724950,
      lng: -73.981333,
      title: "Gruppo",
      infoWindow: {
          content: '<h4>Gruppo</h4>',
          maxWidth: 100
        }
    })

    mapObj.addMarker({
      lat: 40.728626,
      lng: -73.980320,
      title: "Ciao For Now",
      infoWindow: {
          content: '<h4>Ciao For Now</h4>',
          maxWidth: 100
        }
    })


    mapObj.addMarker({
      lat: 40.727518,
      lng: -73.979478,
      title: "Eleven B",
      infoWindow: {
          content: '<h4>Eleven B</h4>',
          maxWidth: 100
        }
    })

    mapObj.addMarker({
      lat: 40.725237,
      lng: -73.981347,
      title: "Housewarmings!",
      infoWindow: {
          content: '<h4>Housewarmings!</h4>',
          maxWidth: 100
        }
    })


  });

});