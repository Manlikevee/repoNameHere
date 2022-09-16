let autocomplete;
let placeSearch;
let componentForm = {
  street_number: 'short_name',
  route: 'long_name',
  locality: 'long_name',
  administrative_area_level_1: 'short_name',
  country: 'long_name',
  postal_code: 'short_name'
};

window.initPlaces = function() {
  if ( jQuery( '#autocomplete-address' ).length ) {
    autocomplete = new google.maps.places.Autocomplete(
      document.getElementById( 'autocomplete-address' ),
      { types: [ 'geocode' ] }
    );
    autocomplete.addListener( 'place_changed', fillInAddress );
  }
};

function fillInAddress() {

  // Get the place details from the autocomplete object.
  let place = autocomplete.getPlace();

  // Get each component of the address from the place details
  // and fill the corresponding field on the form.
  for ( let i = 0; i < place.address_components.length; i++ ) {
    let addressType = place.address_components[i].types[0];
    if ( componentForm[addressType]) {
      let val = place.address_components[i][componentForm[addressType]];
      document.getElementById( addressType ).value = val;
    }
  }
  let streetNum = jQuery( '#street_number' ).val();
  let streetName = jQuery( '#route' ).val();
  let city = jQuery( '#locality' ).val();
  let state = jQuery( '#administrative_area_level_1' ).val();
  let zip = jQuery( '#postal_code' ).val();
  jQuery( 'input[name="rep_address_1"]' ).val( streetNum + ' ' + streetName );
  jQuery( 'input[name="rep_city"]' ).val( city );
  jQuery( 'input[name="rep_state"]' ).val( state );
  jQuery( 'input[name="rep_zip"]' ).val( zip );
  jQuery( '#autocomplete-address' ).val( '' );
}

function geolocate() {
  if ( navigator.geolocation ) {
    navigator.geolocation.getCurrentPosition( function( position ) {
      var geolocation = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      var circle = new google.maps.Circle({
        center: geolocation,
        radius: position.coords.accuracy
      });
      autocomplete.setBounds( circle.getBounds() );
    });
  }
}

jQuery( '#autocomplete-address' ).on( 'focus', function() {
  geolocate();
});

jQuery( '#manual_address' ).on( 'change', function( e ) {
  var checked = e.target.checked;
  if ( true === checked ) {
    jQuery( 'input[name="rep_address_1"]' ).removeAttr( 'disabled' );
    jQuery( 'input[name="rep_address_2"]' ).removeAttr( 'disabled' );
    jQuery( 'input[name="rep_city"]' ).removeAttr( 'disabled' );
    jQuery( 'input[name="rep_state"]' ).removeAttr( 'disabled' );
    jQuery( 'input[name="rep_zip"]' ).removeAttr( 'disabled' );
  } else {
    jQuery( 'input[name="rep_address_1"]' ).attr( 'disabled', 'true' );
    jQuery( 'input[name="rep_address_2"]' ).attr( 'disabled', 'true' );
    jQuery( 'input[name="rep_city"]' ).attr( 'disabled', 'true' );
    jQuery( 'input[name="rep_state"]' ).attr( 'disabled', 'true' );
    jQuery( 'input[name="rep_zip"]' ).attr( 'disabled', 'true' );
  }
});