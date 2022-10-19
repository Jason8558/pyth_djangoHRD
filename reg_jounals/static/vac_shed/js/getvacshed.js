// $(document).ready(function() {getvacshed()})



function getvacshed(granted,check) {
  id = document.location.href.split('/')[5]

  $.getJSON('/vacshed/getvacshed/' + id + '/',  (data) => {
    rowspan = 0
    for (var i = 0; i < data.length; i++) {

      $('.vs-table-create tbody').append(formrow(data[i].id, data[i].emp ,data[i].emp__fullname, data[i].emp__position__name, data[i].dur_from, data[i].dur_to, data[i].days_count, data[i].move_from, data[i].move_to, data[i].move_reason, data[i].days_count_move, data[i].child_year, data[i].city, granted))


    }

    for (var i = 0; i < data.length; i++) {
      emp(data[i].id,data[i].emp,check,granted)
    }

  })



}

function formrow(id, emp, emp__fullname, emp__position__name, dur_from, dur_to, days_count, move_from, move_to, move_reason, days_count_move, child_year, city, granted){
  dur_from = dur_from.toString().split('-')
  dur_from = dur_from[2]+'.'+dur_from[1]+'.'+dur_from[0]

  dur_to = dur_to.toString().split('-')
  dur_to = dur_to[2]+'.'+dur_to[1]+'.'+dur_to[0]

  if (move_from == null) {
    move_from = ''
  }
  else {
    move_from = move_from.toString().split('-')
    move_from = move_from[2]+'.'+move_from[1]+'.'+move_from[0]
  }

  if (move_to == null) {
    move_to = ''
  }
  else {
    move_to = move_to.toString().split('-')
    move_to = move_to[2]+'.'+move_to[1]+'.'+move_to[0]
  }

  if (days_count_move == null) {
    days_count_move = ''
  }

  if (move_reason == null) {
    move_reason = ''
  }






  if (granted == 0) {
    row = '<tr class="vs_row" id="'+ id + '_' + emp + '"><td class="emp '+emp+'">' + emp__fullname + ' | ' + emp__position__name + '</td><td id="durfrom_'+ id +'_' + emp + '">' + dur_from + '</td><td class="count_'+ emp + '">' + days_count + '</td><td class="totaldays'+emp+'"> </td><td class="child' + emp + '">'+child_year+'</td><td id="city_'+ id + '" class="city city' + emp + '">'+city+'</td><td class="not-print sign sign'+ emp +'"></td></tr>'
  }
  else {
    row = '<tr class="vs_row" id="'+ id + '_' + emp + '"><td class="emp '+emp+'">' + emp__fullname + ' | ' + emp__position__name + '</td><td id="durfrom_' + id + '_' + emp + '">' + dur_from + '</td><td class="count_'+ emp + '">' + days_count + '</td><td id="movefrom' + id + '" class="movefrom">'+ move_from + ' - ' + move_reason + '</td><td class="movecount_'+ emp +'">'+ days_count_move +'</td><td class="totaldays'+emp+'"> </td><td class="child' + emp + '">'+child_year+'</td><td id="city_'+ id + '" class="city city' + emp + '">'+city+'</td><td class="not-print sign  sign'+ emp +'"></td></tr>'
  }

  return row
}

function emp(rid,id,check,granted){
  rows_emp = $('.' + id)
  tdays = $('.count_' + id)
  tmovedays = $('.movecount_' + id)
  tcell = $('.totaldays' + id)
  tchild = $('.child' + id)
  tcity = $('.city' + id)
  tsign = $('.sign' + id)

  length = rows_emp.length

  totaldays = 0

  if (length > 1) {
    for (var i = 1; i < length; i++) {
      rows_emp[0].rowSpan = rows_emp.length
      tcell[0].rowSpan = rows_emp.length
      tchild[0].rowSpan = rows_emp.length
      tcity[0].rowSpan = rows_emp.length
      tsign[0].rowSpan = rows_emp.length
      rows_emp[0].parentElement.style.borderTop = '2px solid black'
      totaldays = totaldays + parseInt(tdays[i].innerText)

      if (tmovedays[i].innerText) {
        totaldays = totaldays - parseInt(tdays[i].innerText)
        totaldays = totaldays + parseInt(tmovedays[i].innerText)
      }



      rows_emp[i].remove()
      tcell[i].remove()
      tcity[i].remove()
      tchild[i].remove()
      tsign[i].remove()
    }



    tcell[0].innerText = totaldays+parseInt(tdays[0].innerText)
    if (tmovedays[0].innerText) {
    tcell[0].innerText = totaldays+parseInt(tmovedays[0].innerText)}





  }
  else {
    rows_emp[0].parentElement.style.borderTop = '2px solid black'
    // tcell[0].innerText = tdays[0].innerText

  }
if (check == 'True' && granted == 0) {
  unset_onclick()
}
else {
  set_onclick()
}


}

function set_onclick() {


  rows = $('.vs_row')

  for (var r of rows) {
    id = r.id.split('_')[0]


    url = "/" + "vacshed" + "/" + "itemupd" + "/" + id + "/2'"
    click = "location.href = '" + url

    url2 = "/" + "vacshed" + "/" + "itemupd" + "/" + id + "/1'"
    click2 = "location.href = '" + url2

    url3 = "/" + "vacshed" + "/" + "itemupd" + "/" + id + "/3'"
    click3 = "location.href = '" + url3

    $('#durfrom_' + r.id).attr('onclick', click)
    $('#city_' + id).attr('onclick', click2)
    $('#movefrom' + id).attr('onclick', click3)
  }
}

function unset_onclick() {
  console.log('1l');
  rows = $('.vs_row')

  for (var r of rows) {
    id = r.id.split('_')[0]

    $('#durfrom_' + r.id).attr('onclick', ' ')
    $('#city_' + id).attr('onclick', ' ')
  }
}
