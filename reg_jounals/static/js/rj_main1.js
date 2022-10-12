$('#next_num').click(function() {
  alert('alert!')
})




function get_uname() {
  $.getJSON("/getusername/",  (data) => {
    return data
  })

}



// Рассчет дней отпуска -----------------------------------------------------------------------------------
function vac_calc() {

date_from = $('#id_dur_from').val()
date_from_new = date_from.split('-')[2] + '.' + date_from.split('-')[1] + '.' + date_from.split('-')[0]

date_to = $('#id_dur_to').val()
date_to_new = date_to.split('-')[2] + '.' + date_to.split('-')[1] + '.' + date_to.split('-')[0]

dcount = (( Date.parse(date_to_new) - Date.parse(date_from_new)) / 24 / 60 / 60 / 1000) + 1

$('#id_days_count').val(dcount)


$('#id_days_count2').val(dcount - 1)
// ======================================================================================================
}

// Рассчет даты конца отпуска -----------------------------------------------------------------------------
function duration() {
  date_from = $('#id_dur_from').val()
  date_from_new = date_from.split('-')[2] + '.' + date_from.split('-')[1] + '.' + date_from.split('-')[0]

  days = $('#id_days_count').val()

  days2 = $('#id_days_count2').val()
console.log(days2);
if (days) {
  date_to = Date.parse(date_from_new).addDays(parseInt(days, 10) - 1)}
else {
    date_to = Date.parse(date_from_new).addDays(parseInt(days2, 10))
}



  $('#id_dur_to').val(date_to.toString('yyyy-MM-dd'))


}
// --------------------------------------------------------------------------------------------------------

// Калькулятор дат ----------------------------------------------------------------------------------------
function open_vac_calc() {
  $('#calc-container').css('display','block')
}

function close_vac_calc() {
  $('#calc-container').css('display','none')
}

function select_calc_mode_subtr() {
  if ($('#subtr').css('display') == 'none') {
    $('#subtr').css('display', 'block')
    $('#dur').css('display','none')
  }
}

function select_calc_mode_dur() {
  if ($('#dur').css('display') == 'none') {
    $('#dur').css('display', 'block')
    $('#subtr').css('display','none')
  }
}
// =========================================================================================================

// Открытия диалога при удалении документа из журнала ------------------------------------------------------
function OpenSureDialog() {
  document.getElementById('sure_btn').style.display = "none";
  document.getElementById('sure').style.display = "block";
}
// =========================================================================================================


//Проверка больничного листа ------------------------------------------------
function check_SickDoc() {
      // query_url = 'sick_reg/checkdoc/' + $('#iframe').contents().find('#id_sd_number').val()
      query_url = '/sick_reg/checkdoc/' + $('#id_sd_number').val()
      $.getJSON(query_url,  (data) => {
        alert(data)
      })
}

//Электронные трудовые
function digital_histories() {

if ($('#id_eh_isdigital').prop('checked') == false) {
  $("#id_eh_number").val(" ")
}
else {
  $("#id_eh_number").val("Электронная")
}


}

//Сокращение имени

function sfio() {
fio = $('#id_op_emloyer').val().split(" ")
name = fio[1]
patronymic = fio[2]
new_fio = fio[0] + " " + name[0] + "." + patronymic[0] + "."
$('#short_fio').val(new_fio)
}

function all_off() {
  $('.to_tabel input, .to_tabel select').prop('disabled', true)


}

function all_on() {
  $('.to_tabel input, .to_tabel select').prop('disabled', false)

}

function closeAllFields() {
  $('#op_invite').css('display', 'none')
  $('#op_resign').css('display', 'none')
  $('#op_probation').css('display', 'none')
  $('#op_typeOfWork').css('display','none')
  $('#op_moveFrom').css('display','none')
  $('#op_moveTo').css('display','none')
}

function inviteOnWork() {
  $('#op_invite').css('display', '')
  $('#op_probation').css('display', '')
  $('#op_typeOfWork').css('display','')

}

function ResignFromWork() {
  $('#op_resign').css('display', '')

}

function MoveOnOtherWork() {
  $('#op_typeOfWork').css('display','')
  $('#op_moveFrom').css('display','')
  $('#tab_pos').prop('disabled', false)
}
