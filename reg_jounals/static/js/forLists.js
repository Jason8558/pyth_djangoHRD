
function TextDisabled() {

  var query = String(document.location.href).split('/');
  if (query[5] == 'add') {
    elem = document.getElementById('id_oov_empList').setAttribute('readonly', 'readonly');
  }
}


function FillList() {
  let form = document.forms[0];




  //добавляем позицию в список
  form.oov_empList.value = form.oov_empList.value + "\n" + "| " +  form.emp_name.value + " | " + form.emp_dep.value + " | c " + form.emp_dur_from.value + " по "+ form.emp_dur_to.value + " | " + " дней: " + form.emp_days.value  + " | " + form.emp_vacType.value + " | " + form.comm.value + "\n" + "---------------------------------------------------------------------------------------------------";

  //очищаем поля ввода
  form.emp_name.value = " ";
  form.emp_dep.value = " ";
  form.emp_dur_to.value =" ";
  form.emp_dur_from.value =" ";
  form.emp_days.value = " ";
  form.emp_vacType.value = " ";
  form.comm.value = " ";
}

function col_days() {

  let form = document.forms[0];
  if (form.emp_days.value == "") {



      var s_date1 = form.emp_dur_from.value;
      var year1 = s_date1.slice(6,10);
      var mount1 = s_date1.slice(3,5);
      var day1 = s_date1.slice(0,2);
      var f_date1 = year1 + ", " + mount1 + ", " + day1;

      var s_date2 = form.emp_dur_to.value;
      var year2 = s_date2.slice(6,10);
      var mount2 = s_date2.slice(3,5);
      var day2 = s_date2.slice(0,2);
      var f_date2 = year2 + ", " + mount2 + ", " + day2;


      let day_1 = new Date(f_date1),
          day_2 = new Date(f_date2);

      vac_days = (day_2 - day_1) / (60 * 60 * 24 * 1000);
      form.emp_days.value = Math.ceil(vac_days)+1; }
          }

  function duration() {
    let form = document.forms[0];
    var s_date1 = form.emp_dur_from.value;
    var year1 = s_date1.slice(6,10);
    var mount1 = s_date1.slice(3,5);
    var day1 = s_date1.slice(0,2);
    var f_date1 = year1 + "," + mount1 + "," + day1;
    let s_date = new Date(f_date1);
    let days = form.emp_days.value;
    days = days-1;
    var newDate = new Date(s_date.getTime() + (days * 24 * 60 * 60 * 1000) );



    year = newDate.getFullYear();
    month = newDate.getMonth();
    month = month + 1;
    month = padNum(month)

    day = newDate.getDate();
    day = padNum(day);

    function padNum(num) {
    return num.toString().padStart(2,0);
  };

    form.emp_dur_to.value = day + "." + month + "." + year





  }
