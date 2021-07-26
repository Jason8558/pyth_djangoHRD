
$(document).ready(function(){


query = document.location.href.split('/')
if (query[5] == 'upd') {
dep_val = $('#id_department option:selected').text()

  $('#e_deps option').filter(function() {
      return ($(this).text() == dep_val);
  }).prop('selected', true);
}

if ($('#id_shift_personnel').prop('checked') == false) {
  $('#id_stand_worktime').css('background', 'lightgray')


  $('#id_stand_worktime').prop('readonly', true)}
else {
  $('#id_stand_worktime').css('background', 'white')


  $('#id_stand_worktime').prop('readonly', false)
}

$('#id_shift_personnel').change(function () {
  if ($('#id_stand_worktime').prop('readonly') == true ) {

  $('#id_stand_worktime').prop('readonly', false)
  $('#id_stand_worktime').css('background', 'white')
  }
  else {
    $('#id_stand_worktime').prop('readonly', true)
      $('#id_stand_worktime').css('background', 'lightgray')
  }

})

dep_val = $('#e_deps option:selected').text()

  $('#id_department option').filter(function() {
      return ($(this).text() == dep_val);
  }).prop('selected', true);

$('#id_department').css('display', 'none')

});

function ReSelectDep() {

  dep_val = $('#e_deps option:selected').text()

    $('#id_department option').filter(function() {
        return ($(this).text() == dep_val);
    }).prop('selected', true);

    console.log($('#id_department option:selected').text())
  }

function AreYouSure() {

$('#sure').css('display', 'block')
$('#btn_ays').css('display', 'none')
$('#ue_cancel').css('display', 'none')
}
