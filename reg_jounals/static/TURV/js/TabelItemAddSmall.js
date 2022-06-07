// ВЫВОД ИНФОРМАЦИИ О СОТРУДНИКЕ



function emp_info(e_id) {
  $('#id_employer').css('display', 'none')

  emp_val = $('#t_emps option:selected').val().toString()

  $('#id_employer option').filter(function() {
      return ($(this).text().split(",")[4] == e_id); //To select Blue
  }).prop('selected', true);

  // $('#id_employer option').filter(function() {
  //     return ($(this).text().split(",")[4] == emp_val); //To select Blue
  // }).prop('selected', true);

  emp_select = $('#id_employer option:selected').text().split(",")
  emp_path = "window.open('/turv/employers/upd/" + e_id + "')"

  $('#fullname').text(emp_select[0])
  $('#fullname').attr('onclick', emp_path)
  $('#sex').text(emp_select[7])
  $('#position').text('Должность: ' + emp_select[1])
  $('#level').text('Разряд/категория ст.учета: ' + emp_select[2])
  $('#payment').text('Ступень оплаты: ' + emp_select[3])
  if (emp_select[5] == 'False') {
    $('#shift').html('<img src="/static/TURV/img/sun2.png">Дневной персонал')
    $('#n_time').text('')
    $('#n_time_span').css('display','none')
  }
  else {
    $('#shift').html('<img src="/static/TURV/img/shift.png">Сменный персонал')
    $('#n_time').text(emp_select[6])
      $('#n_time_span').css('display','block')
  }
}
// ------------------------------------------------------------------------
$(document).ready(function(){
$('#id_auto').addClass('chosen-select')
$('#id_auto').css('width', '300px')
$(".chosen-select").chosen()
var query = String(document.location.href).split('/');


emp_info()


// Отметка о том, что сотрудник добавлен в табель

intabels = $('.intabel').find('li')
indeps = $('.indep').find('tr')



for (var i = 0; i < indeps.length; i++) {
 for (var intabel of intabels) {
   if (indeps[i].id == intabel.id) {

     $('.indep').find('#' + intabel.id).css('background', 'lightgreen')
       if ($('#tabel-type').text() == 3 || $('#tabel-type').text() == 2) { }
       else{$('.indep').find('#' + intabel.id).prop('onclick', '')}

   }
 }
  }


month_  = $('#id_month').text()
year_ = $('#id_year').text()
let rMonth = 0

switch (month_) {
case '01':
  rMonth = 0
break;

case '02':
  rMonth = 1
break;

case '03':
  rMonth = 2
break;

case '04':
  rMonth = 3
break;

case '05':
  rMonth = 4
break;

case '06':
  rMonth = 5
break;

case '07':
  rMonth = 6
break;

case '08':
  rMonth = 7
break;

case '09':
  rMonth = 8
break;

case '10':
  rMonth = 9
break;

case '11':
  rMonth = 10
break;

case '12':
  rMonth = 11
break;
}


days_count = Date.getDaysInMonth(year_, rMonth)

switch (days_count) {
case 30:
$('#id_type_time31').css('visibility','hidden')

$('#id_hours31').css('visibility','hidden')

$('#day31').css('visibility','hidden')

break;
case 29:
$('#id_type_time30').css('visibility','hidden')
$('#id_hours30').css('visibility','hidden')
$('#day30').css('visibility','hidden')

$('#id_type_time31').css('visibility','hidden')
$('#id_hours31').css('visibility','hidden')
$('#day31').css('visibility','hidden')
break;

case 28:
$('#id_type_time29').css('visibility','hidden')
$('#id_hours29').css('visibility','hidden')
$('#day29').css('visibility','hidden')

$('#id_type_time30').css('visibility','hidden')
$('#id_hours30').css('visibility','hidden')
$('#day30').css('visibility','hidden')

$('#id_type_time31').css('visibility','hidden')
$('#id_hours31').css('visibility','hidden')
$('#day31').css('visibility','hidden')
break;
default:

}

let fDate = " "

for (var i = 1; i < (days_count+1); i++) {
fDate = (i.toString() + "." + month_.toString() + "." + year_)

pDate = Date.parse(fDate)

pDate = pDate.toString().split(" ")

if (pDate[0] == 'Sat' || pDate[0] == 'Sun') {
switch (pDate[2]) {
    case '01':



    $('#id_hours1').css('background','lightgreen')
    break;

    case '02':



    $('#id_hours2').css('background','lightgreen')
    break;

    case '03':



    $('#id_hours3').css('background','lightgreen')
    break;

    case '04':


    $('#id_hours4').css('background','lightgreen')
    break;

    case '05':



    $('#id_hours5').css('background','lightgreen')
    break;

    case '06':



    $('#id_hours6').css('background','lightgreen')
    break;

    case '07':



    $('#id_hours7').css('background','lightgreen')
    break;

    case '08':



    $('#id_hours8').css('background','lightgreen')
    break;

    case '09':

    $('#id_hours9').css('background','lightgreen')
    break;

    case '10':


    $('#id_hours10').css('background','lightgreen')
    break;

    case '10':


    $('#id_hours10').css('background','lightgreen')
    break;

    case '11':


    $('#id_hours11').css('background','lightgreen')
    break;

    case '12':


    $('#id_hours12').css('background','lightgreen')
    break;

    case '13':


    $('#id_hours13').css('background','lightgreen')
    break;

    case '14':


    $('#id_hours14').css('background','lightgreen')
    break;

    case '15':


    $('#id_hours15').css('background','lightgreen')
    break;

    case '16':


    $('#id_hours16').css('background','lightgreen')
    break;

    case '17':


    $('#id_hours17').css('background','lightgreen')
    break;

    case '18':


    $('#id_hours18').css('background','lightgreen')
    break;

    case '19':


    $('#id_hours19').css('background','lightgreen')
    break;

    case '20':

    $('#id_hours20').css('background','lightgreen')
    break;

    case '21':
    $('#id_hours21').css('background','lightgreen')
    break;

    case '22':

    $('#id_hours22').css('background','lightgreen')
    break;

    case '23':

    $('#id_hours23').css('background','lightgreen')
    break;

    case '24':


    $('#id_hours24').css('background','lightgreen')
    break;

    case '25':

    $('#id_hours25').css('background','lightgreen')
    break;

    case '26':

    $('#id_hours26').css('background','lightgreen')
    break;

    case '27':

    $('#id_hours27').css('background','lightgreen')
    break;

    case '28':

    $('#id_hours28').css('background','lightgreen')
    break;

    case '29':

    $('#id_hours29').css('background','lightgreen')
    break;

    case '30':


    $('#id_hours30').css('background','lightgreen')
    break;

    case '31':


    $('#id_hours31').css('background','lightgreen')
    break;

    default:

    }


}



}

});

function ReSelectEmp() {

emp_info()
  }

function auto_fill() {
  month_  = $('#id_month').text()
  year_ = $('#id_year').text()
  let rMonth = 0

  switch (month_) {
  case '01':
    rMonth = 0
  break;

  case '02':
    rMonth = 1
  break;

  case '03':
    rMonth = 2
  break;

  case '04':
    rMonth = 3
  break;

  case '05':
    rMonth = 4
  break;

  case '06':
    rMonth = 5
  break;

  case '07':
    rMonth = 6
  break;

  case '08':
    rMonth = 7
  break;

  case '09':
    rMonth = 8
  break;

  case '10':
    rMonth = 9
  break;

  case '11':
    rMonth = 10
  break;

  case '12':
    rMonth = 11
  break;
  }


  days_count = Date.getDaysInMonth(year_, rMonth)

  emp_select = $('#id_employer option:selected').text().split(",")
  codes = $('.dig_code')
  hours = $('.dig_hours')
  sex = $('#sex').text()
  shift = emp_select[5]
  console.log(shift);
  if (shift == 'False') {


  for (var i = 0; i < days_count; i++) {
    if (hours[i].style.background != 'lightgreen'){
      hours[i].value = '8'
    }

    if (sex == 'Ж' && codes[i+1].value == 'В' && codes[i].value != 'В' ) {

        hours[i].value = '4'
      }
    }



  }

else {
  alert('Для сотрудников, работающих в сменном режиме, автозаполнение недоступно!')
}
}
