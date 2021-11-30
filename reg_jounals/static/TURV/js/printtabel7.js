function print() {


  info = navigator.userAgent.split(' ')
  for (var inf of info) {
    if (inf.indexOf('Chrome') >-1) {
      browser = "Chrome"
      rcount = 64
    }
    if (inf.indexOf('Firefox') >-1 ) {
      browser = "Firefox"
      rcount = 64
    }
  }

  var WinPrint = window.open('','','left=50,top=50,width=1500,height=1000,toolbar=0,scrollbars=1,status=0');
  WinPrint.document.write('<link rel="stylesheet" type="text/css" href="/static/TURV/css/tabel_print6.css?v=2"> ')
  WinPrint.document.write('<link rel="stylesheet" href="/static/TURV/css/style11.css">')



WinPrint.document.write("<input onclick='window.print()' id='print_button' type='button' value='печать'>")




  WinPrint.document.write("<div style='display:block !important;' class='for-print not-screen cover'> " + $(".cover").html() + "</div>")
    rows = $(".tabel tbody tr")

    parts = ((rows.length)/rcount)
    parts = parts.toString().split('.')[0]

    ost =(rows.length - (parts*rcount))

    if (ost => 1) {
      parts = +parts + 1

    }
i = 0
if (parts > 0) {
    for (var y = 0; y < parts-1; y++) {

        next = i+rcount
        WinPrint.document.write("<table class='print_table' style='page-break-after: always; table-layout: fixed !important;'> <thead>")
        WinPrint.document.write( $(".tabel thead").html() + "</thead><tbody>")

        for (var i = i; i < next; i++) {

          WinPrint.document.write("<tr>" + rows[i].innerHTML + "</tr>" )}

        WinPrint.document.write("</tbody></table>")


    }


  WinPrint.document.write("<table class='print_table'  style='table-layout: fixed !important;'> <thead>")
    i = (rows.length) - ost
WinPrint.document.write( $(".tabel thead").html() + "</thead><tbody>")
    for (var i = i; i < rows.length; i++) {

        WinPrint.document.write("<tr>" + rows[i].innerHTML + "</tr>" )
      }

    WinPrint.document.write("</tbody></table>")
    WinPrint.document.write("<div class='cover-footer'>" + $(".cover-footer").html() + "</div>")
}
else {

}




}
