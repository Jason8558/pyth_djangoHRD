// $(document).ready(function() {getvacshed()})


function getvacshed() {
  year = $('#vs-glob-year').val()
  dep = $('#vs-glob-dep option:selected').val()
  per = $('#vs-glob-per option:selected').val()

  $('.vs-table-create tbody').empty()

  $.getJSON('/vacshed/global/' + year + '/' + dep + '/' + per,  (data) => {
    rowspan = 0
    for (var i = 0; i < data.length; i++) {

      $('.vs-table-create tbody').append(formrow(data[i].bound_shed__dep__name, data[i].id, data[i].emp ,data[i].emp__fullname, data[i].emp__position__name, data[i].dur_from, data[i].dur_to, data[i].days_count, data[i].move_from, data[i].move_to, data[i].days_count_move, data[i].child_year, data[i].city))


    }

    for (var i = 0; i < data.length; i++) {
      emp(data[i].id,data[i].emp)
    }

  })



}

function formrow(dep__name, id, emp, emp__fullname, emp__position__name, dur_from, dur_to, days_count, move_from, move_to, days_count_move, child_year, city){
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

    row = '<tr id="'+ id + '_' + emp + '"><td class="dep' + emp + '">' + dep__name + '</td><td class="'+emp+'">' + emp__fullname + ' ' + emp__position__name + '</td><td>' + dur_from + '</td><td class="count_'+ emp + '">' + days_count + '</td><td>'+ move_from  + '</td><td>'+ days_count_move +'</td><td class="totaldays'+emp+'"> </td><td class="child' + emp + '">'+child_year+'</td><td class="city' + emp + '">'+city+'</td></tr>'


  return row
}

function emp(rid,id){
  rows_emp = $('.' + id)
  tdays = $('.count_' + id)
  tcell = $('.totaldays' + id)
  tchild = $('.child' + id)
  tcity = $('.city' + id)
  tdep = $('.dep' + id)
  console.log(tdays);
  length = rows_emp.length
console.log(length);
  totaldays = 0
  console.log(id + " " + length);
  if (length > 1) {
    for (var i = 1; i < length; i++) {
      rows_emp[0].rowSpan = rows_emp.length
      tcell[0].rowSpan = rows_emp.length
      tchild[0].rowSpan = rows_emp.length
      tcity[0].rowSpan = rows_emp.length
      tdep[0].rowSpan = rows_emp.length
      rows_emp[0].parentElement.style.borderTop = '2px solid black'
      totaldays = totaldays + parseInt(tdays[i].innerText)

      rows_emp[i].remove()
      tcell[i].remove()
      tcity[i].remove()
      tchild[i].remove()
      tdep[i].remove()
    }
    tcell[0].innerText = totaldays+parseInt(tdays[0].innerText)





  }
  else {
    rows_emp[0].parentElement.style.borderTop = '2px solid black'
    // tcell[0].innerText = tdays[0].innerText

  }



}
