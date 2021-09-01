$(document).ready(function(){

// ВЫВОДИТ КОЛ-ВО ВЫХОДНЫХ ДНЕЙ В ЗАПОЛНЕНИИ(ОБНОВЛЕНИИ) СОТРУДНИКА

  weekends = $('#id_sHours24').val()/8
  $('#weekends').val(weekends)

// ----------------------------------------------------------------------------






// УБИРАЕТ ПУСТЫЕ ПОЛЯ ИТОГОВ ВРЕМНИ ИЗ ОКНА ЗАПОЛНЕНИЯ(ОБНОВЛЕНИЯ) СОТРУДНИКА

sum_fields = $('.summary_times').children('.st')
for (var i = 0; i < sum_fields.length; i++) {
  sum_puts = sum_fields[i].childNodes
  for (var j = 0; j < sum_puts.length; j++) {

    if (sum_puts[j].tagName == 'INPUT') {
      if (sum_puts[j].value == 0) {
        sum_fields[i].style.display = 'none'

      }
      else {
        sum_fields[i].style.display = 'block'

      }
    }
  }
}

// ----------------------------------------------------------------------------


// ПРЕОБРАЗОВЫВАЕТ ЦИФРУ МЕСЯЦА В ТЕКСТ

dig_monts = $('.field_month')

for (var i = 0; i < dig_monts.length; i++) {

  switch (dig_monts[i].innerText) {
    case '01':
      dig_monts[i].textContent = 'Январь'
    break;

    case '02':
      dig_monts[i].textContent = 'Февраль'
    break;

    case '03':
      dig_monts[i].textContent = 'Март'
    break;

    case '04':
      dig_monts[i].textContent = 'Апрель'
    break;

    case '05':
      dig_monts[i].textContent = 'Май'
    break;

    case '06':
      dig_monts[i].textContent = 'Июнь'
    break;

    case '07':
      dig_monts[i].textContent = 'Июль'
    break;

    case '08':
      dig_monts[i].textContent = 'Август'
    break;

    case '09':
      dig_monts[i].textContent = 'Сентябрь'
    break;

    case '10':
      dig_monts[i].textContent = 'Октябрь'
    break;

    case '11':
      dig_monts[i].textContent = 'Ноябрь'
    break;

    case '12':
      dig_monts[i].textContent = 'Декабрь'
    break;
}

}

// ----------------------------------------------------------------------------


//ВЫВОДИТ СПИСОК ТОЛЬКО ДОСТУПНЫХ В НАСТОЯЩИЙ МОМЕНТ(ДЛЯ ТЕКУЩЕГО ПОЛЬЗОВАТЕЛЯ) ПОДРАЗДЕЛЕНИЙ (ПРИ ОТКРЫТИИ)

    dep = $('#t_dep option:selected').val()

    $("#id_department option").filter(function() {return this.text == dep;}).prop('selected', true);

// ----------------------------------------------------------------------------


// ПРЕДОТВРАЩАЕТ ЗАМЕНУ МЕСЯЦА ПРИ ВЫВОДЕ СПИСКА СОТРУДНИКОВ ТАБЕЛЯ

    var query = String(document.location.href).split('/');
    if (query[4] != 'create') {
      $('#id_month').val($('#t_month option:selected').val())
    }

// ----------------------------------------------------------------------------




//открыть сотрудника для обновления


// emp_ = $('#id_employer option:selected').text()
//
// emp_s = emp_.split(',')
//
//
// $('#fullname').text(emp_s[0])
// $('#position').text('Должность: ' + emp_s[1])
// $('#payment').text('Ступень оплаты: ' + emp_s[3])
// $('#id_positionOfPayment').val(emp_s[3])
// $('#level').text('Разряд: ' + emp_s[2])
//
//
// // $('#id_employer').css('display','none')
// $("#id_employer option").filter(function() {return this.text.split(',')[4] == emp_s[4];}).prop('selected', true);



});

// УСТАНОВКА МЕСЯЦА ПРИ СОЗДАНИИ НОВОГО ТАБЕЛЯ

function SetMonth() {
  $('#id_month').val($('#t_month option:selected').val())

}

// ----------------------------------------------------------------------------


// УСТАНОВКА ДОСТУПНОГО ПОДРАЗДЕЛЕНИЯ ПРИ СОЗДАНИИ ТАБЕЛЯ (ВО ВРЕМЯ ВЫБОРА)

function ReSelectDep() {

  dep = $('#t_dep option:selected').val()
  $("#id_department option").filter(function() {return this.text == dep;}).prop('selected', true);
}

// ----------------------------------------------------------------------------

// function ReSelectEmp() {
// emp_ = $('#t_emps option:selected').text()
//
// emp_s = emp_.split(',')
//
// // for (var i = 0; i < emp_s.length; i++) {
// //   console.log(emp_s[i] + ' ' + i)
// // }
// $('#fullname').text(emp_s[0])
// $('#position').text('Должность: ' + emp_s[1])
// $('#payment').text('Ступень оплаты: ' + emp_s[3])
// $('#id_positionOfPayment').val(emp_s[3])
// $('#id_level').val(emp_s[2])
// if (emp_s[2] != " ") {
//   $('#level').text('Разряд: ' + emp_s[2])
// } else {
// $('#level').text('')
// }
//
// console.log("---НАЧАЛО ОТЛАДКИ---")
// console.log("должность в выборе " + emp_s[1] )
//
//
//
//   $("#id_position option").filter(function() {return this.text = emp_s[1];}).prop('selected', true);
//   $("#id_employer option").filter(function() {return this.text.split(',')[4] == emp_s[4];}).prop('selected', true);
// }

function Tabel() {


// ВЫДАЕТ ОШИБКУ, ЕСЛИ ВМЕСТО 8 "В"
checkfields = $('.dig_hours')
errors = 0
for (var field of checkfields) {
  if (field.value == 'В' || field.value == 'в') {
    field.style.background = 'red'
    errors = 1
  }
  else if (field.style.background == 'red') {

      field.style.background = 'white'
      errors = 0
    }
  }
  if (errors == 1) {
    $('.errors').text("Ошибка заполнения! Проверьте поля, выделенные красным.")
  $('.errors').css('display','block')
  $('.errors').css('position','absolute')
  $('.tItem_submit').prop('type','button')
}

  else {
      $('.errors').text("")
      $('.errors').css('display','none')
      $('.tItem_submit').prop('type','submit')


    }




// Виды аремени и кол-во часов
  tt1 = $('#id_type_time1').val().toUpperCase()
  $('#id_type_time1').val(tt1)
  h1 = $('#id_hours1').val()

  tt2 = $('#id_type_time2').val().toUpperCase()
  $('#id_type_time2').val(tt2)
  h2 = $('#id_hours2').val()

  tt3 = $('#id_type_time3').val().toUpperCase()
  $('#id_type_time3').val(tt3)
  h3 = $('#id_hours3').val()

  tt4 = $('#id_type_time4').val().toUpperCase()
  $('#id_type_time4').val(tt4)
  h4 = $('#id_hours4').val()

  tt5 = $('#id_type_time5').val().toUpperCase()
  $('#id_type_time5').val(tt5)
  h5 = $('#id_hours5').val()

  tt6 = $('#id_type_time6').val().toUpperCase()
  $('#id_type_time6').val(tt6)
  h6 = $('#id_hours6').val()

  tt7 = $('#id_type_time7').val().toUpperCase()
  $('#id_type_time7').val(tt7)
  h7 = $('#id_hours7').val()

  tt8 = $('#id_type_time8').val().toUpperCase()
  $('#id_type_time8').val(tt8)
  h8 = $('#id_hours8').val()

  tt9 = $('#id_type_time9').val().toUpperCase()
  $('#id_type_time9').val(tt9)
  h9 = $('#id_hours9').val()

  tt10 = $('#id_type_time10').val().toUpperCase()
  $('#id_type_time10').val(tt10)
  h10 = $('#id_hours10').val()

  tt11 = $('#id_type_time11').val().toUpperCase()
  $('#id_type_time11').val(tt11)
  h11 = $('#id_hours11').val()

  tt12 = $('#id_type_time12').val().toUpperCase()
  $('#id_type_time12').val(tt12)
  h12 = $('#id_hours12').val()

  tt13 = $('#id_type_time13').val().toUpperCase()
  $('#id_type_time13').val(tt13)
  h13 = $('#id_hours13').val()

  tt14 = $('#id_type_time14').val().toUpperCase()
  $('#id_type_time14').val(tt14)
  h14 = $('#id_hours14').val()

  tt15 = $('#id_type_time15').val().toUpperCase()
  $('#id_type_time15').val(tt15)
  h15 = $('#id_hours15').val()

  tt16 = $('#id_type_time16').val().toUpperCase()
  $('#id_type_time16').val(tt16)
  h16 = $('#id_hours16').val()

  tt17 = $('#id_type_time17').val().toUpperCase()
  $('#id_type_time17').val(tt17)
  h17 = $('#id_hours17').val()

  tt18 = $('#id_type_time18').val().toUpperCase()
  $('#id_type_time18').val(tt18)
  h18 = $('#id_hours18').val()

  tt19 = $('#id_type_time19').val().toUpperCase()
  $('#id_type_time19').val(tt19)
  h19 = $('#id_hours19').val()

  tt20 = $('#id_type_time20').val().toUpperCase()
  $('#id_type_time20').val(tt20)
  h20 = $('#id_hours20').val()

  tt21 = $('#id_type_time21').val().toUpperCase()
  $('#id_type_time21').val(tt21)
  h21 = $('#id_hours21').val()

  tt22 = $('#id_type_time22').val().toUpperCase()
  $('#id_type_time22').val(tt22)
  h22 = $('#id_hours22').val()

  tt23 = $('#id_type_time23').val().toUpperCase()
  $('#id_type_time23').val(tt23)
  h23 = $('#id_hours23').val()

  tt24 = $('#id_type_time24').val().toUpperCase()
  $('#id_type_time24').val(tt24)
  h24 = $('#id_hours24').val()

  tt25 = $('#id_type_time25').val().toUpperCase()
  $('#id_type_time25').val(tt25)
  h25 = $('#id_hours25').val()

  tt26 = $('#id_type_time26').val().toUpperCase()
  $('#id_type_time26').val(tt26)
  h26 = $('#id_hours26').val()

  tt27 = $('#id_type_time27').val().toUpperCase()
  $('#id_type_time27').val(tt27)
  h27 = $('#id_hours27').val()

  tt28 = $('#id_type_time28').val().toUpperCase()
  $('#id_type_time28').val(tt28)
  h28 = $('#id_hours28').val()

  tt29 = $('#id_type_time29').val().toUpperCase()
  $('#id_type_time29').val(tt29)
  h29 = $('#id_hours29').val()

  tt30 = $('#id_type_time30').val().toUpperCase()
  $('#id_type_time30').val(tt30)
  h30 = $('#id_hours30').val()

  tt31 = $('#id_type_time31').val().toUpperCase()
  $('#id_type_time31').val(tt31)
  h31 = $('#id_hours31').val()




//Суммирование часов
  let s1 = 0 //явки
  let s2 = 0 //ночные
  let s3 = 0 //РВ
  if ($('#manover').prop('checked') == false){
  let s4 = 0} //сверхурочка
  let s5 = 0 //Вахтовый метод
  let s6 = 0 //командировка
  let s7 = 0 //ПК
  let s8 = 0 //ПМ
  let s9 = 0 //ОТ
  let s10 = 0 //ОД
  let s11 = 0 //Учебный
  let s12 = 0 //УВ
  let s13 = 0 //УД
  let s14 = 0 //Роды
  let s15 = 0 //Декрет
  let s16 = 0 //ДО
  let s17 = 0 //Б
  let s18 = 0 //Неоплачиваемый больничный Т
  let s19 = 0 //ЛЧ
  let s20 = 0 //ПВ
  let s21 = 0 //Г
  let s22 = 0 //Прогулы
  let s23 = 0 //НС
  let s24 = 0 //выходные
  let s25 = 0 //ОВ
  let s26 = 0 //Доп вых неоплач.  НВ
  let s27 = 0 //Забастовка ЗБ
  let s28 = 0 //Неявки невыясненные НН
  let s29 = 0 //Простой по вине ра-ля РП
  let s30 = 0 //Простой не по вине ра-ля НП
  let s31 = 0 //Простой  по вине раб-ка ВП
  let s32 = 0 //НБ
  let s33 = 0 //Опл. отр. от р. НО
  let s34 = 0 //Нет ЗП НЗ
  let s36 = 0 //Местная командировка
  let s37 = 0 //ОЗ
  let s38 = 0 //НОД (нерабочие оплачиваемые дни)

//Суммирование дней
  let work = 0 //дни явок
  let vac = 0 //дни неявок
  let h_work = 0 //часы явок
  let h_vac = 0 //часы неявок


switch (tt1) {
  case 'Я':
    s1 += parseFloat(h1)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h1)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h1)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h1)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h1)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h1)
    vac += 1
  break;

  case 'ПК':
    s7 += parseFloat(h1)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h1)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h1)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h1)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h1)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h1)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h1)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h1)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h1)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h1)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h1)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h1)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h1)
    work += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h1)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h1)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h1)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h1)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h1)


  break;

  case 'ОВ':
    s25 += parseFloat(h1)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h1)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h1)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h1)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h1)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h1)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h1)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h1)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h1)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h1)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h1)
    vac += 1
  break;

  case 'НОД':
  if (h1.length > 2) {
    h_split = h1.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h1)
      work += 1
    }
    console.log(s19);
  break;

  case 'Я/ЛЧ':
    h1_ = h1.split('/')

    s1 += parseFloat(h1_[0])
    s19 += parseFloat(h1_[1])
    work += 1
  break;

  case 'Я/Н':
    h1_ = h1.split('/')

    s1 += parseFloat(h1_[0])
    s2 += parseFloat(h1_[1])
    work += 1
  break;

  case 'РВ/Н':
    h1_ = h1.split('/')

    s3 += parseFloat(h1_[0])
    s2 += parseFloat(h1_[1])
    work += 1
  break;
}

switch (tt2) {
  case 'Я':
    s1 += parseFloat(h2)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h2)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h2)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h2)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h2)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h2)
    vac += 1
  break;

  case 'ПК':
    s7 += parseFloat(h2)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h2)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h2)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h2)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h2)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h2)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h2)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h2)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h2)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h2)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h2)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h2)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h2)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h2)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h2)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h2)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h2)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h2)


  break;

  case 'ОВ':
    s25 += parseFloat(h2)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h2)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h2)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h2)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h2)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h2)
    vac += 1
  break;

  case 'ВП':
    s34 += parseFloat(h2)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h2)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h2)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h2)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h2)
    vac += 1
  break;

  case 'НОД':
  if (h2.length > 2) {
    h_split = h2.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h2)
      work += 1
    }
    console.log(s19);
  break;

  case 'Я/ЛЧ':
    h2_ = h2.split('/')
    s1 += parseFloat(h2_[0])
    s19 += parseFloat(h2_[1])
    work += 1
  break;

  case 'Я/Н':
    h2_ = h2.split('/')
    s1 += parseFloat(h2_[0])
    s2 += parseFloat(h2_[1])
    work += 1
  break;

  case 'РВ/Н':
    h2_ = h2.split('/')
    s3 += parseFloat(h2_[0])
    s2 += parseFloat(h2_[1])
    work += 1
  break;
}

switch (tt3) {
  case 'Я':
    s1 += parseFloat(h3)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h3)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h3)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h3)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h3)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h3)
    vac += 1
  break;

  case 'ПК':
    s7 += parseFloat(h3)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h3)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h3)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h3)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h3)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h3)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h3)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h3)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h3)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h3)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h3)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h3)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h3)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h3)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h3)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h3)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h3)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h3)


  break;

  case 'ОВ':
    s25 += parseFloat(h3)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h3)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h3)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h3)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h3)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h3)
    vac += 1
  break;

  case 'ВП':
    s34 += parseFloat(h3)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h3)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h3)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h3)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h3)
    vac += 1
  break;

  case 'НОД':
  if (h3.length > 2) {
    h_split = h3.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h3)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h3_ = h3.split('/')

    s1 += parseFloat(h3_[0])
    s19 += parseFloat(h3_[1])
    work += 1
  break;

  case 'Я/Н':
    h3_ = h3.split('/')

    s1 += parseFloat(h3_[0])
    s2 += parseFloat(h3_[1])
    work += 1
  break;

  case 'РВ/Н':
    h3_ = h3.split('/')

    s3 += parseFloat(h3_[0])
    s2 += parseFloat(h3_[1])
    work += 1
  break;
}

switch (tt4) {
  case 'Я':
    s1 += parseFloat(h4)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h4)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h4)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h4)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h4)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h4)
    vac += 1
  break;

  case 'ПК':
    s7 += parseFloat(h4)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h4)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h4)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h4)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h4)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h4)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h4)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h4)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h4)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h4)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h4)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h4)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h4)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h4)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h4)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h4)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h4)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h4)


  break;

  case 'ОВ':
    s25 += parseFloat(h4)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h4)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h4)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h4)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h4)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h4)
    vac += 1
  break;

  case 'ВП':
    s34 += parseFloat(h4)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h4)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h4)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h4)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h4)
    vac += 1
  break;

  case 'НОД':
  if (h4.length > 2) {
    h_split = h4.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h4)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h4_ = h4.split('/')

    s1 += parseFloat(h4_[0])
    s19 += parseFloat(h4_[1])
    work += 1
  break;

  case 'Я/Н':
    h4_ = h4.split('/')

    s1 += parseFloat(h4_[0])
    s2 += parseFloat(h4_[1])
    work += 1
  break;

  case 'РВ/Н':
    h4_ = h4.split('/')

    s3 += parseFloat(h4_[0])
    s2 += parseFloat(h4_[1])
    work += 1
  break;
}

switch (tt5) {
  case 'Я':
    s1 += parseFloat(h5)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h5)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h5)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h5)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h5)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h5)
    vac += 1
  break;

  case 'ПК':
    s7 += parseFloat(h5)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h5)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h5)
    vac += 1

  break;

  case 'ОД':
    s10 += parseFloat(h5)
    vac += 1

  break;

  case 'У':
    s11 += parseFloat(h5)
    vac += 1

  break;

  case 'УВ':
    s12 += parseFloat(h5)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h5)
    vac += 1

  break;

  case 'Р':
    s14 += parseFloat(h5)
    vac += 1

  break;

  case 'ОЖ':
    s15 += parseFloat(h5)
    vac += 1

  break;

  case 'ДО':
    s16 += parseFloat(h5)
    vac += 1

  break;

  case 'Б':
    s17 += parseFloat(h5)
    vac += 1

  break;

  case 'Т':
    s18 += parseFloat(h5)
    vac += 1

  break;

  case 'ЛЧ':
    s19 += parseFloat(h5)
    vac += 1

  break;

  case 'ПВ':
    s20 += parseFloat(h5)
    vac += 1

  break;

  case 'Г':
    s21 += parseFloat(h5)
    vac += 1

  break;

  case 'ПР':
    s22 += parseFloat(h5)
    vac += 1

  break;

  case 'НС':
    s23 += parseFloat(h5)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h5)


  break;

  case 'ОВ':
    s25 += parseFloat(h5)
    vac += 1

  break;

  case 'НВ':
    s26 += parseFloat(h5)
    vac += 1

  break;

  case 'ЗБ':
    s27 += parseFloat(h5)
    vac += 1

  break;

  case 'НН':
    s28 += parseFloat(h5)
    vac += 1

  break;

  case 'РП':
    s29 += parseFloat(h5)
    vac += 1

  break;

  case 'НП':
    s30 += parseFloat(h5)
    vac += 1

  break;

  case 'ВП':
    s34 += parseFloat(h5)
    vac += 1

  break;

  case 'НО':
    s33 += parseFloat(h5)
    vac += 1

  break;

  case 'НБ':
    s32 += parseFloat(h5)
    vac += 1

  break;

  case 'НЗ':
    s34 += parseFloat(h5)
    vac += 1

  break;

  case 'ОЗ':
    s37 += parseFloat(h5)
    vac += 1
  break;

  case 'НОД':
  if (h5.length > 2) {
    h_split = h5.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h5)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h5_ = h5.split('/')

    s1 += parseFloat(h5_[0])
    s19 += parseFloat(h5_[1])
    work += 1
  break;

  case 'Я/Н':
    h5_ = h5.split('/')

    s1 += parseFloat(h5_[0])
    s2 += parseFloat(h5_[1])
    work += 1
  break;

  case 'РВ/Н':
    h5_ = h5.split('/')

    s3 += parseFloat(h5_[0])
    s2 += parseFloat(h5_[1])
    work += 1
  break;
}

switch (tt6) {
  case 'Я':
    s1 += parseFloat(h6)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h6)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h6)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h6)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h6)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h6)
    vac += 1
  break;

  case 'ПК':
    s7 += parseFloat(h6)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h6)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h6)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h6)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h6)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h6)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h6)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h6)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h6)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h6)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h6)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h6)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h6)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h6)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h6)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h6)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h6)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h6)

  break;

  case 'ОВ':
    s25 += parseFloat(h6)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h6)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h6)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h6)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h6)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h6)
    vac += 1
  break;

  case 'ВП':
    s34 += parseFloat(h6)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h6)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h6)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h6)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h6)
    vac += 1
  break;

  case 'НОД':
  if (h6.length > 2) {
    h_split = h6.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h6)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h6_ = h6.split('/')

    s1 += parseFloat(h6_[0])
    s19 += parseFloat(h6_[1])
    work += 1
  break;

  case 'Я/Н':
    h6_ = h6.split('/')

    s1 += parseFloat(h6_[0])
    s2 += parseFloat(h6_[1])
    work += 1
  break;

  case 'РВ/Н':
    h6_ = h6.split('/')

    s3 += parseFloat(h6_[0])
    s2 += parseFloat(h6_[1])
    work += 1
  break;
}

switch (tt7) {
  case 'Я':
    s1 += parseFloat(h7)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h7)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h7)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h7)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h7)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h7)
    vac += 1
  break;

  case 'ПК':
    s7 += parseFloat(h7)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h7)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h7)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h7)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h7)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h7)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h7)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h7)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h7)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h7)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h7)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h7)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h7)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h7)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h7)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h7)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h7)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h7)

  break;

  case 'ОВ':
    s25 += parseFloat(h7)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h7)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h7)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h7)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h7)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h7)
    vac += 1
  break;

  case 'ВП':
    s34 += parseFloat(h7)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h7)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h7)
    vac += 1
  break;


  case 'НЗ':
    s34 += parseFloat(h7)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h7)
    vac += 1
  break;

  case 'НОД':
  if (h7.length > 2) {
    h_split = h7.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h7)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h7_ = h7.split('/')
    s1 += parseFloat(h7_[0])
    s19 += parseFloat(h7_[1])
    work += 1

  break;

  case 'Я/Н':
    h7_ = h7.split('/')
    s1 += parseFloat(h7_[0])
    s2 += parseFloat(h7_[1])
    work += 1

  break;

  case 'РВ/Н':
    h7_ = h7.split('/')
    s3 += parseFloat(h7_[0])
    s2 += parseFloat(h7_[1])
    work += 1

  break;
}

switch (tt8) {
  case 'Я':
    s1 += parseFloat(h8)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h8)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h8)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h8)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h8)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h8)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h8)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h8)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h8)
    vac += 1

  break;

  case 'ОД':
    s10 += parseFloat(h8)
    vac += 1

  break;

  case 'У':
    s11 += parseFloat(h8)
    vac += 1

  break;

  case 'УВ':
    s12 += parseFloat(h8)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h8)
    vac += 1

  break;

  case 'Р':
    s14 += parseFloat(h8)
    vac += 1

  break;

  case 'ОЖ':
    s15 += parseFloat(h8)

    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h8)
    vac += 1

  break;

  case 'Б':
    s17 += parseFloat(h8)
    vac += 1

  break;

  case 'Т':
    s18 += parseFloat(h8)
    vac += 1

  break;

  case 'ЛЧ':
    s19 += parseFloat(h8)
    vac += 1

  break;

  case 'ПВ':
    s20 += parseFloat(h8)
    vac += 1

  break;

  case 'Г':
    s21 += parseFloat(h8)
    vac += 1

  break;

  case 'ПР':
    s22 += parseFloat(h8)
    vac += 1

  break;

  case 'НС':
    s23 += parseFloat(h8)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h8)


  break;

  case 'ОВ':
    s25 += parseFloat(h8)
    vac += 1

  break;

  case 'НВ':
    s26 += parseFloat(h8)
    vac += 1

  break;

  case 'ЗБ':
    s27 += parseFloat(h8)
    vac += 1

  break;

  case 'НН':
    s28 += parseFloat(h8)
    vac += 1

  break;

  case 'РП':
    s29 += parseFloat(h8)
    vac += 1

  break;

  case 'НП':
    s30 += parseFloat(h8)
    vac += 1

  break;

  case 'ВП':
    s34 += parseFloat(h8)
    vac += 1

  break;

  case 'НО':
    s33 += parseFloat(h8)
    vac += 1

  break;

  case 'НБ':
    s32 += parseFloat(h8)
    vac += 1
    break;

  case 'НЗ':
    s34 += parseFloat(h8)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h8)
    vac += 1
  break;

  case 'НОД':
  if (h8.length > 2) {
    h_split = h8.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h8)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h8_ = h8.split('/')
    s1 += parseFloat(h8_[0])
    s19 += parseFloat(h8_[1])
    work += 1
  break;

  case 'Я/Н':
    h8_ = h8.split('/')
    s1 += parseFloat(h8_[0])
    s2 += parseFloat(h8_[1])
    work += 1
  break;

  case 'РВ/Н':
    h8_ = h8.split('/')
    s3 += parseFloat(h8_[0])
    s2 += parseFloat(h8_[1])
    work += 1
  break;
}

switch (tt9) {
  case 'Я':
    s1 += parseFloat(h9)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h9)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h9)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h9)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h9)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h9)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h9)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h9)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h9)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h9)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h9)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h9)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h9)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h9)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h9)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h9)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h9)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h9)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h9)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h9)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h9)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h9)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h9)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h9)


  break;

  case 'ОВ':
    s25 += parseFloat(h9)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h9)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h9)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h9)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h9)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h9)
    vac += 1
  break;

  case 'ВП':
    s34 += parseFloat(h9)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h9)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h9)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h9)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h9)
    vac += 1
  break;

  case 'НОД':
  if (h9.length > 2) {
    h_split = h9.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h9)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h9_ = h9.split('/')
    s1 += parseFloat(h9_[0])
    s19 += parseFloat(h9_[1])
    work += 1
  break;

  case 'Я/Н':
    h9_ = h9.split('/')
    s1 += parseFloat(h9_[0])
    s2 += parseFloat(h9_[1])
    work += 1
  break;

  case 'РВ/Н':
    h9_ = h9.split('/')
    s3 += parseFloat(h9_[0])
    s2 += parseFloat(h9_[1])
    work += 1
  break;
}

switch (tt10) {
  case 'Я':
    s1 += parseFloat(h10)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h10)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h10)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h10)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h10)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h10)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h10)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h10)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h10)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h10)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h10)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h10)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h10)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h10)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h10)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h10)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h10)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h10)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h10)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h10)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h10)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h10)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h10)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h10)


  break;

  case 'ОВ':
    s25 += parseFloat(h10)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h10)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h10)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h10)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h10)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h10)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h10)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h10)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h10)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h10)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h10)
    vac += 1
  break;

  case 'НОД':
  if (h10.length > 2) {
    h_split = h10.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h10)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h10_ = h10.split('/')
    s1 += parseFloat(h10_[0])
    s19 += parseFloat(h10_[1])
    work += 1
  break;

  case 'Я/Н':
    h10_ = h10.split('/')
    s1 += parseFloat(h10_[0])
    s2 += parseFloat(h10_[1])
    work += 1
  break;

  case 'РВ/Н':
    h10_ = h10.split('/')
    s3 += parseFloat(h10_[0])
    s2 += parseFloat(h10_[1])
    work += 1
  break;
}

switch (tt11) {
  case 'Я':
    s1 += parseFloat(h11)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h11)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h11)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h11)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h11)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h11)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h11)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h11)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h11)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h11)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h11)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h11)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h11)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h11)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h11)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h11)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h11)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h11)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h11)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h11)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h11)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h11)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h11)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h11)


  break;

  case 'ОВ':
    s25 += parseFloat(h11)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h11)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h11)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h11)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h11)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h11)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h11)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h11)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h11)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h11)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h11)
    vac += 1
  break;

  case 'НОД':
  if (h11.length > 2) {
    h_split = h11.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h11)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h11_ = h11.split('/')
    s1 += parseFloat(h11_[0])
    s19 += parseFloat(h11_[1])
    work += 1
  break;

  case 'Я/Н':
    h11_ = h11.split('/')
    s1 += parseFloat(h11_[0])
    s2 += parseFloat(h11_[1])
    work += 1
  break;

  case 'РВ/Н':
    h11_ = h11.split('/')
    s3 += parseFloat(h11_[0])
    s2 += parseFloat(h11_[1])
    work += 1


  break;
}

switch (tt12) {
  case 'Я':
    s1 += parseFloat(h12)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h12)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h12)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h12)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h12)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h12)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h12)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h12)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h12)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h12)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h12)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h12)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h12)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h12)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h12)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h12)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h12)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h12)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h12)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h12)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h12)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h12)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h12)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h12)


  break;

  case 'ОВ':
    s25 += parseFloat(h12)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h12)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h12)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h12)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h12)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h12)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h12)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h12)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h12)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h12)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h12)
    vac += 1
  break;

  case 'НОД':
  if (h12.length > 2) {
    h_split = h12.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h12)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h12_ = h12.split('/')
    s1 += parseFloat(h12_[0])
    s19 += parseFloat(h12_[1])
    work += 1
  break;

  case 'Я/Н':
    h12_ = h12.split('/')
    s1 += parseFloat(h12_[0])
    s2 += parseFloat(h12_[1])
    work += 1
  break;

  case 'РВ/Н':
    h12_ = h12.split('/')
    s3 += parseFloat(h12_[0])
    s2 += parseFloat(h12_[1])
    work += 1
  break;
}

switch (tt13) {
  case 'Я':
    s1 += parseFloat(h13)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h13)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h13)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h13)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h13)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h13)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h13)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h13)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h13)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h13)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h13)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h13)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h13)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h13)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h13)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h13)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h13)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h13)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h13)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h13)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h13)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h13)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h13)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h13)


  break;

  case 'ОВ':
    s25 += parseFloat(h13)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h13)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h13)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h13)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h13)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h13)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h13)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h13)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h13)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h13)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h13)
    vac += 1
  break;

  case 'НОД':
  if (h13.length > 2) {
    h_split = h13.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h13)
      work += 1
    }
    console.log(s19);
  break;

  case 'Я/ЛЧ':
    h13_ = h13.split('/')
    s1 += parseFloat(h13_[0])
    s19 += parseFloat(h13_[1])
    work += 1
  break;

  case 'Я/Н':
    h13_ = h13.split('/')
    s1 += parseFloat(h13_[0])
    s2 += parseFloat(h13_[1])
    work += 1
  break;

  case 'РВ/Н':
    h13_ = h13.split('/')
    s3 += parseFloat(h13_[0])
    s2 += parseFloat(h13_[1])
    work += 1
  break;
}

switch (tt14) {
  case 'Я':
    s1 += parseFloat(h14)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h14)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h14)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h14)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h14)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h14)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h14)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h14)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h14)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h14)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h14)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h14)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h14)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h14)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h14)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h14)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h14)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h14)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h14)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h14)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h14)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h14)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h14)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h14)

  break;

  case 'ОВ':
    s25 += parseFloat(h14)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h14)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h14)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h14)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h14)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h14)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h14)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h14)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h14)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h14)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h14)
    vac += 1
  break;

  case 'НОД':
  if (h14.length > 2) {
    h_split = h14.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h14)
      work += 1
    }
    console.log(s19);
  break;

  case 'Я/ЛЧ':
    h14_ = h14.split('/')
    s1 += parseFloat(h14_[0])
    s19 += parseFloat(h14_[1])
    work += 1
  break;

  case 'Я/Н':
    h14_ = h14.split('/')
    s1 += parseFloat(h14_[0])
    s2 += parseFloat(h14_[1])
    work += 1
  break;

  case 'РВ/Н':
    h14_ = h14.split('/')
    s3 += parseFloat(h14_[0])
    s2 += parseFloat(h14_[1])
    work += 1
  break;
}

switch (tt15) {
  case 'Я':
    s1 += parseFloat(h15)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h15)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h15)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h15)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h15)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h15)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h15)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h15)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h15)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h15)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h15)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h15)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h15)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h15)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h15)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h15)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h15)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h15)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h15)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h15)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h15)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h15)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h15)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h15)


  break;

  case 'ОВ':
    s25 += parseFloat(h15)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h15)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h15)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h15)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h15)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h15)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h15)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h15)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h15)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h15)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h15)
    vac += 1
  break;

  case 'НОД':
  if (h15.length > 2) {
    h_split = h15.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h15)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h15_ = h15.split('/')
    s1 += parseFloat(h15_[0])
    s19 += parseFloat(h15_[1])

    work += 1
  break;

  case 'Я/Н':
    h15_ = h15.split('/')
    s1 += parseFloat(h15_[0])
    s2 += parseFloat(h15_[1])
    work += 1
  break;

  case 'РВ/Н':
    h15_ = h15.split('/')
    s3 += parseFloat(h15_[0])
    s2 += parseFloat(h15_[1])
    work += 1
  break;
}

switch (tt16) {
  case 'Я':
    s1 += parseFloat(h16)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h16)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h16)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h16)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h16)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h16)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h16)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h16)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h16)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h16)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h16)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h16)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h16)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h16)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h16)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h16)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h16)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h16)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h16)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h16)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h16)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h16)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h16)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h16)


  break;

  case 'ОВ':
    s25 += parseFloat(h16)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h16)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h16)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h16)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h16)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h16)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h16)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h16)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h16)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h16)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h16)
    vac += 1
  break;

  case 'НОД':
  if (h16.length > 2) {
    h_split = h16.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h16)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h16_ = h16.split('/')
    s1 += parseFloat(h16_[0])
    s19 += parseFloat(h16_[1])
    work += 1
  break;

  case 'Я/Н':
    h16_ = h16.split('/')
    s1 += parseFloat(h16_[0])
    s2 += parseFloat(h16_[1])
    work += 1
  break;

  case 'РВ/Н':
    h16_ = h16.split('/')
    s3 += parseFloat(h16_[0])
    s2 += parseFloat(h16_[1])
    work += 1
  break;
}

switch (tt17) {
  case 'Я':
    s1 += parseFloat(h17)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h17)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h17)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h17)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h17)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h17)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h17)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h17)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h17)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h17)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h17)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h17)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h17)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h17)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h17)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h17)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h17)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h17)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h17)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h17)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h17)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h17)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h17)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h17)


  break;

  case 'ОВ':
    s25 += parseFloat(h17)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h17)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h17)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h17)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h17)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h17)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h17)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h17)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h17)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h17)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h17)
    vac += 1
  break;

  case 'НОД':
  if (h17.length > 2) {
    h_split = h17.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h17)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h17_ = h17.split('/')
    s1 += parseFloat(h17_[0])
    s19 += parseFloat(h17_[1])
    work += 1
  break;

  case 'Я/Н':
    h17_ = h17.split('/')
    s1 += parseFloat(h17_[0])
    s2 += parseFloat(h17_[1])
    work += 1
  break;

  case 'РВ/Н':
    h17_ = h17.split('/')
    s3 += parseFloat(h17_[0])
    s2 += parseFloat(h17_[1])
    work += 1
  break;
}

switch (tt18) {
  case 'Я':
    s1 += parseFloat(h18)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h18)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h18)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h18)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h18)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h18)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h18)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h18)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h18)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h18)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h18)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h18)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h18)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h18)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h18)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h18)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h18)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h18)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h18)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h18)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h18)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h18)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h18)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h18)


  break;

  case 'ОВ':
    s25 += parseFloat(h18)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h18)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h18)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h18)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h18)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h18)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h18)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h18)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h18)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h18)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h18)
    vac += 1
  break;

  case 'НОД':
  if (h18.length > 2) {
    h_split = h18.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h18)
      work += 1
    }
    console.log(s19);
  break;

  case 'Я/ЛЧ':
    h18_ = h18.split('/')
    s1 += parseFloat(h18_[0])
    s19 += parseFloat(h18_[1])
    work += 1
  break;

  case 'Я/Н':
    h18_ = h18.split('/')
    s1 += parseFloat(h18_[0])
    s2 += parseFloat(h18_[1])
    work += 1
  break;

  case 'РВ/Н':
    h18_ = h18.split('/')
    s3 += parseFloat(h18_[0])
    s2 += parseFloat(h18_[1])
    work += 1
  break;
}

switch (tt19) {
  case 'Я':
    s1 += parseFloat(h19)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h19)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h19)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h19)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h19)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h19)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h19)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h19)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h19)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h19)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h19)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h19)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h19)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h19)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h19)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h19)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h19)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h19)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h19)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h19)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h19)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h19)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h19)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h19)


  break;

  case 'ОВ':
    s25 += parseFloat(h19)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h19)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h19)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h19)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h19)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h19)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h19)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h19)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h19)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h19)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h19)
    vac += 1
  break;

  case 'НОД':
  if (h19.length > 2) {
    h_split = h19.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h19)
      work += 1
    }
    console.log(s19);
  break;

  case 'Я/ЛЧ':
    h19_ = h19.split('/')
    s1 += parseFloat(h19_[0])
    s19 += parseFloat(h19_[1])
    work += 1
  break;

  case 'Я/Н':
    h19_ = h19.split('/')
    s1 += parseFloat(h19_[0])
    s2 += parseFloat(h19_[1])
    work += 1
  break;

  case 'РВ/Н':
    h19_ = h19.split('/')
    s3 += parseFloat(h19_[0])
    s2 += parseFloat(h19_[1])
    work += 1
  break;
}

switch (tt20) {
  case 'Я':
    s1 += parseFloat(h20)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h20)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h20)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h20)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h20)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h20)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h20)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h20)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h20)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h20)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h20)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h20)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h20)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h20)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h20)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h20)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h20)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h20)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h20)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h20)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h20)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h20)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h20)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h20)


  break;

  case 'ОВ':
    s25 += parseFloat(h20)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h20)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h20)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h20)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h20)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h20)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h20)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h20)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h20)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h20)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h20)
    vac += 1
  break;

  case 'НОД':
  if (h20.length > 2) {
    h_split = h20.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h20)
      work += 1
    }
    console.log(s19);
  break;

  case 'Я/ЛЧ':
    h20_ = h20.split('/')
    s1 += parseFloat(h20_[0])
    s19 += parseFloat(h20_[1])
    work += 1
  break;

  case 'Я/Н':
    h20_ = h20.split('/')
    s1 += parseFloat(h20_[0])
    s2 += parseFloat(h20_[1])
    work += 1
  break;

  case 'РВ/Н':
    h20_ = h20.split('/')
    s3 += parseFloat(h20_[0])
    s2 += parseFloat(h20_[1])
    work += 1
  break;
}

switch (tt21) {
  case 'Я':
    s1 += parseFloat(h21)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h21)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h21)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h21)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h21)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h21)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h21)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h21)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h21)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h21)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h21)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h21)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h21)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h21)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h21)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h21)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h21)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h21)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h21)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h21)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h21)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h21)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h21)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h21)


  break;

  case 'ОВ':
    s25 += parseFloat(h21)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h21)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h21)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h21)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h21)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h21)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h21)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h21)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h21)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h21)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h21)
    vac += 1
  break;

  case 'НОД':
  if (h21.length > 2) {
    h_split = h21.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h21)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h21_ = h21.split('/')
    s1 += parseFloat(h21_[0])
    s19 += parseFloat(h21_[1])
    work += 1
  break;

  case 'Я/Н':
    h21_ = h21.split('/')
    s1 += parseFloat(h21_[0])
    s2 += parseFloat(h21_[1])
    work += 1
  break;

  case 'РВ/Н':
    h21_ = h21.split('/')
    s3 += parseFloat(h21_[0])
    s2 += parseFloat(h21_[1])
    work += 1
  break;
}

switch (tt22) {
  case 'Я':
    s1 += parseFloat(h22)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h22)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h22)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h22)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h22)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h22)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h22)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h22)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h22)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h22)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h22)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h22)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h22)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h22)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h22)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h22)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h22)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h22)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h22)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h22)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h22)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h22)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h22)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h22)


  break;

  case 'ОВ':
    s25 += parseFloat(h22)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h22)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h22)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h22)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h22)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h22)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h22)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h22)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h22)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h22)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h22)
    vac += 1
  break;

  case 'НОД':
  if (h22.length > 2) {
    h_split = h22.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h22)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h22_ = h22.split('/')
    s1 += parseFloat(h22_[0])
    s19 += parseFloat(h22_[1])

    work += 1
  break;

  case 'Я/Н':
    h22_ = h22.split('/')
    s1 += parseFloat(h22_[0])
    s2 += parseFloat(h22_[1])
    work += 1
  break;

  case 'РВ/Н':
    h22_ = h22.split('/')
    s3 += parseFloat(h22_[0])
    s2 += parseFloat(h22_[1])
    work += 1
  break;
}

switch (tt23) {
  case 'Я':
    s1 += parseFloat(h23)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h23)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h23)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h23)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h23)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h23)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h23)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h23)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h23)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h23)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h23)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h23)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h23)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h23)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h23)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h23)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h23)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h23)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h23)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h23)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h23)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h23)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h23)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h23)


  break;

  case 'ОВ':
    s25 += parseFloat(h23)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h23)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h23)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h23)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h23)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h23)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h23)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h23)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h23)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h23)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h23)
    vac += 1
  break;

  case 'НОД':
  if (h23.length > 2) {
    h_split = h23.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h23)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h23_ = h23.split('/')
    s1 += parseFloat(h23_[0])
    s19 += parseFloat(h23_[1])
    work += 1
  break;

  case 'Я/Н':
    h23_ = h23.split('/')
    s1 += parseFloat(h23_[0])
    s2 += parseFloat(h23_[1])
    work += 1
  break;

  case 'РВ/Н':
    h23_ = h23.split('/')
    s3 += parseFloat(h23_[0])
    s2 += parseFloat(h23_[1])
    work += 1
  break;
}

switch (tt24) {
  case 'Я':
    s1 += parseFloat(h24)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h24)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h24)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h24)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h24)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h24)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h24)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h24)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h24)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h24)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h24)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h24)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h24)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h24)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h24)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h24)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h24)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h24)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h24)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h24)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h24)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h24)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h24)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h24)


  break;

  case 'ОВ':
    s25 += parseFloat(h24)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h24)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h24)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h24)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h24)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h24)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h24)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h24)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h24)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h24)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h24)
    vac += 1
  break;

  case 'НОД':
  if (h24.length > 2) {
    h_split = h24.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h24)
      work += 1
    }
    console.log(s19);
  break;

  case 'Я/ЛЧ':
    h24_ = h24.split('/')
    s1 += parseFloat(h24_[0])
    s19 += parseFloat(h24_[1])
    work += 1
  break;

  case 'Я/Н':
    h24_ = h24.split('/')
    s1 += parseFloat(h24_[0])
    s2 += parseFloat(h24_[1])
    work += 1
  break;

  case 'РВ/Н':
    h24_ = h24.split('/')
    s3 += parseFloat(h24_[0])
    s2 += parseFloat(h24_[1])
    work += 1
  break;
}

switch (tt25) {
  case 'Я':
    s1 += parseFloat(h25)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h25)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h25)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h25)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h25)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h25)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h25)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h25)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h25)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h25)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h25)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h25)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h25)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h25)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h25)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h25)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h25)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h25)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h25)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h25)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h25)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h25)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h25)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h25)


  break;

  case 'ОВ':
    s25 += parseFloat(h25)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h25)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h25)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h25)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h25)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h25)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h25)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h25)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h25)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h25)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h25)
    vac += 1
  break;

  case 'НОД':
  if (h25.length > 2) {
    h_split = h25.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h25)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h25_ = h25.split('/')
    s1 += parseFloat(h25_[0])
    s19 += parseFloat(h25_[1])
    work += 1
  break;

  case 'Я/Н':
    h25_ = h25.split('/')
    s1 += parseFloat(h25_[0])
    s2 += parseFloat(h25_[1])
    work += 1
  break;

  case 'РВ/Н':
    h25_ = h25.split('/')
    s3 += parseFloat(h25_[0])
    s2 += parseFloat(h25_[1])
    work += 1
  break;
}

switch (tt26) {
  case 'Я':
    s1 += parseFloat(h26)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h26)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h26)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h26)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h26)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h26)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h26)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h26)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h26)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h26)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h26)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h26)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h26)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h26)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h26)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h26)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h26)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h26)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h26)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h26)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h26)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h26)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h26)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h26)


  break;

  case 'ОВ':
    s25 += parseFloat(h26)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h26)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h26)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h26)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h26)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h26)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h26)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h26)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h26)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h26)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h26)
    vac += 1
  break;

  case 'НОД':
  if (h26.length > 2) {
    h_split = h26.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h26)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h26_ = h26.split('/')
    s1 += parseFloat(h26_[0])
    s19 += parseFloat(h26_[1])
    work += 1
  break;

  case 'Я/Н':
    h26_ = h26.split('/')
    s1 += parseFloat(h26_[0])
    s2 += parseFloat(h26_[1])
    work += 1
  break;

  case 'РВ/Н':
    h26_ = h26.split('/')
    s3 += parseFloat(h26_[0])
    s2 += parseFloat(h26_[1])
    work += 1
  break;
}

switch (tt27) {
  case 'Я':
    s1 += parseFloat(h27)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h27)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h27)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h27)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h27)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h27)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h27)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h27)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h27)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h27)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h27)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h27)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h27)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h27)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h27)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h27)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h27)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h27)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h27)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h27)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h27)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h27)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h27)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h27)


  break;

  case 'ОВ':
    s25 += parseFloat(h27)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h27)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h27)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h27)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h27)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h27)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h27)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h27)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h27)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h27)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h27)
    vac += 1
  break;

  case 'НОД':
  if (h27.length > 2) {
    h_split = h27.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h27)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h27_ = h27.split('/')
    s1 += parseFloat(h27_[0])
    s19 += parseFloat(h27_[1])
    work += 1
  break;

  case 'Я/Н':
    h27_ = h27.split('/')
    s1 += parseFloat(h27_[0])
    s2 += parseFloat(h27_[1])
    work += 1
  break;

  case 'РВ/Н':
    h27_ = h27.split('/')
    s3 += parseFloat(h27_[0])
    s2 += parseFloat(h27_[1])
    work += 1
  break;
}

switch (tt28) {
  case 'Я':
    s1 += parseFloat(h28)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h28)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h28)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h28)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h28)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h28)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h28)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h28)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h28)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h28)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h28)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h28)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h28)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h28)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h28)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h28)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h28)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h28)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h28)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h28)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h28)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h28)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h28)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h28)


  break;

  case 'ОВ':
    s25 += parseFloat(h28)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h28)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h28)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h28)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h28)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h28)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h28)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h28)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h28)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h28)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h28)
    vac += 1
  break;

  case 'НОД':
  if (h28.length > 2) {
    h_split = h28.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h28)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h28_ = h28.split('/')
    s1 += parseFloat(h28_[0])
    s19 += parseFloat(h28_[1])
    work += 1
  break;

  case 'Я/Н':
    h28_ = h28.split('/')
    s1 += parseFloat(h28_[0])
    s2 += parseFloat(h28_[1])
    work += 1
  break;

  case 'РВ/Н':
    h28_ = h28.split('/')
    s3 += parseFloat(h28_[0])
    s2 += parseFloat(h28_[1])
    work += 1
  break;
}

switch (tt29) {
  case 'Я':
    s1 += parseFloat(h29)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h29)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h29)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h29)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h29)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h29)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h29)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h29)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h29)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h29)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h29)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h29)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h29)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h29)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h29)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h29)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h29)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h29)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h29)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h29)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h29)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h29)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h29)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h29)


  break;

  case 'ОВ':
    s25 += parseFloat(h29)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h29)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h29)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h29)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h29)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h29)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h29)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h29)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h29)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h29)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h29)
    vac += 1
  break;

  case 'НОД':
  if (h29.length > 2) {
    h_split = h29.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h29)
      work += 1
    }
    console.log(s19);
  break;

  case 'Я/ЛЧ':
    h29_ = h29.split('/')
    s1 += parseFloat(h29_[0])
    s19 += parseFloat(h29_[1])

    work += 1
  break;

  case 'Я/Н':
    h29_ = h29.split('/')
    s1 += parseFloat(h29_[0])
    s2 += parseFloat(h29_[1])
    work += 1
  break;

  case 'РВ/Н':
    h29_ = h29.split('/')
    s3 += parseFloat(h29_[0])
    s2 += parseFloat(h29_[1])
    work += 1
  break;
}

switch (tt30) {
  case 'Я':
    s1 += parseFloat(h30)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h30)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h30)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h30)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h30)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h30)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h30)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h30)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h30)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h30)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h30)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h30)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h30)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h30)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h30)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h30)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h30)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h30)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h30)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h30)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h30)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h30)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h30)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h30)


  break;

  case 'ОВ':
    s25 += parseFloat(h30)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h30)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h30)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h30)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h30)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h30)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h30)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h30)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h30)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h30)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h30)
    vac += 1
  break;

  case 'НОД':
  if (h30.length > 2) {
    h_split = h30.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h30)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h30_ = h30.split('/')
    s1 += parseFloat(h30_[0])
    s19 += parseFloat(h30_[1])
    work += 1
  break;

  case 'Я/Н':
    h30_ = h30.split('/')
    s1 += parseFloat(h30_[0])
    s2 += parseFloat(h30_[1])
    work += 1
  break;

  case 'РВ/Н':
    h30_ = h30.split('/')
    s3 += parseFloat(h30_[0])
    s2 += parseFloat(h30_[1])
    work += 1
  break;
}

switch (tt31) {
  case 'Я':
    s1 += parseFloat(h31)
    work += 1
  break;

  case 'Н':
    s2 += parseFloat(h31)
    work += 1
  break;

  case 'РВ':
    s3 += parseFloat(h31)
    work += 1
  break;

  case 'ВМ':
    s5 += parseFloat(h31)
    work += 1
  break;

  case 'КМ':
    s36 += parseFloat(h31)
    work += 1
  break;

  case 'К':
    s6 += parseFloat(h31)
    vac += 1
  break;


  case 'ПК':
    s7 += parseFloat(h31)
    work += 1
  break;

  case 'ПМ':
    s8 += parseFloat(h31)
    work += 1
  break;

  case 'ОТ':
    s9 += parseFloat(h31)
    vac += 1
  break;

  case 'ОД':
    s10 += parseFloat(h31)
    vac += 1
  break;

  case 'У':
    s11 += parseFloat(h31)
    vac += 1
  break;

  case 'УВ':
    s12 += parseFloat(h31)
    work += 1
  break;

  case 'УД':
    s13 += parseFloat(h31)
    vac += 1
  break;

  case 'Р':
    s14 += parseFloat(h31)
    vac += 1
  break;

  case 'ОЖ':
    s15 += parseFloat(h31)
    vac += 1
  break;

  case 'ДО':
    s16 += parseFloat(h31)
    vac += 1
  break;

  case 'Б':
    s17 += parseFloat(h31)
    vac += 1
  break;

  case 'Т':
    s18 += parseFloat(h31)
    vac += 1
  break;

  case 'ЛЧ':
    s19 += parseFloat(h31)
    vac += 1
  break;

  case 'ПВ':
    s20 += parseFloat(h31)
    vac += 1
  break;

  case 'Г':
    s21 += parseFloat(h31)
    vac += 1
  break;

  case 'ПР':
    s22 += parseFloat(h31)
    vac += 1
  break;

  case 'НС':
    s23 += parseFloat(h31)
    work += 1
  break;

  case 'В':
    s24 += parseFloat(h31)


  break;

  case 'ОВ':
    s25 += parseFloat(h31)
    vac += 1
  break;

  case 'НВ':
    s26 += parseFloat(h31)
    vac += 1
  break;

  case 'ЗБ':
    s27 += parseFloat(h31)
    vac += 1
  break;

  case 'НН':
    s28 += parseFloat(h31)
    vac += 1
  break;

  case 'РП':
    s29 += parseFloat(h31)
    vac += 1
  break;

  case 'НП':
    s30 += parseFloat(h31)
    vac += 1
  break;

  case 'ВП':
    s31 += parseFloat(h31)
    vac += 1
  break;

  case 'НО':
    s33 += parseFloat(h31)
    vac += 1
  break;

  case 'НБ':
    s32 += parseFloat(h31)
    vac += 1
  break;

  case 'НЗ':
    s34 += parseFloat(h31)
    vac += 1
  break;

  case 'ОЗ':
    s37 += parseFloat(h31)
    vac += 1
  break;

  case 'НОД':
  if (h31.length > 2) {
    h_split = h31.split('/')


      s38 += parseFloat(h_split[0])
      s19 += parseFloat(h_split[1])


    work += 1 }
    else {
      s38 += parseFloat(h31)
      work += 1
    }
    console.log(s19);
  break;


  case 'Я/ЛЧ':
    h31_ = h31.split('/')
    s1 += parseFloat(h31_[0])
    s19 += parseFloat(h31_[1])
    work += 1
  break;

  case 'Я/Н':
    h31_ = h31.split('/')
    s1 += parseFloat(h31_[0])
    s2 += parseFloat(h31_[1])
    work += 1
  break;

  case 'РВ/Н':
    h31_ = h31.split('/')
    s3 += parseFloat(h31_[0])
    s2 += parseFloat(h31_[1])
    work += 1
  break;
}

h_work = s1 + s5 + s3 + s36 + s7 + s8 + s23 + s38
console.log(h_work);
h_vac = s9 + s10 + s11 + s13 + s14 + s15 + s16 + s17 + s18 + s20 + s21 +  s24 + s25 + s26 + s27 + s28 + s29 + s30 + s31 + s32 + s33 + s34 + s37

weekends = s24/8


if ($('#manover').prop('checked') == false){
s4 = h_work - parseFloat($('#n_time').text()) - s3}

if (s4 < 0) {
  s4 = 0
}

$('#weekends').val(weekends)
$('#id_sHours1').val(s1)
$('#id_sHours2').val(s2)
$('#id_sHours3').val(s3)
if ($('#manover').prop('checked') == false){
$('#id_sHours4').val(s4)}
$('#id_sHours5').val(s5)
$('#id_sHours6').val(s6)
$('#id_sHours7').val(s7)
$('#id_sHours8').val(s8)
$('#id_sHours9').val(s9)
$('#id_sHours10').val(s10)
$('#id_sHours11').val(s11)
$('#id_sHours12').val(s12)
$('#id_sHours13').val(s13)
$('#id_sHours14').val(s14)
$('#id_sHours15').val(s15)
$('#id_sHours16').val(s16)
$('#id_sHours17').val(s17)
$('#id_sHours18').val(s18)




    $('#id_sHours19').val(s19)

$('#id_sHours20').val(s20)
$('#id_sHours21').val(s21)
$('#id_sHours22').val(s22)
$('#id_sHours23').val(s23)
$('#id_sHours24').val(s24)
$('#id_sHours25').val(s25)
$('#id_sHours26').val(s26)
$('#id_sHours27').val(s27)
$('#id_sHours28').val(s28)
$('#id_sHours29').val(s29)
$('#id_sHours30').val(s30)
$('#id_sHours31').val(s31)
$('#id_sHours32').val(s32)
$('#id_sHours33').val(s33)
$('#id_sHours34').val(s34)
$('#id_sHours37').val(s37)
$('#id_sHours38').val(s38)
$('#id_w_days').val(work)
$('#id_w_hours').val(h_work)
$('#id_v_days').val(vac)
$('#id_v_hours').val(h_vac)

console.log(s19);

sum_fields = $('.summary_times').children('.st')
container = $('#tabel_item')

for (var i = 0; i < sum_fields.length; i++) {
  sum_puts = sum_fields[i].childNodes
  for (var j = 0; j < sum_puts.length; j++) {
    if (sum_puts[j].tagName == 'INPUT') {
      if (sum_puts[j].value == 0) {
        sum_fields[i].style.display = 'none'
      }
      else {
        sum_fields[i].style.display = 'block'
        container_heigth = window.getComputedStyle(container[0]).height;
        container_heigth = parseInt(container_heigth, 10)
        container_heigth += 38
        container[0].style.height = container_heigth + 'px'
      }
    }
  }


}
}
