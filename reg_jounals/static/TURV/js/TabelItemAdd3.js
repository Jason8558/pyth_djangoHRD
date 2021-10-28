// ВЫВОД ИНФОРМАЦИИ О СОТРУДНИКЕ
function emp_info() {
  $('#id_employer').css('display', 'none')

  emp_val = $('#t_emps option:selected').val().toString()

  $('#id_employer option').filter(function() {
      return ($(this).text().split(",")[4] == emp_val); //To select Blue
  }).prop('selected', true);

  emp_select = $('#id_employer option:selected').text().split(",")

  $('#fullname').text(emp_select[0])
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
$(".chosen-select").chosen()
var query = String(document.location.href).split('/');
console.log($('#t_emps').find('option').text());

emp_info()


// Отметка о том, что сотрудник добавлен в табель

intabels = $('.intabel').find('li')
indeps = $('.indep').find('li')



for (var i = 0; i < indeps.length; i++) {
 for (var intabel of intabels) {
   if (indeps[i].id == intabel.id) {
     console.log(indeps[i].id + " yes");
     $('.indep').find('#' + intabel.id).css('background', 'lightgreen')
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
    $('#id_type_time1').val("В")
    $('#id_hours1').val("8")
    $('#id_type_time1').css('background','lightgreen')

    $('#id_hours1').css('background','lightgreen')
    break;

    case '02':
    $('#id_type_time2').val("В")
    $('#id_hours2').val("8")
    $('#id_type_time2').css('background','lightgreen')

    $('#id_hours2').css('background','lightgreen')
    break;

    case '03':
    $('#id_type_time3').val("В")
    $('#id_hours3').val("8")
    $('#id_type_time3').css('background','lightgreen')

    $('#id_hours3').css('background','lightgreen')
    break;

    case '04':
    $('#id_type_time4').val("В")
    $('#id_hours4').val("8")
    $('#id_type_time4').css('background','lightgreen')

    $('#id_hours4').css('background','lightgreen')
    break;

    case '05':
    $('#id_type_time5').val("В")
    $('#id_hours5').val("8")
    $('#id_type_time5').css('background','lightgreen')

    $('#id_hours5').css('background','lightgreen')
    break;

    case '06':
    $('#id_type_time6').val("В")
    $('#id_hours6').val("8")
    $('#id_type_time6').css('background','lightgreen')

    $('#id_hours6').css('background','lightgreen')
    break;

    case '07':
    $('#id_type_time7').val("В")
    $('#id_hours7').val("8")
    $('#id_type_time7').css('background','lightgreen')

    $('#id_hours7').css('background','lightgreen')
    break;

    case '08':
    $('#id_type_time8').val("В")
    $('#id_hours8').val("8")
    $('#id_type_time8').css('background','lightgreen')

    $('#id_hours8').css('background','lightgreen')
    break;

    case '09':
    $('#id_type_time9').val("В")
    $('#id_hours9').val("8")
    $('#id_type_time9').css('background','lightgreen')
    $('#id_hours9').css('background','lightgreen')
    break;

    case '10':
    $('#id_type_time10').val("В")
    $('#id_hours10').val("8")
    $('#id_type_time10').css('background','lightgreen')
    $('#id_hours10').css('background','lightgreen')
    break;

    case '10':
    $('#id_type_time10').val("В")
    $('#id_hours10').val("8")
    $('#id_type_time10').css('background','lightgreen')
    $('#id_hours10').css('background','lightgreen')
    break;

    case '11':
    $('#id_type_time11').val("В")
    $('#id_hours11').val("8")
    $('#id_type_time11').css('background','lightgreen')
    $('#id_hours11').css('background','lightgreen')
    break;

    case '12':
    $('#id_type_time12').val("В")
    $('#id_hours12').val("8")
    $('#id_type_time12').css('background','lightgreen')
    $('#id_hours12').css('background','lightgreen')
    break;

    case '13':
    $('#id_type_time13').val("В")
    $('#id_hours13').val("8")
    $('#id_type_time13').css('background','lightgreen')
    $('#id_hours13').css('background','lightgreen')
    break;

    case '14':
    $('#id_type_time14').val("В")
    $('#id_hours14').val("8")
    $('#id_type_time14').css('background','lightgreen')
    $('#id_hours14').css('background','lightgreen')
    break;

    case '15':
    $('#id_type_time15').val("В")
    $('#id_hours15').val("8")
    $('#id_type_time15').css('background','lightgreen')
    $('#id_hours15').css('background','lightgreen')
    break;

    case '16':
    $('#id_type_time16').val("В")
    $('#id_hours16').val("8")
    $('#id_type_time16').css('background','lightgreen')
    $('#id_hours16').css('background','lightgreen')
    break;

    case '17':
    $('#id_type_time17').val("В")
    $('#id_hours17').val("8")
    $('#id_type_time17').css('background','lightgreen')
    $('#id_hours17').css('background','lightgreen')
    break;

    case '18':
    $('#id_type_time18').val("В")
    $('#id_hours18').val("8")
    $('#id_type_time18').css('background','lightgreen')
    $('#id_hours18').css('background','lightgreen')
    break;

    case '19':
    $('#id_type_time19').val("В")
    $('#id_hours19').val("8")
    $('#id_type_time19').css('background','lightgreen')
    $('#id_hours19').css('background','lightgreen')
    break;

    case '20':
    $('#id_type_time20').val("В")
    $('#id_hours20').val("8")
    $('#id_type_time20').css('background','lightgreen')
    $('#id_hours20').css('background','lightgreen')
    break;

    case '21':
    $('#id_type_time21').val("В")
    $('#id_hours21').val("8")
    $('#id_type_time21').css('background','lightgreen')
    $('#id_hours21').css('background','lightgreen')
    break;

    case '22':
    $('#id_type_time22').val("В")
    $('#id_hours22').val("8")
    $('#id_type_time22').css('background','lightgreen')
    $('#id_hours22').css('background','lightgreen')
    break;

    case '23':
    $('#id_type_time23').val("В")
    $('#id_hours23').val("8")
    $('#id_type_time23').css('background','lightgreen')
    $('#id_hours23').css('background','lightgreen')
    break;

    case '24':
    $('#id_type_time24').val("В")
    $('#id_hours24').val("8")
    $('#id_type_time24').css('background','lightgreen')
    $('#id_hours24').css('background','lightgreen')
    break;

    case '25':
    $('#id_type_time25').val("В")
    $('#id_hours25').val("8")
    $('#id_type_time25').css('background','lightgreen')
    $('#id_hours25').css('background','lightgreen')
    break;

    case '26':
    $('#id_type_time26').val("В")
    $('#id_hours26').val("8")
    $('#id_type_time26').css('background','lightgreen')
    $('#id_hours26').css('background','lightgreen')
    break;

    case '27':
    $('#id_type_time27').val("В")
    $('#id_hours27').val("8")
    $('#id_type_time27').css('background','lightgreen')
    $('#id_hours27').css('background','lightgreen')
    break;

    case '28':
    $('#id_type_time28').val("В")
    $('#id_hours28').val("8")
    $('#id_type_time28').css('background','lightgreen')
    $('#id_hours28').css('background','lightgreen')
    break;

    case '29':
    $('#id_type_time29').val("В")
    $('#id_hours29').val("8")
    $('#id_type_time29').css('background','lightgreen')
    $('#id_hours29').css('background','lightgreen')
    break;

    case '30':
    $('#id_type_time30').val("В")
    $('#id_hours30').val("8")
    $('#id_type_time30').css('background','lightgreen')
    $('#id_hours30').css('background','lightgreen')
    break;

    case '31':
    $('#id_type_time31').val("В")
    $('#id_hours31').val("8")
    $('#id_type_time31').css('background','lightgreen')
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
