$(document).ready(function() {getvacshed()})


function getvacshed() {
  $.getJSON('/vacshed/getvacshed/2/',  (data) => {
    rowspan = 0
    for (var i = 0; i < data.length; i++) {

      $('.vs-table-create tbody').append(formrow(data[i].id, data[i].emp ,data[i].emp__fullname, data[i].emp__position__cat__name, data[i].dur_from, data[i].dur_to, data[i].days_count, data[i].move_from, data[i].move_to, data[i].days_count_move, data[i].child_year, data[i].city))


    }

    for (var i = 0; i < data.length; i++) {
      emp(data[i].id,data[i].emp)
    }

  })



}

function formrow(id, emp, emp__fullname, emp__position__cat__name, dur_from, dur_to, days_count, move_from, move_to, days_count_move, child_year, city){
  dur_from = dur_from.toString().split('-')
  dur_from = dur_from[2]+'.'+dur_from[1]+'.'+dur_from[0]

  dur_to = dur_to.toString().split('-')
  dur_to = dur_to[2]+'.'+dur_to[1]+'.'+dur_to[0]
  console.log(move_to);
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

  row = '<tr id="'+ id + '_' + emp + '"><td class="'+emp+'">' + emp__fullname + ' ' + emp__position__cat__name + '</td><td>' + dur_from + ' - ' + dur_to + '</td><td class="count_'+ emp + '">' + days_count + '</td><td>'+ move_from + ' - ' + move_to + '</td><td>'+ days_count_move +'</td><td class="totaldays'+emp+'"> </td><td>'+child_year+'</td><td>'+city+'</td></tr>'
  return row
}

function emp(rid,id){
  rows_emp = $('.' + id)
  tdays = $('.count_' + id)
  tcell = $('.totaldays' + id)
  console.log(tdays);
  length = rows_emp.length

  totaldays = 0

  if (length > 1) {
    for (var i = 1; i < length; i++) {
      rows_emp[0].rowSpan = rows_emp.length
      tcell[0].rowSpan = rows_emp.length
      rows_emp[0].parentElement.style.borderTop = '2px solid black'
      totaldays = totaldays + parseInt(tdays[i].innerText)

      rows_emp[i].remove()
      tcell[i].remove()
    }
    tcell[0].innerText = totaldays+parseInt(tdays[0].innerText)





  }
  else {
    rows_emp[0].parentElement.style.borderTop = '2px solid black'

  }



}
