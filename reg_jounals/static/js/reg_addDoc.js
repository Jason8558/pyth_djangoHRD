$(document).ready(function() {
  var query = String(document.location.href).split('/');
  var regnum = parseInt(query[5])
  document.getElementById('id_sd_reg_number').value = regnum})
