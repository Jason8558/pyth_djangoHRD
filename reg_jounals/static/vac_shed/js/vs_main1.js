function end_count(date_from, days) {
  date_from_new = date_from.split('-')[2] + '.' + date_from.split('-')[1] + '.' + date_from.split('-')[0]

if (days) {
  date_to = Date.parse(date_from_new).addDays(parseInt(days, 10)-1)}
else {
    date_to = Date.parse(date_from_new).addDays(parseInt(days2, 10))
}

console.log(date_to.toString('yyyy-MM-dd'));

  return(date_to.toString('yyyy-MM-dd'))
}

function celebrates(date_from, date_to, id) {
  date_from = date_from.split('-')[2] + '.' + date_from.split('-')[1] + '.' + date_from.split('-')[0]
  date_to = date_to.split('-')[2] + '.' + date_to.split('-')[1] + '.' + date_to.split('-')[0]


  jan = [1,2,3,4,5,6,7,8]
  feb = [23]
  mar = [8]
  may = [1,9]
  jun = [12]
  nov = [4]

  total_celebrate = 0

  day_from = date_from.split('.')[0]
  month_from = date_from.split('.')[1]
  year_from = date_from.split('.')[2]

  day_to = date_to.split('.')[0]
  month_to = date_to.split('.')[1]
  year_to = date_to.split('.')[2]

if (day_from[0] == 0) {
  day_from = day_from[1]
}


if (day_to[0] == 0) {
  day_to = day_to[1]
}



  if (month_from != month_to) {
    switch (month_from) {
      case '01':
          for (var day of jan) {
            if (day_from <= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
        break;

      case '02':
          for (var day of feb) {
            if (day_from <= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
        break;

        case '03':
            for (var day of mar) {
              if (day_from <= day) {
                total_celebrate = total_celebrate + 1
                console.log(total_celebrate);
              }
            }
          break;

          case '05':
          for (var day of may) {
            if (day_from <= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
          break;

          case '06':
          for (var day of jun) {
            if (day_from <= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
          break;

          case '11':
          for (var day of nov) {
            if (day_from <= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
          break;

          default:

        }


  switch (month_to) {
    case '01':
        for (var day of jan) {
          if (day_to >= day) {
            total_celebrate = total_celebrate + 1
            console.log(total_celebrate);
          }
        }
      break;

      case '02':
          for (var day of feb) {
            if (day_to >= day) {
              console.log(day_to);
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
        break;

        case '03':
            for (var day of mar) {
              if (day_to >= day) {
                total_celebrate = total_celebrate + 1
                console.log(total_celebrate);
              }
            }
          break;

          case '04':
              for (var day of mar) {
                if (day_to >= day) {
                  total_celebrate = total_celebrate + 1
                  console.log(total_celebrate);
                }
              }
            break;

          case '05':
          for (var day of may) {
            if (day_to >= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
          break;

          case '06':
          for (var day of jun) {
            if (day_to >= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
          break;

          case '07':
            if (month_from != '06') {

              total_celebrate = total_celebrate + 1}

          break;


          case '10':
          if (month_from != '09' && month_from != '08' && month_from != '07' && month_from != '06' && month_from != '03' && month_from != '02' && month_from != '01') {

              total_celebrate = total_celebrate + 1 }

          break;

          case '11':
          for (var day of nov) {
            if (day_to >= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
          break;

          default:


  }
console.log(total_celebrate);
  }

  else {
    switch (month_from) {
      case '01':
          for (var day of jan) {
            if (day_from <= day && day_to >= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
        break;

      case '02':
          for (var day of feb) {
          if (day_from <= day && day_to >= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
        break;

        case '03':
            for (var day of mar) {
              if (day_from <= day && day_to >= day) {
                total_celebrate = total_celebrate + 1
                console.log(total_celebrate);
              }
            }
          break;

          case '05':
          for (var day of may) {
            if (day_from <= day && day_to >= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
          break;

          case '06':
          for (var day of jun) {
          if (day_from <= day && day_to >= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
          break;

          case '11':
          for (var day of nov) {
          if (day_from <= day && day_to >= day) {
              total_celebrate = total_celebrate + 1
              console.log(total_celebrate);
            }
          }
          break;

          default:

        }

  }

date_to = Date.parse(date_to).addDays(parseInt(total_celebrate, 10));





console.log($('per' + id + ' #per-date-to').val());

$('#per' + id + ' #per-date-to').val(date_to.toString('yyyy-MM-dd'))



}

function celebrates_new(date_from, date_to, id) {

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


  cel_months = [1,2,3,5,6,11]

  jan = [1,2,3,4,5,6,7,8]
  feb = [23]
  mar = [8]
  may = [1,9]
  jun = [12]
  nov = [4]

  total_celebrate = 0


for (var m of cel_months) {
  if (month_from == m) {
    switch (month_from) {

// Январь
      case 1:
        for (var day of jan) {
          if (day_from <= day) {
              total_celebrate = total_celebrate + 1
          }
        }

            console.log(total_celebrate);

        break;

  // Февраль
        case 2:
          for (var day of feb) {
            if (day_from <= day) {
                total_celebrate = total_celebrate + 1
            }
          }
    console.log(total_celebrate);
          break;
  // Март
        case 3:
          for (var day of mar) {
            if (day_from <= day) {
                total_celebrate = total_celebrate + 1
            }
          }
    console.log(total_celebrate);
          break;
  // Май
        case 5:
          for (var day of may) {
            if (day_from <= day) {
                total_celebrate = total_celebrate + 1
            }
          }

          break;

  // Июнь
        case 6:
        for (var day of jun) {
          if (day_from <= day) {
            total_celebrate = total_celebrate + 1
          }
        }

        break;

  // Июнь
        case 11:
        for (var day of nov) {
          if (day_from <= day) {
            total_celebrate = total_celebrate + 1
          }
        }

        break;

    }
  }

}

if (month_from != month_to) {
  for (var i = parseInt(month_from, 10)+1; i <= month_to; i++) {
    for (var m of cel_months) {
      console.log(m);
        console.log(i);
      if (i == m && i != month_to) {

        switch (i) {

    // Январь
          case 1:
          total_celebrate = total_celebrate + jan.length
          break;

      // Февраль
            case 2:
            total_celebrate = total_celebrate + feb.length
                console.log(total_celebrate);
            break;

      // Март
            case 3:
            total_celebrate = total_celebrate + mar.length
                console.log(total_celebrate);
            break;
      // Май
            case 5:
            total_celebrate = total_celebrate + may.length
            break;

      // Июнь
            case 6:
            total_celebrate = total_celebrate + jun.length
            break;

      // Ноябрь
            case 11:
            total_celebrate = total_celebrate + nov.length
            break;

        }

      }
else if (i == m && i == month_to) {
  switch (month_to) {

// Январь
    case 1:
      for (var day of jan) {
        if (day_to >= day) {
            total_celebrate = total_celebrate + 1
        }
      }

      break;

// Февраль
      case 2:
        for (var day of feb) {
          if (day_to >= day) {
              total_celebrate = total_celebrate + 1
          }
        }
    console.log(total_celebrate);
        break;
// Март
      case 3:
        for (var day of mar) {
          if (day_to >= day) {
              total_celebrate = total_celebrate + 1
          }
        }

        break;
// Май
      case 5:
        for (var day of may) {
          if (day_to >= day) {
              total_celebrate = total_celebrate + 1
          }
        }

        break;

// Июнь
      case 6:
      for (var day of jun) {
        if (day_to >= day) {
          total_celebrate = total_celebrate + 1
        }
      }

      break;

// Июнь
      case 11:
      for (var day of nov) {
        if (day_to >= day) {
          total_celebrate = total_celebrate + 1
        }
      }

      break;

  }

}

    }
  }
}

else {
  total_celebrate = 0
  switch (month_from) {
    case 1:
      for (var i = day_from; i <= day_to; i++) {
        for (var day of jan) {
          if (i == day) {
            total_celebrate = total_celebrate + 1
          }
        }
      }

      break;

    case 2:
            for (var i = day_from; i <= day_to; i++) {
              for (var day of feb) {
                if (i == day) {
                  total_celebrate = total_celebrate + 1
                }
              }
            }

      break;

      case 3:
      for (var i = day_from; i <= day_to; i++) {
        for (var day of mar) {
          if (i == day) {
            total_celebrate = total_celebrate + 1
          }
        }
      }
        break;

        case 5:
          for (var i = day_from; i <= day_to; i++) {
            for (var day of may) {
              if (i == day) {
                total_celebrate = total_celebrate + 1
              }
            }
          }
        break;

        case 6:
        for (var i = day_from; i <= day_to; i++) {
          for (var day of jun) {
            if (i == day) {
              total_celebrate = total_celebrate + 1
            }
          }
        }
        break;

        case 11:
        for (var i = day_from; i <= day_to; i++) {
          for (var day of nov) {
            if (i == day) {
              total_celebrate = total_celebrate + 1
            }
          }
        }
        break;

        default:

      }
}


//Проверка на високосный февраль
Date.prototype.daysInMonth = function() {
  return 30 - new Date(this.getFullYear(), this.getMonth(), 32).getDate();
};

date_to = Date.parse(date_to).addDays(parseInt(total_celebrate, 10));

if (month_from != month_to) {
  date_to = date_to.toString('yyyy-MM-dd')
  
    if (date_to.split('-')[1] == 2 && date_to.split('-')[2] >= 23) {
    days_in_feb = new Date(year_from,2,30).daysInMonth()
    if (days_in_feb == 29) {
      date_to = Date.parse(date_to).addDays(1)
    }
  }
  }

 

$('#per' + id + ' #per-date-to').val(date_to.toString('yyyy-MM-dd'))

}

//Контекстное меню

function show_context_menu(el, id) {
  
  coords = el.getBoundingClientRect()

  
  
  context_menu_button             = document.getElementById('context-menu-cancel')
  context_menu_container          = document.getElementById('context-menu-container')
  cancel_reason_container         = document.getElementById('cancel-reason-container')
  cancel_reason_accept_container  = document.getElementById('cancel-reason-accept-container')
  cancel_reason_submit            = document.getElementById('cancel-reason-submit')
  cancel_reason_accept            = document.getElementById('cancel-reason-accept')
  
  coords_top = Number(coords.top) + 20
  coords_top = coords_top + 'px'


  el.addEventListener('contextmenu', (e) => {
    e.preventDefault(); //убирает стандартное контекстное меню

    // позиционирует само меню
    context_menu_container.style.display    = 'block'
    context_menu_container.style.position   = 'fixed'
    context_menu_container.style.top        = coords_top
    context_menu_container.style.left       = coords.left + 'px'
  });

  window.addEventListener('scroll', (w) => {
    close_all_forms()
  })

  counter = 0

  context_menu_button.onclick = function() {
    //вызывает форму ввода комментария

    context_menu_container.style.display    = 'none'

    cancel_reason_container.style.display    = 'flex'
    cancel_reason_container.style.position   = 'fixed'
    cancel_reason_container.style.top        = coords_top
    cancel_reason_container.style.left       = coords.left + 'px'

 
  }

  cancel_reason_submit.onclick = function() {
    //вызывает форму подтверждения

    cancel_reason_accept_container.style.display    = 'flex'
    cancel_reason_accept_container.style.position   = 'fixed'
    cancel_reason_accept_container.style.top        = coords_top
    cancel_reason_accept_container.style.left       = coords.left + 'px'    

  }

  cancel_reason_accept.onclick = function() {
    //производит ПОСТ запрос с отменой

    send_cancel_request(id, el)
    close_all_forms()

  }







}

function close_all_forms() {
  //Закрывает все формы и диалоги

  context_menu_container          = document.getElementById('context-menu-container')
  cancel_reason_container         = document.getElementById('cancel-reason-container')
  cancel_reason_accept_container  = document.getElementById('cancel-reason-accept-container')
  additional_menu_panel           = document.getElementById('vacshed-additional-menu-panel')
  vacshed_search_panel            = document.getElementById('vac_shed-search-panel')

  try {
    context_menu_container.style.display            = 'none'
  } catch (error) {
    
  }
  
  try {cancel_reason_container.style.display = 'none'} catch (error) {}
  try {cancel_reason_accept_container.style.display = 'none'} catch (error) {}
  try {additional_menu_panel.style.display = 'none'} catch (error) {}
  try {vacshed_search_panel.style.display  = 'none'} catch (error) {}   
  
  
  

}

//подсветка 

previous_color = '' //сюда заносим предыдущий цвет строки, так как отмененный период выделен красным

//выделяет основные данные
function set_higlight_main(el) {
  hgl_els = el.parentNode.getElementsByClassName('clr_higlight_main')

  for (const hgl of hgl_els) {
    hgl.style.background = 'lightblue'
  }
}

//выделяет период
function set_higlight_period(el) {
  hgl_els = el.parentNode.getElementsByClassName('clr_higlight_period')

  previous_color = hgl_els[0].style.background

  for (const hgl of hgl_els) {
    hgl.style.background = 'lightgreen'
  }


}

function unset_higlight(el) {
  hgl_els = el.parentNode.childNodes

  for (const hgl of hgl_els) {
    hgl.style.background = 'none'
  }

}



function send_cancel_request(id, el) {
  // отправка комментария с отменой отпуска с помощью AJAX
  //получить куку

  csrf_cookie = document.cookie.split(";")

  for (const csrf_cook of csrf_cookie) {
    csrf_cook_ = csrf_cook.split('=')
    if (csrf_cook_[0] = 'csrftoken') {
      csrf_token = csrf_cook_[1]
    }
  }

  cancel_reason = document.getElementById('cancel-reason-input').value

  $.ajax({
    type: "POST",
    url: "/vacshed/itemupd/cancelvac/" + id,
    data: {'incoming': cancel_reason, 'csrfmiddlewaretoken': csrf_token},
    dataType: "json",
    success: (data) => { //в случае успеха переписываем поля таблицы на клиенте
      move_reason_field   = el.parentNode.getElementsByClassName('movefrom')[0]
      comm_field          = el.parentNode.getElementsByClassName('comm')[0]

      if (data.cancel_state == 1) { // Получаем состояние (1 - отменен, 0 - восстановлен)
        move_reason_field.innerText = 'Отменен'
      }
      else {
        move_reason_field.innerText = '' 
      }
      
      comm_field = cancel_reason
    },

    error: function() { // в случае факапа выводим сообщение
      alert('Что то пошло не так')
    }


  });

  document.getElementById('cancel-reason-input').value = ''

}

function open_additional_menu(el) {
  // открыть доп меню
  close_all_forms()

  additional_menu_panel = document.getElementById('vacshed-additional-menu-panel')

  coords = el.getBoundingClientRect()

  additional_menu_panel.style.display   = 'flex'
  additional_menu_panel.style.position  = 'absolute'
  additional_menu_panel.style.top       = (Number(coords.top) + 40) + 'px'
  additional_menu_panel.style.left      = coords.left + 'px'
  additional_menu_panel.style.height    = '67px' 

  additional_menu_panel.addEventListener('mouseleave', (vsp) => {
    close_all_forms()
  })

  el.onclick = function() {
    
    if (additional_menu_panel.style.display == 'none') {
      additional_menu_panel.style.display = 'flex'}
    else {
      additional_menu_panel.style.display = 'none'
      
    }

  }
 

 //el.onclick = 'open_additional_menu(this)'

}

function open_search_menu(el) {
  // открыть меню поиска

  vacshed_search_panel = document.getElementById('vac_shed-search-panel')

  coords = el.getBoundingClientRect()

  vacshed_search_panel.style.display    = 'flex'
  vacshed_search_panel.style.position   = 'absolute'
  vacshed_search_panel.style.top        = (Number(coords.top) + 30) + 'px'
  vacshed_search_panel.style.left       = coords.left + 'px'
  vacshed_search_panel.style.height     = '81px' 

  vacshed_search_panel.addEventListener('mouseleave', (vsp) => {
    close_all_forms()
  })

  el.onclick = function() {
    if (vacshed_search_panel.style.display == 'none') {
      vacshed_search_panel.style.display = 'flex'}
    else {
      vacshed_search_panel.style.display = 'none'
    }
  }

}

function set_table_head(original, copy) {
  // установить фиксированную шапку таблицы
  original_table_th   = document.querySelectorAll('#' + original + ' th')
  copy_table_th       = document.querySelectorAll('#' + copy + ' thead th')

  i = 0

  for (const th of copy_table_th) {
    th.style.width = window.getComputedStyle(original_table_th[i]).width
    i++ 
  }

  document.getElementById(copy).style.width = window.getComputedStyle(document.getElementById(original)).width
  document.getElementById(copy).style.display = 'block'
}




