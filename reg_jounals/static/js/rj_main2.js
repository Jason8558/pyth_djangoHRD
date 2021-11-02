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

// Проверка вида документа ---------------------------------------------------------------------------------
function check_doctype() {

  loc = document.location.href.split('/')[3]
  console.log(loc + " " + document.location.href.split('/').length );
  if (loc == 'orders_on_vacation_new' && document.location.href.split('/').length == 5) {

      return 'orders_on_vacation_new_add'

  }
  else {
    return loc
  }



  }
// =========================================================================================================

// Проверка действия над документом ------------------------------------------------------------------------
function check_act() {

  if ($('#iframe').attr('src').split('/')[2]== 'add' || $('#iframe').attr('src').split('/')[3]== 'addItem' || $('#iframe').attr('src').split('/')[5]== 'addItem' )  {
    return 'add'
  }
  if ($('#iframe').attr('src').split('/')[3]== 'edit' || $('#iframe').attr('src').split('/')[3]== 'upd' || $('#iframe').attr('src').split('/')[2]== 'upd' || $('#iframe').attr('src').split('/')[2]== 'updItem' )  {

    return 'upd'
  }
}
// =========================================================================================================

// Открытие диалогового окна при добавлении документа ------------------------------------------------------
function open_frame_new() {
  console.log(check_doctype())
  switch (check_doctype()) {

    case 'orders_on_others':
      src = "/orders_on_others/add"

      break;
    case 'orders_on_vacation_new':
      src = "/orders_on_vacation_new/" + document.location.href.split('/')[4] + "/addItem"
      break;

    case 'orders_on_vacation_new_add':
      src = "/orders_on_vacation_new/add"
      break;

    case 'outbound_docs':
      src = "/outbound_docs/add"
      break;

    case 'orders_of_BTrip':
      src = "/orders_of_BTrip/add"
      break;

    case 'orders_on_personnel':
      src = "/orders_on_personnel/add"
      break;

    case 'laborContracts':
      src = "/laborContracts/add"
      break;

    case 'letters_of_resignation':
      src = "/letters_of_resignation/add"
      break;

    case 'letters_of_invite':
      src = "/letters_of_invite/add"
      break;

    case 'employment_history':
      src = "/employment_history/add"
      break;

    case 'sick_reg':
      src = "/sick_reg/" + document.location.href.split('/')[4] + "/addItem"
      break;

    case 'identity':
      src = "/identity/add"
      break;
    default:

  }

  $('#frame_').css('display','block')
  setTimeout(function(){
    $('#frame_').css('opacity','initial');
  }, 250);

  $('#iframe').attr('src', src)
console.log(check_act());

}
// =========================================================================================================

// Открытие диалогового окна при изменении документа -------------------------------------------------------
function open_for_upd(id) {
switch (check_doctype()) {
  case 'orders_on_others':
    request = "/orders_on_others/"+ id + "/edit"
    break;

  case 'orders_on_vacation_new':
    request = "/orders_on_vacation_new/updItem/" + id
    break;

  case 'outbound_docs':
    request = "/outbound_docs/" + id + "/edit"
    break;

    case 'orders_of_BTrip':
      request = "/orders_of_BTrip/" + id + "/upd"
      break;

    case 'orders_on_personnel':
      request = "/orders_on_personnel/" + id + "/upd"
      break;

    case 'laborContracts':
      request = "/laborContracts/" + id + "/upd"
      break;

    case 'letters_of_resignation':
      request = "/letters_of_resignation/" + id + "/edit"
      break;

    case 'letters_of_invite':
      request = "/letters_of_invite/"+ id + "/edit"
      break;

    case 'employment_history':
      request = "/employment_history/"+ id + "/upd"
      break;

    case 'sick_reg':
      request = "/sick_reg/updItem/" + id
      break;

    case 'identity':
      request = "/identity/upd/" + id
      break;
  default:

}



  $('#iframe').attr('src', request)
  $('#frame_').css('display','block')
  setTimeout(function(){
    $('#frame_').css('opacity','initial');
  }, 250);
  console.log(check_act());

}
// =========================================================================================================

// Закрытие диалогового окна -------------------------------------------------------------------------------
function close_frame() {
$('#frame_').css('opacity','0');
  setTimeout(function(){
    $('#frame_').css('display','none')
  }, 300);
}
// =========================================================================================================

// Процедура добавления\изменения документа в бд и интерфейсе ----------------------------------------------
function send_submit() {
  next_id = $('tbody').find('tr').attr('id')
  next_id = parseInt(next_id, 10) + 1
  res_officer = $('#uname').text()
  next_num = $('#iframe').contents().find("#next_num").text()
    switch (check_doctype()) {
      case 'orders_on_others':
      next_num = $('#iframe').contents().find("#next_num").text()
      date = $('#iframe').contents().find("#doc_date").val().split("-")
      date = date[2] + "." + date[1] + "." + date[0]

      content = $('#iframe').contents().find("#id_oom_content").val()

      if (check_act() == 'add') {

      $('tbody').prepend("<tr><td>" + date + "</td><td>" + next_num + "</td><td>" + content + "</td><td>"+ res_officer +"</td></tr>") }

      if (check_act() == 'upd') {
        id = $('#iframe').attr('src').split('/')[2]
        $("#" + id).find('#date').text(date)
        $("#" + id).find('#content').text(content)
      }
      break;

      case 'orders_on_vacation_new_add':
        date = $('#iframe').contents().find("#id_order_date").val().split("-")
        date = date[2] + "." + date[1] + "." + date[0]

        if (check_act() == 'add') {
          onclick_string = ''
onclick_string = " '/orders_on_vacation_new/" + next_id + "/create'" + ">"

$('tbody').prepend("<tr id='" + next_id + "'" + "onclick" + "=" + " return location.href" + "=" + onclick_string + "<td>" + date + "</td><td>" + next_num + "</td><td>" + res_officer + "</td></tr>")
var url = "/orders_on_vacation_new/" + next_id + "/create";
setTimeout(function(){
$(location).attr('href',url);}, 250)
}



      break;

      case 'orders_on_vacation_new':

        name = $('#iframe').contents().find("#id_fio").val()
        dep = $('#iframe').contents().find("#id_dep option:selected").text()
        from = $('#iframe').contents().find("#id_dur_from").val().split("-")
        from = from[2] + "." + from[1] + "." + from[0]
        to = $('#iframe').contents().find("#id_dur_to").val().split("-")
        to = to[2] + "." + to[1] + "." + to[0]
        days = $('#iframe').contents().find("#id_days_count").val()
        type = $('#iframe').contents().find("#id_vac_type option:selected").val()
        comm = $('#iframe').contents().find("#id_comm").val()

                switch (check_act()) {

                  case 'add':
                        if ($('table').is('.vac_table')) {
                          $('tbody').prepend("<tr><td>" + name + "</td><td>" + dep + "</td><td>" + from + "</td><td>"+ to +"</td><td>" + days + "</td><td>" + type + "</td><td>" + comm + "</td><td></td></tr>")
                        }
                        else {
                          $('#btn-add').before('<table class="vac_table"><thead class="thead-dark"><thead class="thead-dark"><tr class="tr-header"><th scope="col">ФИО</th><th scope="col">Подразделение</th><th scope="col">Дата начала</th><th scope="col">Дата окончания</th><th scope="col">Дней отпуска</th><th scope="col">Вид отпуска</th><th scope="col">Примечание</th><th scope="col"></th></tr></thead><tbody></tbody></table>')
                          $('tbody').prepend("<tr><td>" + name + "</td><td>" + dep + "</td><td>" + from + "</td><td>"+ to +"</td><td>" + days + "</td><td>" + type + "</td><td>" + comm + "</td><td></td></tr>")
                        }

                    break;
                  case 'upd':
                      console.log(from);
                      id = $('#iframe').attr('src').split('/')[3]
                      $("#" + id).find('#name').text(name)
                      $("#" + id).find('#dep').text(dep)
                      $("#" + id).find('#from').text(from)
                      $("#" + id).find('#to').text(to)
                      $("#" + id).find('#days').text(days)
                      $("#" + id).find('#type').text(type)
                      $("#" + id).find('#comm').text(comm)
                      break;
                  default:

                }
      break;

      case 'outbound_docs':
        type = $('#iframe').contents().find("#id_doc_type").val()
        date = $('#iframe').contents().find("#id_doc_date").val().split("-")
        date = date[2] + "." + date[1] + "." + date[0]
        dest = $('#iframe').contents().find("#id_doc_dest").val()
        content = $('#iframe').contents().find("#id_doc_additionalData").val()
        next_num = $('#iframe').contents().find("#next_num").text()
            switch (check_act()) {
              case 'add':
                    $('tbody').prepend("<tr><td>" + date + "</td><td>" + next_num + "</td><td>" + type + "</td><td>"+ dest +"</td><td>" + content + "</td><td>" + res_officer + "</td></tr>")
                break;
              case 'upd':

              id = $('#iframe').attr('src').split('/')[2]
              $("#" + id).find('#date').text(date)
                $("#" + id).find('#type').text(type)
                $("#" + id).find('#dest').text(dest)
              $("#" + id).find('#content').text(content)
              break;}

      break;

      case 'orders_of_BTrip':



          date = $('#iframe').contents().find("#id_bt_date").val().split("-")
          date = date[2] + "." + date[1] + "." + date[0]
          fio = $('#iframe').contents().find("#id_bt_emloyer").val()
          place = $('#iframe').contents().find("#id_bt_place").val()
          dep = $('#iframe').contents().find("#id_bt_dep option:selected").text()

            switch (check_act()) {
              case 'add':
                    $('tbody').prepend("<tr id="+ next_id + " onclick='open_for_upd("+ next_id +")'><td>" + date + "</td><td>" + next_num + "</td><td>" + place + "</td><td>"+ fio +"</td><td>" + dep + "</td><td>" + res_officer + "</td></tr>")
                break;
            case 'upd':

                  id = $('#iframe').attr('src').split('/')[2]
                  $("#" + id).find('#date').text(date)
                  $("#" + id).find('#place').text(place)
                  $("#" + id).find('#employer').text(fio)
                  $("#" + id).find('#dep').text(dep)

                  break;








            }
      break;

      case 'orders_on_personnel':
          next_id = $('tbody').find('tr').attr('id')
          next_id = parseInt(next_id, 10) + 1
          date = $('#iframe').contents().find("#id_op_date").val().split("-")
          date = date[2] + "." + date[1] + "." + date[0]
          fio = $('#iframe').contents().find("#id_op_emloyer").val()
          dep = $('#iframe').contents().find("#id_op_dep option:selected").text()
          content =  $('#iframe').contents().find("#id_op_content").val()
              switch (check_act()) {
                case 'add':
                      $('tbody').prepend("<tr id="+ next_id + " ondblclick='open_for_upd("+ next_id +")' class='t_row'><td><input type='checkbox' class='for_print' name='forprint' value=''></td><td>" + date + "</td><td>" + next_num + "</td><td>" + fio + "</td><td>"+ dep +"</td><td>" + content + "</td><td>" + res_officer + "</td></tr>")
                  break;
                case 'upd':
                    // console.log($('#iframe').attr('src').split('/'));
                    id = $('#iframe').attr('src').split('/')[2]
                    $("#" + id).find('#date').text(date)
                    $("#" + id).find('#emloyer').text(fio)
                    $("#" + id).find('#dep').text(dep)
                    $("#" + id).find('#content').text(content)

                  break;
                  }
      break;

      case 'laborContracts':
          date = $('#iframe').contents().find("#id_lc_date").val().split("-")
          date = date[2] + "." + date[1] + "." + date[0]
          dateInv = $('#iframe').contents().find("#id_lc_dateOfInv").val().split("-")
          dateinv = dateinv[2] + "." + dateinv[1] + "." + dateinv[0]
          fio = $('#iframe').contents().find("#id_lc_emloyer").val()
          pos = $('#iframe').contents().find("#id_lc_pos").val()
          dep = $('#iframe').contents().find("#id_lc_dep option:selected").text()
          thisyear = Date.today().toString("yy")

              switch (check_act()) {
                case 'add':
                      $('tbody').prepend("<tr id="+ next_id + " onclick='open_for_upd("+ next_id +")'><td>" + date + "</td><td>" + next_num + "(" + thisyear + ")" + "</td><td>" + fio + "</td><td>"+ dep +"</td><td>" + dateInv + "</td><td>" + res_officer + "</td></tr>")
                  break;
              case 'upd':
                    console.log($('#iframe').attr('src').split('/')[2]);
                    id = $('#iframe').attr('src').split('/')[2]
                    $("#" + id).find('#date').text(date)
                    $("#" + id).find('#emloyer').text(fio)
                    $("#" + id).find('#dep').text(dep)
                    $("#" + id).find('#dateInv').text(dateInv)

                    break;


            }
      break;

      case 'letters_of_resignation':
          date = $('#iframe').contents().find("#id_lor_date").val().split("-")
          date = date[2] + "." + date[1] + "." + date[0]
          fio = $('#iframe').contents().find("#id_lor_employee").val()
          pos = $('#iframe').contents().find("#id_lor_position").val()
          dep =  $('#iframe').contents().find("#id_lor_departament option:selected").text()
          if ($('#iframe').contents().find("#id_lor_dateOfRes").val()) {
            dateofres = $('#iframe').contents().find("#id_lor_dateOfRes").val().split("-")
            dateofres = dateofres[2] + "." + dateofres[1] + "." + dateofres[0]
          }
            else {
              dateofres = ""
            }
          content = $('#iframe').contents().find("#id_lor_additionalData").val()
              switch (check_act()) {
                case 'add':
                      $('tbody').prepend("<tr id="+ next_id + " onclick='open_for_upd("+ next_id +")'><td>" + next_num + "</td><td>" + date +  "</td><td>" + fio + "</td><td>"+ pos +"</td><td>" + dep + "</td><td>" + dateofres + "</td><td>" + content +"</td><td>"+ res_officer +"</td></tr>")
                  break;
              case 'upd':
                    console.log($('#iframe').attr('src').split('/'));
                    id = $('#iframe').attr('src').split('/')[2]
                    $("#" + id).find('#date').text(date)
                    $("#" + id).find('#emloyer').text(fio)
                    $("#" + id).find('#dep').text(dep)
                    $("#" + id).find('#dateRes').text(dateofres)
                    $("#" + id).find('#content').text(content)

                    break;


            }


      break;

      case 'letters_of_invite':
          date = $('#iframe').contents().find("#id_loi_date").val().split("-")
          date = date[2] + "." + date[1] + "." + date[0]
          fio = $('#iframe').contents().find("#id_loi_employee").val()
          pos = $('#iframe').contents().find("#id_loi_position").val()
          dep =  $('#iframe').contents().find("#id_loi_department option:selected").text()
          if ($('#iframe').contents().find("#id_loi_dateOfInv").val()) {
            dateofinv = $('#iframe').contents().find("#id_loi_dateOfInv").val().split("-")
            dateofinv = dateofinv[2] + "." + dateofinv[1] + "." + dateofinv[0]
          }
            else {
              dateofinv = ""
            }
            switch (check_act()) {
              case 'add':
                    $('tbody').prepend("<tr id="+ next_id + " onclick='open_for_upd("+ next_id +")'><td>" + next_num + "</td><td>" + date +  "</td><td>" + fio + "</td><td>"+ pos +"</td><td>" + dep + "</td><td>" + dateofinv + "</td><td>"+ res_officer +"</td></tr>")
                break;
            case 'upd':
                  console.log($('#iframe').attr('src').split('/'));
                  id = $('#iframe').attr('src').split('/')[2]
                  $("#" + id).find('#date').text(date)
                  $("#" + id).find('#emloyer').text(fio)
                  $("#" + id).find('#dep').text(dep)
                  $("#" + id).find('#dateofinv').text(dateofinv)
                  $("#" + id).find('#pos').text(pos)

                  break;            }

      break;

      case 'employment_history':
          number = $('#iframe').contents().find("#id_eh_number").val()
          dateofinv = $('#iframe').contents().find("#id_eh_dateOfInv").val().split("-")
          dateofinv = dateofinv[2] + "." + dateofinv[1] + "." + dateofinv[0]
          if ($('#iframe').contents().find("#id_eh_dateOfResign").val()) {
            dateofres = $('#iframe').contents().find("#id_eh_dateOfResign").val().split("-")
            dateofres = dateofres[2] + "." + dateofres[1] + "." + dateofres[0]
          }
          else {
            dateofres = ""
          }
          fio = $('#iframe').contents().find("#id_eh_employer").val()
          pos = $('#iframe').contents().find("#id_eh_pos").val()
          dep = $('#iframe').contents().find("#id_eh_dep option:selected").text()
          inviteorder = $('#iframe').contents().find("#id_eh_OrderInv").val()
          resignorder = $('#iframe').contents().find("#id_eh_OrderResign").val()
          switch (check_act()) {
            case 'add':
                  $('tbody').prepend("<tr id="+ next_id + " onclick='open_for_upd("+ next_id +")'><td>" + number + "</td><td>" + dateofinv +  "</td><td>" + fio + "</td><td>"+ dep +"</td><td>" + pos + "</td><td>" + inviteorder + "</td><td>"+  dateofres + "</td><td>" + resignorder + "</td><td>"+  res_officer +"</td></tr>")
              break;
          case 'upd':
                console.log($('#iframe').attr('src').split('/'));
                id = $('#iframe').attr('src').split('/')[2]
                $("#" + id).find('#number').text(number)
                $("#" + id).find('#fio').text(fio)
                $("#" + id).find('#dateofinv').text(dateofinv)
                $("#" + id).find('#dep').text(dep)
                $("#" + id).find('#pos').text(pos)
                $("#" + id).find('#orderinv').text(inviteorder)
                $("#" + id).find('#orderres').text(resignorder)
                $("#" + id).find('#dateofresign').text(dateofres)

                break;            }
      break;

      case 'sick_reg':
          number = $('#iframe').contents().find("#id_sd_number").val()
          fio = $('#iframe').contents().find("#id_sd_emp").val()
          pos = $('#iframe').contents().find("#id_sd_pos").val()
          dep = $('#iframe').contents().find("#id_sd_dep option:selected").text()
          from = $('#iframe').contents().find("#id_sd_dur_from").val().split("-")
          from = from[2] + "." + from[1] + "." + from[0]
          if ($('#iframe').contents().find("#id_sd_dur_to").val()) {
            to = $('#iframe').contents().find("#id_sd_dur_to").val().split("-")
            to = to[2] + "." + to[1] + "." + to[0]
          }
          else {
            to = ""
          }
          comm = $('#iframe').contents().find("#id_sd_comm").val()

          switch (check_act()) {
            case 'add':
            setTimeout(function(){
            if ($('#iframe').contents().find('div').is('#form_error')) {
              console.log('есть ошибки!');
            }
            else {

                    $('tbody').prepend("<tr id="+ next_id + " onclick='open_for_upd("+ next_id +")'><td>" + number + "</td><td>" + fio +  "</td><td>" + pos + "</td><td>"+ dep +"</td><td>" + from + "</td><td>" + to + "</td><td>"+  comm + "</td><td></td></tr>")
            }
            }, 500)

              break;
          case 'upd':
                console.log($('#iframe').attr('src').split('/'));
                id = $('#iframe').attr('src').split('/')[3]

                $("#" + id).find('#number').text(number)
                $("#" + id).find('#fio').text(fio)
                $("#" + id).find('#pos').text(pos)
                $("#" + id).find('#dep').text(dep)
                $("#" + id).find('#from').text(from)
                $("#" + id).find('#to').text(to)


                break;            }
      break;

      case 'identity':
          date = $('#iframe').contents().find("#id_date_giving").val().split("-")
          date = date[2] + "." + date[1] + "." + date[0]
          fio = $('#iframe').contents().find("#id_employer").val()
          dep = $('#iframe').contents().find("#id_department option:selected").text()
          switch (check_act()) {
            case 'add':
                  $('tbody').prepend("<tr id="+ next_id + " onclick='open_for_upd("+ next_id +")'><td>" + next_num + "</td><td>" + date +  "</td><td>" + fio + "</td><td>"+ dep +"</td><td>" + res_officer +"</td></tr>")
              break;
          case 'upd':
                console.log($('#iframe').attr('src').split('/'));
                id = $('#iframe').attr('src').split('/')[3]
                $("#" + id).find('#date').text(date)
                $("#" + id).find('#emloyer').text(fio)
                $("#" + id).find('#dep').text(dep)


                break;            }
      break;






    }
    // Делаем сабмит, закрываем форму -----------
$('#iframe').contents().find('form').submit()
setTimeout(function(){
if ($('#iframe').contents().find('div').is('#form_error')) {
  console.log('есть ошибки!');
}
else {

    close_frame()
}
}, 500)



    // ------------------------------------------
}
// =========================================================================================================
