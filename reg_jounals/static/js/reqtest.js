
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
  errors = 1


  const request = new XMLHttpRequest()

  const url = "/sick_reg/268/addItem"

  const params = 'sd_number=' + sd_number + "&sd_emp=" + sd_emp + "&sd_pos=" + sd_pos + "&sd_dur_from=" + sd_dur_from + "&sd_dur_to=" + sd_dur_to + "&sd_dep=8&sd_reg_number=268&sd_bound_reg_id=268"

  request.open("POST",url,true)

  token = $.cookie('csrftoken')
  // console.log(token);
  request.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
  request.setRequestHeader("X-CSRFToken", token)

  request.addEventListener("readystatechange", () => {
    // console.log(request.status);
    txt = request.responseText

  //
  //     console.log(k, v);
  //
  //
  // })
  // try {
    txt = JSON.parse(txt)
  //   console.log(txt);
  //   console.log(errors);
  // } catch (e) {
  //   errors = 0
  // }


  if (errors == 1) {
  keys = Object.keys(txt)
  values = Object.values(txt)

  vals = Object.values(values[0])


  for (var i = 0; i < values.length; i++) {
    val = Object.values(values[i])
    console.log(keys[i] + " " + val[0].message + " <" + val[0].code + "> ");
  }
}





    // $.getJSON(txt,  (data) => {
    //   nw.write(data)
    // })



    if(request.status === 500) {





}

  })

  request.send(params)
}
