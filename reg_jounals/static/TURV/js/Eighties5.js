$(document).ready(function()

{

DrawDays()

let vacs = ['ОТ','ОД','У','УД','Р','ОЖ','ДО','Б','Т','ПВ','Г','ПР','В','ОВ','НВ','ЗБ','НН','РП','НП','ВП','НБ','НО','НЗ','ДБ','ОЗ', 'К']

  types_rows = $('.time_types')
  types_rows_nums = $('.time_types').children('.print-num')
  types = $('.cell_ttime')
  hours = $('.cell_hours')
  vac_include = $('.vac-include')
  weekends = $('.weekends')
  let s1 = 0 //явки
  let s2 = 0 //ночные
  let s3 = 0 //РВ
  let s4 = 0 //сверхурочка
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
  let s37 = 0 //ОЗ


// Убрать NONE

for (var i = 0; i < types.length; i++) {
  if (types[i].innerText == 'None') {
    types[i].textContent = ""
  }
}

for (var i = 0; i < types.length; i++) {
  if (hours[i].innerText == 'None') {
    hours[i].textContent = ""
  }
}

// --------------------------------------------------


for (var i = 0; i < types.length; i++) {
  vacs.forEach(function(item, j, arr) {
    if (types[i].innerText == item) {
      hours[i].textContent = ''
    }
  });
}





// ПОДСЧЕТ И ВЫВОД ИТОГОВ ПО НЕЯВКАМ

for (var i = 0; i < types_rows.length; i++) {

n = i+1
types_rows_nums[i].textContent = n

  s9 = 0
  s10 = 0
  s11 = 0
  s13 = 0
  s14 = 0
  s15 = 0
  s16 = 0
  s17 = 0
  s18 = 0
  s20 = 0
  s21 = 0
  s22 = 0
  s24 = 0
  s25 = 0
  s26 = 0
  s27 = 0
  s28 = 0
  s29 = 0
  s30 = 0
  s31 = 0
  s32 = 0
  s33 = 0
  s34 = 0
  s37 = 0
  s6 = 0
  cells = types_rows[i].childNodes

  for (var j = 0; j < cells.length; j++) {
    // if (cells[j].className == 'cell_ttime') {

      switch (cells[j].innerText) {
        case 'ОТ':
          s9 += 1

        break;

        case 'ОД':
          s10 +=1

        break;

        case 'У':
          s11 +=1

        break;

        case 'УД':
          s13 +=1

        break;

        case 'Р':
          s14 +=1

        break;

        case 'ОЖ':
          s15 +=1

        break;

        case 'ДО':
          s16 +=1

        break;

        case 'Б':
          s17 +=1

        break;

        case 'Т':
          s18 +=1
        break;

        case 'ПВ':
          s20 +=1
        break;

        case 'Г':
          s21 +=1
        break;

        case 'ПР':
          s22 +=1
        break;

        case 'ОВ':
          s25 +=1
        break;

        case 'НВ':
          s26 +=1
        break;

        case 'ЗБ':
          s27 +=1
        break;

        case 'НН':
          s28 +=1
        break;

        case 'РП':
          s29 +=1
        break;

        case 'НП':
          s30 +=1
        break;

        case 'ВП':
          s31 +=1
        break;

        case 'ВП':
          s31 +=1
        break;

        case 'НБ':
          s32 +=1
        break;

        case 'НО':
          s33 +=1
        break;

        case 'НЗ':
          s34 +=1
        break;

        case 'ОЗ':
          s37 +=1
        break;

        case 'К':
          s6 +=1
        break;





        default:

      }

}








  if (s6 != 0) {
  vac_include[i].textContent += ' | К ' + s6}
  if (s9 != 0) {
  vac_include[i].textContent += ' | ОТ ' + s9}
  if (s10 != 0) {
  vac_include[i].textContent += ' | ОД ' + s10}
  if (s11 != 0) {
  vac_include[i].textContent += ' | У ' + s11}
  if (s13 != 0) {
  vac_include[i].textContent += ' | УД ' + s13}
  if (s14 != 0) {
  vac_include[i].textContent += ' | Р ' + s14}
  if (s15 != 0) {
  vac_include[i].textContent +=  ' | ОЖ ' + s15}
  if (s16 != 0) {
  vac_include[i].textContent +=  ' | ДО ' + s16}
  if (s17 != 0) {
  vac_include[i].textContent +=  ' | Б ' + s17}
  if (s18 != 0) {
  vac_include[i].textContent +=  ' | Т ' + s18}
  if (s20 != 0) {
  vac_include[i].textContent +=  ' | ПВ ' + s20}
  if (s21 != 0) {
  vac_include[i].textContent +=  ' | Г ' + s21}
  if (s22 != 0) {
  vac_include[i].textContent +=  ' | ПР ' + s22}
  if (s25 != 0) {
  vac_include[i].textContent +=  ' | ОВ ' + s25}
  if (s26 != 0) {
  vac_include[i].textContent +=  ' | НВ ' + s26}
  if (s27 != 0) {
  vac_include[i].textContent +=  ' | ЗБ ' + s27}
  if (s28 != 0) {
  vac_include[i].textContent +=  ' | НН ' + s28}
  if (s29 != 0) {
  vac_include[i].textContent +=  ' | РП ' + s29}
  if (s30 != 0) {
  vac_include[i].textContent +=  ' | НП ' + s30}
  if (s31 != 0) {
  vac_include[i].textContent +=  ' | ВП ' + s31}
  if (s32 != 0) {
  vac_include[i].textContent +=  ' | НБ ' + s32}
  if (s33 != 0) {
  vac_include[i].textContent +=  ' | НО ' + s33}
  if (s34 != 0) {
  vac_include[i].textContent +=  ' | ОЗ ' + s34}
  if (s37 != 0) {
  vac_include[i].textContent +=  ' | ОЗ ' + s37}


weekends[i].textContent =  parseInt(weekends[i].innerText, 10)/8


}

// --------------------------------------------------------------------

//ПЕРЕВОД НОМЕРА МЕСЯЦА В НУЖНЫЙ ФОРМАТ ДЛЯ ПОДСЧЕТА КОЛ-ВА ДНЕЙ
function DrawDays() {
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
//--------------------------------------------------------

// ОТРИСОВКА ЧИСЕЛ В ЗАВИСИМОСТИ ОТ КОЛ-ВА ДНЕЙ

days_count = Date.getDaysInMonth(year_, rMonth)





let days29 = $('.day29')
let days30 = $('.day30')
let days31 = $('.day31')




switch (days_count) {

case 28:

  for (var i = 0; i < days29.length; i++) {
    days29[i].style.display = 'None'
  }


  for (var i = 0; i < days30.length; i++) {
    days30[i].style.display = 'None'
  }

  for (var i = 0; i < days31.length; i++) {
    days31[i].style.display = 'None'
  }


  case 29:

    for (var i = 0; i < days30.length; i++) {
      days30[i].style.display = 'None'
    }

    for (var i = 0; i < days31.length; i++) {
      days31[i].style.display = 'None'
    }


  case 30:


    for (var i = 0; i < days31.length; i++) {
      days31[i].style.display = 'None'
    }








  break;
default:

}
}
$('#cover_from').text("01." + month_ + "." + year_)
$('#cover_to').text(days_count + "." + month_ + "." + year_)
$('#cover_today').text(Date.today().toString("dd.MM.yyyy"))
$('.tabel').css('display', '')
// ---------------------------------------------------------
})
