$(document).ready(function() {getvacshed()})


function getvacshed() {
  $.getJSON('/vacshed/getvacshed/2/',  (data) => {
    rowspan = 0
    for (var i = 0; i < data.length; i++) {

      $('.vs-table-create tbody').append(formrow(data[i].id, data[i].emp ,data[i].emp__fullname, data[i].dur_from, data[i].dur_to, data[i].days_count))


    }

    for (var i = 0; i < data.length; i++) {
      emp(data[i].id,data[i].emp)
    }

  })



}

function formrow(id, emp, emp__fullname, dur_from, dur_to, days_count){
  dur_from = dur_from.toString().split('-')
  dur_from = dur_from[2]+'.'+dur_from[1]+'.'+dur_from[0]

  dur_to = dur_to.toString().split('-')
  dur_to = dur_to[2]+'.'+dur_to[1]+'.'+dur_to[0]

  row = '<tr id="'+ id + '_' + emp + '"><td class="'+emp+'">' + emp__fullname + '</td><td>С ' + dur_from + ' по ' + dur_to + '</td><td class="count_'+ emp + '">' + days_count + '</td><td class="totaldays'+emp+'"> </td></tr>'
  return row
}

function emp(rid,id){
  rows_emp = $('.' + id)
  tdays = $('.count_' + id)
  tcell = $('.totaldays_' + id)
  console.log(tdays);
  length = rows_emp.length

  totaldays = 0

  if (length > 1) {
    for (var i = 1; i < length; i++) {
      rows_emp[0].rowSpan = rows_emp.length
      tcell[0].rowSpan = length
      rows_emp[0].parentElement.style.borderTop = '2px solid black'
      totaldays = totaldays + parseInt(tdays[i].innerText)

      rows_emp[i].remove()
    }
    console.log(totaldays+1);
    $('#' + rid + ' #totaldays').text()





  }
  else {
    rows_emp[0].parentElement.style.borderTop = '2px solid black'

  }



}
