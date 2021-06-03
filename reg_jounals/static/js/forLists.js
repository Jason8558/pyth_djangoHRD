function CreateList () {
loc = '/journals/sick_list/create/' + document.getElementById('id_sk_number').value.toString();
alert(loc)
location.href = loc;

}

function ClearEnter() {

    document.getElementById('id_sk_number').setAttribute('readonly', 'readonly');
    document.getElementById('id_sk_rumber').value = "";
    document.getElementById('id_sk_emp').value = "";
    document.getElementById('id_sk_pos').value = "";
    document.getElementById('id_sk_dur_from').value = "";
    document.getElementById('id_sk_dur_to').value = "";
    document.getElementById('id_sk_comm').value = "";

}

function OpenSureDialog() {
  document.getElementById('sure_btn').style.display = "none";
  document.getElementById('sure').style.display = "block";
}


function TextDisabled() {

  var query = String(document.location.href).split('/');
  if (query[5] == 'add') {
    elem = document.getElementById('id_oov_empList').setAttribute('readonly', 'readonly');
  };

  if (query[5] == 'Itemadd') {
  document.getElementById('id_sk_number').value = query[6];
}

}


function FillList() {
  let form = document.forms[0];

var vac_from = form.dur_from.value;
var v_year_from = vac_from.slice(0,4);
var v_mount_from = vac_from.slice(6,7);
var v_day_from = vac_from.slice(8,10);
if (v_mount_from.length < 2) {
v_mount_from = "0" + v_mount_from;

}

vac_from = v_day_from + "." + v_mount_from + "." + v_year_from

var vac_to = form.dur_to.value;
var v_year_to = vac_to.slice(0,4);
var v_mount_to = vac_to.slice(6,7);
var v_day_to = vac_to.slice(8,10);
if (v_mount_to.length < 2) {
v_mount_to = "0" + v_mount_to;

}

vac_to = v_day_to + "." + v_mount_to + "." + v_year_to


  //добавляем позицию в список
  form.oov_empList.value = form.oov_empList.value + "\n" + "| " +  form.emp_name.value + " | " + form.emp_dep.value + " | c " + vac_from + " по "+ vac_to + " | " + " дней: " + form.days_count.value  + " | " + form.emp_vacType.value + " | " + form.comm.value + "\n" + "---------------------------------------------------------------------------------------------------";

  //очищаем поля ввода
  form.emp_name.value = " ";
  form.emp_dep.value = " ";
  form.dur_to.value =" ";
  form.dur_from.value =" ";
  form.days_count.value = " ";
  form.emp_vacType.value = " ";
  form.comm.value = " ";
}

function col_days() {

  let form = document.forms[0];
  if (form.days_count.value == "") {



      var s_date1 = form.dur_from.value;
      console.log(s_date1)
      var year1 = s_date1.slice(0,4);
      var mount1 = s_date1.slice(6,7);
      var day1 = s_date1.slice(8,10);
      var f_date1 = year1 + ", " + mount1 + ", " + day1;
      console.log(f_date1)

      var s_date2 = form.dur_to.value;
      console.log(s_date2)
      var year2 = s_date2.slice(0,4);
      var mount2 = s_date2.slice(6,7);
      var day2 = s_date2.slice(8,10);
      var f_date2 = year2 + ", " + mount2 + ", " + day2;
      console.log(f_date2)

      let day_1 = new Date(f_date1),
          day_2 = new Date(f_date2);

      console.log("c" + day_1 + "по" + day_2)

      vac_days = (day_2 - day_1) / (60 * 60 * 24 * 1000);
      form.days_count.value = Math.ceil(vac_days)+1; }
          }

  // function duration() {
  //   let form = document.forms[0];
  //   var s_date1 = form.dur_from.value;
  //   var year1 = s_date1.slice(0,4);
  //   var mount1 = s_date1.slice(6,7);
  //   var day1 = s_date1.slice(8,10);
  //   var f_date1 = year1 + "," + mount1 + "," + day1;
  //   let s_date = new Date(f_date1);
  //   let days = form.days_count.value;
  //   days = days-1;
  //   var newDate = new Date(s_date.getTime() + (days * 24 * 60 * 60 * 1000) );
  //
  //
  //
  //   year = newDate.getFullYear();
  //   month = newDate.getMonth();
  //   month = month + 1;
  //   month = padNum(month)
  //
  //   day = newDate.getDate();
  //   day = padNum(day);
  //
  //   function padNum(num) {
  //   return num.toString().padStart(2,0);
  // };
  //
  //   form.dur_to.value = year + "-" + month + "-" + day
  //
  //
  //
  //
  //
  // }
