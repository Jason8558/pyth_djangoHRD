
function getemps() {
  dep = $('#id_dep option:selected').val()


  $.getJSON('/shift_shed/getemps/' + dep ,  (data) => {
    $('#id_emps').empty()

    for (var i = 0; i < data.length; i++) {

      $('#id_emps').append('<option value="' + data[i].id + '">' + data[i].fullname + ', ' + data[i].position__name + '</option>')


    }
  })
  // $(".chosen-select").chosen()
}

function add_emp_to_table() {
  val = $('#id_emps option:selected').val()
  text = $('#id_emps option:selected').text()
  $('#emps-table tbody').append('<tr id="' + val + '"><td class="emp_id">'+ val +'</td><td class="emp_fio">' + text + '</td><td><button type="button" class="button delete" onclick="del_emp_from_table('+ val +')">Удалить</button></td> </tr>')
}

function del_emp_from_table(id) {
  $('#emps-table tbody #' + id).remove()
}

function form_submit() {
  emps = $('.emp_id')
  for (var emp of emps) {
    console.log(emp);
    $('#id_emps_list').val(  $('#id_emps_list').val() + emp.innerText+',')
  }
}
