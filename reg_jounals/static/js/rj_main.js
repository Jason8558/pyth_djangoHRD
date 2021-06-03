function vac_calc() {

date_from = $('#id_dur_from').val()
date_from_new = date_from.split('-')[2] + '.' + date_from.split('-')[1] + '.' + date_from.split('-')[0]

date_to = $('#id_dur_to').val()
date_to_new = date_to.split('-')[2] + '.' + date_to.split('-')[1] + '.' + date_to.split('-')[0]

dcount = (( Date.parse(date_to_new) - Date.parse(date_from_new)) / 24 / 60 / 60 / 1000) + 1

$('#id_days_count').val(dcount)

}

function duration() {
  date_from = $('#id_dur_from').val()
  date_from_new = date_from.split('-')[2] + '.' + date_from.split('-')[1] + '.' + date_from.split('-')[0]

  days = $('#id_days_count').val()

  date_to = Date.parse(date_from_new).addDays(parseInt(days, 10) - 1)

  $('#id_dur_to').val(date_to.toString('yyyy-MM-dd'))


}

function OpenSureDialog() {
  document.getElementById('sure_btn').style.display = "none";
  document.getElementById('sure').style.display = "block";
}
