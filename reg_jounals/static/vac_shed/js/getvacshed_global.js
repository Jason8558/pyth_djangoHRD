$(document).ready(function() {  $(".chosen-select").chosen()})




function comment_print_visible() {
  cells = $(".commentary")

  if ($("#set_comment_print")[0].checked) {

  for (const cell of cells) {
   
    cell.className += ' no-print'

  }
}

else {

  for (const cell of cells) {
    
    new_cn = cell.className.split(' ')[0]
    
    cell.className = new_cn

  }

}

}


function add_emp (){

  eid = $('#vs-glob-emp option:selected').val()
  ename = $('#vs-glob-emp option:selected').text()

  $('#vs-glob-emp-name').val($('#vs-glob-emp-name').val() + ename + '\n')
  $('#vs-glob-emp-id').val($('#vs-glob-emp-id').val() + eid + ',')


}


function getvacshed() {
  if ($('#vs-glob-emp-id').val) {
  $('#vs-glob-emp-id').val($('#vs-glob-emp-id').val().slice(0,-1))}

    $('#loading').css('display', '')
  year = $('#vs-glob-year').val()
  dep = $('#vs-glob-dep option:selected').val()
  dep_name = $('#vs-glob-dep option:selected').text()
  per = $('#vs-glob-per option:selected').val()
  emps = $('#vs-glob-emp-id').val()
  check = $('#vs-glob-fil option:selected').val()
  terr = $('#vs-glob-terr').val()
  pos = $('#vs-glob-pos').val()

  if (pos == '') {
    pos = 0
  }

  $('#comment_print_switch')[0].style.display = ""

  // if (check == true) {
  //   check = 1
  // }
  // else {
  //   check = 0
  // }

  //  if (!emps) {

document.title = 'График отпусков на ' + year + ' год'

  url = '?'

  // posuri = encodeURIComponent(document.getElementById('vs-glob-pos').value)
  
  url = url +
   '&vs-glob-year='      + document.getElementById('vs-glob-year').value +
   '&vs-glob-dep='       + document.getElementById('vs-glob-dep').value  +
   '&vs-glob-pos='       + document.getElementById('vs-glob-pos').value + 
   '&vs-glob-fil='       + document.getElementById('vs-glob-fil').value + 
   '&vs-glob-terr='      + document.getElementById('vs-glob-terr').value +
   '&vs-glob-per='       + document.getElementById('vs-glob-per').value + 
   '&vs-glob-emp-id='    + document.getElementById('vs-glob-emp-id').value 

  // url = url.replace('NaN', posuri)


  $('.vs-table-create tbody').empty()

  $.getJSON('/vacshed/global/new' + url,  (data) => {
    rowspan = 0
    for (var i = 0; i < data.length; i++) {

      $('.vs-table-create tbody').append(formrow(data[i].emp__department__name, data[i].emp__aup__name, data[i].id, data[i].emp ,data[i].emp__fullname, data[i].emp__position__name, data[i].dur_from, data[i].dur_to, data[i].days_count, data[i].move_from, data[i].move_to, data[i].days_count_move, data[i].child_year, data[i].city, data[i].comm))


    }

    for (var i = 0; i < data.length; i++) {
      emp(data[i].id,data[i].emp)
    }
    $('#loading').css('display', 'none')
    $('#vs-global-table').css('display', '')
  })
  // else {

  //   $('.vs-table-create tbody').empty()

  //   $.getJSON('/vacshed/global/' + year + '/' + dep + '/' + per + '/' + emps + '/0/0/0',  (data) => {
  //     rowspan = 0
  //     for (var i = 0; i < data.length; i++) {

  //       $('.vs-table-create tbody').append(formrow(data[i].emp__department__name, data[i].emp__aup__name, data[i].id, data[i].emp ,data[i].emp__fullname, data[i].emp__position__name, data[i].dur_from, data[i].dur_to, data[i].days_count, data[i].move_from, data[i].move_to, data[i].days_count_move, data[i].child_year, data[i].city, data[i].comm))


  //     }

  //     for (var i = 0; i < data.length; i++) {
  //       emp(data[i].id,data[i].emp)
  //     }
  //     $('#loading').css('display', 'none')
  //     $('#vs-global-table').css('display', '')
  //   })
  // }
emps_close()


}

function formrow(dep__name, aup__name, id, emp, emp__fullname, emp__position__name, dur_from, dur_to, days_count, move_from, move_to, days_count_move, child_year, city, comm){
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

  if (comm == null) {
    comm = ''
  }

  if (days_count_move == null) {
    days_count_move = ''
  }

  if (aup__name == null) {
    aup__name = ""
  }
  else {
    aup__name = "(" + aup__name + ")"
  }

    row = '<tr id="'+ id + '_' + emp + '"><td class="dep' + emp + '">' + dep__name + " " + aup__name + '</td><td class="emp '+emp+'">' + emp__fullname + ' ' + emp__position__name + '</td><td>' + dur_from + '</td><td class="count_'+ emp + '">' + days_count + '</td><td>'+ move_from  + '</td><td>'+ days_count_move +'</td><td class="commentary" id="' + id +'">'+comm+'</td><td class="totaldays'+emp+'">' + days_count +  '</td><td class="child' + emp + '">'+child_year+'</td><td class="city' + emp + '">'+city+'</td> <td class="print print-sign sign sign'+emp +'"></td></tr>'


  return row
}

function emp(rid,id){
  rows_emp = $('.' + id)
  tdays = $('.count_' + id)
  tcell = $('.totaldays' + id)
  tchild = $('.child' + id)
  tcity = $('.city' + id)
  tdep = $('.dep' + id)
  tsign = $('.sign' + id)

  length = rows_emp.length

  totaldays = 0

  if (length > 1) {
    for (var i = 1; i < length; i++) {
      rows_emp[0].rowSpan = rows_emp.length



      tcell[0].rowSpan = rows_emp.length
      tchild[0].rowSpan = rows_emp.length
      tcity[0].rowSpan = rows_emp.length
      tdep[0].rowSpan = rows_emp.length
      tsign[0].rowSpan = rows_emp.length
      // rows_emp[0].parentElement.style.borderTop = '2px solid black'
      totaldays = totaldays + parseInt(tdays[i].innerText)

      rows_emp[i].remove()
      tcell[i].remove()
      tcity[i].remove()
      tchild[i].remove()
      tdep[i].remove()
      tsign[i].remove()
    }
    tcell[0].innerText = totaldays+parseInt(tdays[0].innerText)

    for (var re of rows_emp) {
      if (re.rowSpan > 1) {
        re.parentNode.classList.add('main-row')
      }
    }



  }
  else {
    rows_emp[0].parentElement.style.borderTop = '2px solid black'

  }

if (dep != '0') {
  $('#ph-dep').text(dep_name)
}
else {
  $('#ph-dep').text('')
}

$('#ph-year').text(year)

}

function open_emps(){
  if ($('#vs-glob-emp-cont').css('display') == 'none') {
  $('#vs-glob-emp-cont').css('display', 'block')
  }
}

function emps_close(){
    $('#vs-glob-emp-cont').attr('style', 'display:none !important;')
}

