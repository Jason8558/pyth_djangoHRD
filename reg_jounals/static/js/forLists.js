

function FillList() {
  let form = document.forms[0];




  //добавляем позицию в список
  form.oov_empList.value = form.oov_empList.value + "\n" + "| " +  form.emp_name.value + " | " + form.emp_dep.value + " | c " + form.emp_dur_from.value + " по "+ form.emp_dur_to.value + " | " + form.emp_days.value + " дней" + " | " + form.emp_vacType.value + " | " + form.comm.value + "\n" + "---------------------------------------------------------------------------------------------------";

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

  var first = form.emp_dur_to.value;
  var sl_day = first.slice(0,2);
  var sl_mount = first.slice(2,4);
  var sl_year = first.slice(4,9);

  form.emp_dur_to.value = sl_day + "." + sl_mount + "." + sl_year


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
      form.emp_days.value = Math.ceil(vac_days);
          };
