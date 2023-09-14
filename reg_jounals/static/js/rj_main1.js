$(document).ready(function () {GetRecordsHomeScreen()})
today = new Date()

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

if (days) {
  date_to = Date.parse(date_from_new).addDays(parseInt(days, 10) - 1)}
else {
    date_to = Date.parse(date_from_new).addDays(parseInt(days2, 10))
}


date_to = date_to.toString('yyyy-MM-dd')

date_from = date_from.split('-')[2] + '.' + date_from.split('-')[1] + '.' + date_from.split('-')[0]
date_to = date_to.split('-')[2] + '.' + date_to.split('-')[1] + '.' + date_to.split('-')[0]

day_from = date_from.split('.')[0]
month_from = date_from.split('.')[1]
year_from = date_from.split('.')[2]

day_to = date_to.split('.')[0]
month_to = date_to.split('.')[1]
year_to = date_to.split('.')[2]


if (day_from[0] == 0) {
  day_from = parseInt(day_from[1], 10)
}

if (month_from[0] == 0) {
  month_from = parseInt(month_from[1], 10)
}


if (day_to[0] == 0) {
  day_to = parseInt(day_to[1], 10)
}

if (month_to[0] == 0) {
  month_to = parseInt(month_to[1], 10)
}

day_from = parseInt(day_from, 10)
month_from = parseInt(month_from, 10)
day_to = parseInt(day_to, 10)
month_to = parseInt(month_to, 10)








  $.getJSON('/work_cal/' + year_to ,  (data) => {
    calendar = []
    for (var i = 0; i < data.length; i++) {
      calendar.push({
        'month':data[i].month,
        'days':data[i].days
      })
    }
    console.log(calendar);




total_celebrate = 0

for (var rec of calendar) {
  if (month_from == rec.month) {
    days = rec.days.split(',')
    for (var day of days) {
      if (day_from <= day) {
          total_celebrate = total_celebrate + 1
      }
    }
  }
}

if (month_from != month_to) {
for (var i = parseInt(month_from, 10)+1; i <= month_to; i++) {
  for (var rec of calendar) {

    if (i == rec.month && i != month_to) {
      days = rec.days.split(',')
      total_celebrate = total_celebrate + days.length
    }

    else if (i == rec.month && i == month_to) {
      console.log('wtf');
       days = rec.days.split(',')
       for (var day of days) {
         if (day <= day_to) {
           total_celebrate = total_celebrate + 1
         }
       }
    }


    }
  }
  date_to = Date.parse(date_to).addDays(parseInt(total_celebrate, 10)+1);
}
else {
  date_to = Date.parse(date_to).addDays(parseInt(total_celebrate, 10));
}


  if (month_to < month_from) {
  for (var i = 1; i <= month_to; i++) {
    for (var rec of calendar) {

      if (i == rec.month && i != month_to) {
        days = rec.days.split(',')
        total_celebrate = total_celebrate + days.length
      }
      else if (i == rec.month && i == month_to) {
        console.log('wtf');
         days = rec.days.split(',')
         for (var day of days) {
           if (day <= day_to) {
             total_celebrate = total_celebrate + 1
           }
         }
      }

  }
}
date_to = Date.parse(date_to).addDays(parseInt(total_celebrate, 10));
}










$('#id_dur_to').val(date_to.toString('yyyy-MM-dd'))
  })
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

// Запись на прием

function CheckInForInvite() {
      cookies = document.cookie.split(';')
      console.log(cookies);
      for (const c of cookies) {
        if (c.split('=')[0] == 'csrftoken') {
          csrf = c.split('=')[1]
        }
      }
      // Определяем функцию которая принимает в качестве параметров url и данные которые необходимо обработать:
      const postData = async (url = '', data = {}) => {
      // Формируем запрос
      const response = await fetch(url, {
      // Метод, если не указывать, будет использоваться GET
      method: 'POST',
      // Заголовок запроса
      headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrf,

      },
      // Данные
      body: JSON.stringify(data)
      });
      return response.json(); 
}




checkdatetime = $('#checkinDate').val()
citizen = $('#citizen').val()

postData('/invite_checkin/new', {'checkinDate': checkdatetime, 'citizen': citizen })
 
  .then((data) => {
    alert(data); 
  });

  setTimeout(GetRecords(5), 1000);

}

function GetRecords(count) {

  $('#invite-records-table tbody').remove()
  $('#checkin').css('display','block')
  $('#invite-records-table').append('<tbody>')
  $.getJSON('/invite_checkin/' + count,  (data) => {
   
    for (let i = 0; i < data.length; i++) {
     
      new_date = Date.parse(data[i].checkinDate)
      style = ''
      
      if (data[i].cancelled == true) {
        style = 'text-decoration: line-through;'
      }

      if (new_date.toString("dd.MM.yy") == today.toString("dd.MM.yy")) {
        style = 'background: lightgreen;'

      }
      
      console.log(new_date.toString("dd.MM.yy") + " " + today.toString("dd.MM.yy") );

      $('#invite-records-table').append('<tr style="'+ style +'" id="' + data[i].id + '"><td>' + new_date.toString("dd.MM.yy HH:mm") + '</td><td>' + data[i].citizen + '</td><td onclick="SetRecordCancelled('+ data[i].id +')">Отменить</td></tr>')
   
    }

  })
  $('#invite-records-table').append('</tbody>')  

  GetRecordsHomeScreen()

}

function GetRecordsHomeScreen() {
  $('#checkins table tbody').remove()
  $('#checkins table').append('<tbody>')

  $.getJSON('/invite_checkin/15',  (data) => {

    
   
    for (let i = 0; i < data.length; i++) {
      
      new_date = Date.parse(data[i].checkinDate)
      style = ''
      
      if (data[i].cancelled == true) {
        style = 'text-decoration: line-through;'
      }

      if (new_date.toString("dd.MM.yy") == today.toString("dd.MM.yy")) {
        style = 'background: lightgreen;'
        console.log('1');
      }

      
      $('#checkins table tbody').append('<tr style="'+ style +'" id="' + data[i].id + '"><td>' + new_date.toString('dd.MM.yy HH:mm') + '</td><td>' + data[i].citizen + '</td></tr>')
   
    }

  })
  $('#checkins table').append('</tbody>')  
}

function SetRecordCancelled(recid) {
  cookies = document.cookie.split(';')
      console.log(cookies);
      for (const c of cookies) {
        if (c.split('=')[0] == 'csrftoken') {
          csrf = c.split('=')[1]
        }
      }
      // Определяем функцию которая принимает в качестве параметров url и данные которые необходимо обработать:
      const postData = async (url = '', data = {}) => {
      // Формируем запрос
      const response = await fetch(url, {
      // Метод, если не указывать, будет использоваться GET
      method: 'GET',
      // Заголовок запроса
      headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrf,

      }});
      // Данные
      // body: JSON.stringify(data)
      // });
       return response.json(); 
    }
      postData('/invite_checkin/cancel/' + recid, {})
 
    .then((data) => {
      alert(data); 
    });

    setTimeout(GetRecords(5), 1000);

}