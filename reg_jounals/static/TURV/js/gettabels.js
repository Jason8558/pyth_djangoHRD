function gettabels(type, access) {

  $.getJSON('/turv/gettabels/' + type,  (data) => {
    $('#tabels-main-table tbody').empty()

    for (var i = 0; i < data.length; i++) {
      if (access == 'True') {
        $('#tabels-main-table tbody').append('<tr><td>' + data[i].id + '</td><td class="table-type">' + data[i].type__name + '</td><td>' + data[i].year +  '</td><td>' + data[i].department__name + '</td><td>' + data[i].res_officer + '</td><td>' + data[i].paper_check + '</td><td>' + data[i].sup_check + '</td><td>' + data[i].unloaded + '</td><td></td></tr>')
      }
      else {
        $('#tabels-main-table tbody').append('<tr><td>' + data[i].id + '</td><td class="table-type">' + data[i].type__name + '</td><td>' + data[i].year +  '</td><td>' + data[i].department__name + '</td><td>' + data[i].sup_check + '</td></tr>')
      }

    }

  })

}

function month_to_str(month) {

}
