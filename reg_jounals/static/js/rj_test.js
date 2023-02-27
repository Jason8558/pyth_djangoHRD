$(document).ready(function() {

  $.getJSON('/work_cal/2023' ,  (data) => {
var calendar = []
    for (var i = 0; i < data.length; i++) {
      calendar.push({
        'month':data[i].month,
        'days':data[i].days
      })
    }
console.log(calendar[0].days);
  })

})
