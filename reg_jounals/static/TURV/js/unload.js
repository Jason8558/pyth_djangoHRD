function write_deps() {
  $('#udeps_hide').val(($('select#u_dep').val()))
}

function upd_norma() {
  
  query_url = '/turv/overtime/upd'
  $.getJSON(query_url,  (data) => {
    alert(data)
  })

}
