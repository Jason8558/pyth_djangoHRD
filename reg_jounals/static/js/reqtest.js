
function open_frame() {
  $('#iframe').attr("src", "/sick_reg/268/addItem")
  $('#iframe').attr('display','block')
}



function send_request() {
  sd_number = $('#iframe').contents().find('#id_sd_number').val()
  sd_emp = "Тестовый запрос"
  sd_pos = "Тестовый запрос"
  sd_dur_from = "2021-01-01"
  sd_dur_to = "z"
  sd_dep_id = "1"
  sd_reg_number = "268"
  sd_bound_reg_id = "268"
  id="1051"


  const request = new XMLHttpRequest()

  const url = "/sick_reg/updItem/1051"

  const params = 'sd_number=' + sd_number + "&sd_emp=" + sd_emp + "&sd_pos=" + sd_pos + "&sd_dur_from=" + sd_dur_from + "&sd_dur_to=" + sd_dur_to + "&sd_dep=8&sd_reg_number=268&sd_bound_reg_id=268"

  request.open("POST",url,true)

  token = $.cookie('csrftoken')
  console.log(token);
  request.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
  request.setRequestHeader("X-CSRFToken", token)

  request.addEventListener("readystatechange", () => {
    if(request.status === 500) {
console.log(request.responseText);
nw = window.open();
nw.document.write(request.responseText)
}
console.log(request.responseText);
  })

  request.send(params)
}
