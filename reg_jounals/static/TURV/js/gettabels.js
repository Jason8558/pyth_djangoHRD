function gettabels(type, access) {

  $.getJSON('/turv/gettabels/' + type,  (data) => {
    $('#tabels-main-table tbody').empty()



    for (var i = 0; i < data.length; i++) {



      if (data[i].del_check == true) {
        color = 'color: red;'
      }
      else {
        color = ''
      }


      if (access == 'True') {
        $('#tabels-main-table tbody').append('<tr style="'+color+'"><td>' + data[i].id + '</td><td class="table-type">' + data[i].type__name + '</td><td>' + month_to_str(data[i].month) + ' ' + data[i].year +  '</td><td>' + data[i].department__name + '</td><td>' + data[i].res_officer + '</td><td>' + true_false(data[i].paper_check) + '</td><td>' +  true_false(data[i].sup_check) + '</td><td>' + true_false(data[i].unloaded) + '</td><td>' + data[i].comm + '</td></tr>')
      }
      else {
        $('#tabels-main-table tbody').append('<trstyle="'+color+'"><td>' + data[i].id + '</td><td class="table-type">' + data[i].type__name + '</td><td>' +  month_to_str(data[i].month) + ' ' + data[i].year +  '</td><td>' + data[i].department__name + '</td><td>' + true_false(data[i].sup_check) + '</td><td>' + data[i].comm + '</td></tr>')
      }

    }
    rows = $('#tabels-main-table tbody tr')

    for (var i = 0; i < rows.length; i++) {

      url = "/" + "turv" + "/" + "create" + "/" + data[i].id + "')"
      click = " return window.open('" + url


      rows[i].setAttribute('onclick', click)
    }


  })

clear_all_inputs()

}

function month_to_str(month) {
switch (month) {
  case '01':
    month = 'Январь'
    return month
  break;

  case '02':
    month = 'Февраль'
    return month
  break;

  case '03':
    month = 'Март'
    return month
  break;

  case '04':
    month = 'Апрель'
    return month
  break;

  case '05':
    month = 'Май'
    return month
  break;

  case '06':
    month = 'Июнь'
    return month
  break;

  case '07':
    month = 'Июль'
    return month
  break;

  case '08':
    month = 'Август'
    return month
  break;

  case '09':
    month = 'Сентябрь'
    return month
  break;

  case '10':
    month = 'Октябрь'
    return month
  break;

  case '11':
    month = 'Ноябрь'
    return month
  break;

  case '12':
    month = 'Декабрь'
    return month
  break;


  default:

}
}

function true_false(boolean) {
    switch (boolean) {
    case true:
      boolean = '✅'
      return boolean
      break;

    case false:
      boolean = '❌'
      return boolean
      break;
    default:

  }

}

function gettabels_search(access) {

  baseurl = '/turv/gettabels/search/?'

  if ($('#search_month option:selected').val()) {
    baseurl = baseurl + '&search_month=' + $('#search_month option:selected').val()
  }

  if ($('#fs-year').val()) {
    baseurl = baseurl + '&search_year=' + $('#fs-year').val()
  }

  if ($('#search_code').val()) {
    baseurl = baseurl + '&search_code=' + $('#search_code').val()
  }

  if ($('#t_tab_dep_search option:selected').val()) {
    baseurl = baseurl + '&t_tab_dep_search=' + $('#t_tab_dep_search option:selected').val()
  }

  if ($('#search_type option:selected').val()) {
    baseurl = baseurl + '&search_type=' + $('#search_type option:selected').val()
  }

  if ($('#tab_user option:selected').val()) {

    tab_user = $('#tab_user option:selected').val().replace(' ', '+')

    baseurl = baseurl + '&tab_user=' + tab_user
  }




  $.getJSON(baseurl,  (data) => {
    $('#tabels-main-table tbody').empty()

    for (var i = 0; i < data.length; i++) {
      console.log(data[i].iscorr);
      if (data[i].iscorr == true) {
        iscorr = ' (корректировка)'
      }
      else {
        iscorr = ''
      }

      if (access == 'True') {
        $('#tabels-main-table tbody').append('<tr><td>' + data[i].id + '</td><td class="table-type">' + data[i].type__name + iscorr + '</td><td>' + month_to_str(data[i].month) + ' ' + data[i].year +  '</td><td>' + data[i].department__name + '</td><td>' + data[i].res_officer + '</td><td>' + true_false(data[i].paper_check) + '</td><td>' +  true_false(data[i].sup_check) + '</td><td>' + true_false(data[i].unloaded) + '</td><td>' + data[i].comm + '</td></tr>')
      }
      else {
        $('#tabels-main-table tbody').append('<tr><td>' + data[i].id + '</td><td class="table-type">' + data[i].type__name + iscorr + '</td><td>' +  month_to_str(data[i].month) + ' ' + data[i].year +  '</td><td>' + data[i].department__name + '</td><td>' + true_false(data[i].sup_check) + '</td><td>' + data[i].comm + '</td></tr>')
      }

    }
    rows = $('#tabels-main-table tbody tr')

    for (var i = 0; i < rows.length; i++) {

      url = "/" + "turv" + "/" + "create" + "/" + data[i].id + "')"
      click = " return window.open('" + url


      rows[i].setAttribute('onclick', click)
    }


  })

}

function clear_all_inputs() {



  inputs = $('.f_search input[type=text] ')

  for (var i of inputs) {
    i.value = ''
  }



}
