function vac_calc() {

date_from = $('#id_dur_from').val()
date_from_new = date_from.split('-')[2] + '.' + date_from.split('-')[1] + '.' + date_from.split('-')[0]

date_to = $('#id_dur_to').val()
date_to_new = date_to.split('-')[2] + '.' + date_to.split('-')[1] + '.' + date_to.split('-')[0]

dcount = (( Date.parse(date_to_new) - Date.parse(date_from_new)) / 24 / 60 / 60 / 1000) + 1

$('#id_days_count').val(dcount)


$('#id_days_count2').val(dcount - 1)

}

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

function OpenSureDialog() {
  document.getElementById('sure_btn').style.display = "none";
  document.getElementById('sure').style.display = "block";
}

function check_doctype() {
  loc = document.location.href.split('/')[3]
  return loc
  // switch (loc) {
  //   case 'orders_on_others' :
  //       return 'orders_on_others'
  //     break;
  //     case 'orders_on_vacation_new' :
  //         return 'orders_on_vacation_new'
  //       break;
  //   default:
  //
  // }

  }


function check_act() {

  if ($('#iframe').attr('src').split('/')[2]== 'add' || $('#iframe').attr('src').split('/')[3]== 'addItem')  {
    return 'add'
  }
  if ($('#iframe').attr('src').split('/')[3]== 'edit' || $('#iframe').attr('src').split('/')[3]== 'upd' || $('#iframe').attr('src').split('/')[2]== 'updItem' )  {

    return 'upd'
  }
}

function open_frame_new() {
  console.log(check_doctype())
  switch (check_doctype()) {

    case 'orders_on_others':
      src = "/orders_on_others/add"

      break;
    case 'orders_on_vacation_new':
      src = "/orders_on_vacation_new/" + document.location.href.split('/')[4] + "/addItem"
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
    default:

  }

  $('#frame_').css('display','block')

  $('#iframe').attr('src', src)
console.log(check_act());

}

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

  default:

}



  $('#iframe').attr('src', request)
  $('#frame_').css('display','block')
  console.log(check_act());

}

function close_frame() {
  $('#frame_').css('display','none')
}

function send_submit() {
  // $('#iframe').contents().find('form').submit()
  res_officer = $('#uname').text()
  next_num = $('#iframe').contents().find("#next_num").text()
    switch (check_doctype()) {
      case 'orders_on_others':
      next_num = $('#iframe').contents().find("#next_num").text()
      date = Date.parse($('#iframe').contents().find("#doc_date").val()).toString('dd.MM.yyyy')

      content = $('#iframe').contents().find("#id_oom_content").val()

      if (check_act() == 'add') {

      $('tbody').prepend("<tr><td>" + date + "</td><td>" + next_num + "</td><td>" + content + "</td><td>"+ res_officer +"</td></tr>") }

      if (check_act() == 'upd') {
        id = $('#iframe').attr('src').split('/')[2]
        $("#" + id).find('#date').text(date)
        $("#" + id).find('#content').text(content)
      }
      break;

      case 'orders_on_vacation_new':

        name = $('#iframe').contents().find("#id_fio").val()
        dep = $('#iframe').contents().find("#id_dep option:selected").text()
        from = Date.parse($('#iframe').contents().find("#id_dur_from").val()).toString('dd.MM.yyyy')
        to = Date.parse($('#iframe').contents().find("#id_dur_to").val()).toString('dd.MM.yyyy')
        days = $('#iframe').contents().find("#id_days_count").val()
        type = $('#iframe').contents().find("#id_vac_type option:selected").val()
        comm = $('#iframe').contents().find("#id_comm").val()
                switch (check_act()) {
                  case 'add':
                        $('tbody').prepend("<tr><td>" + name + "</td><td>" + dep + "</td><td>" + from + "</td><td>"+ to +"</td><td>" + days + "</td><td>" + type + "</td><td>" + comm + "</td><td></td></tr>")
                    break;
                  case 'upd':
                      // console.log($('#iframe').attr('src').split('/'));
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
        date = Date.parse($('#iframe').contents().find("#id_doc_date").val()).toString('dd.MM.yyyy')
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

          next_id = $('tbody').find('tr').attr('id')
          next_id = parseInt(next_id, 10) + 1

          date = Date.parse($('#iframe').contents().find("#id_bt_date").val()).toString('dd.MM.yyyy')
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
          date = Date.parse($('#iframe').contents().find("#id_op_date").val()).toString('dd.MM.yyyy')
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

            }








    }


//   close_frame()
