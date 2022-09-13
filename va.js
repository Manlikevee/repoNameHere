$(function() {
    $('.form_body').on('input', function() {
      var p = $('#p').val();
      var r = $('#r').val();
      var t = $('#t').val();
      var rMonthly = (r / 100) / 12;
      var pmt = p * rMonthly / (1 - Math.pow(1 / (1 + rMonthly), t));
      var totalCost = pmt * t;
      var totalInt = totalCost - p;
      $('#totalCosts').val(totalCost.toFixed(2));
      $('#totalInts').val(totalInt.toFixed(2));
      $('#pmts').val(pmt.toFixed(2));
    // $('#totalCost').text(totalCost.toFixed(2));
    // $('#totalInt').text(totalInt.toFixed(2));
    // $('#pmt').text(pmt.toFixed(2));
    });
  });
