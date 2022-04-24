function print() {


  info = navigator.userAgent.split(' ')
  for (var inf of info) {
    if (inf.indexOf('Chrome') >-1) {
      browser = "Chrome"
      rcount = 56
    }
    if (inf.indexOf('Firefox') >-1 ) {
      browser = "Firefox"
      rcount = 58
    }
  }

  var WinPrint = window.open('','','left=50,top=50,width=1500,height=1000,toolbar=0,scrollbars=1,status=0');
  WinPrint.document.write("<!DOCTYPE html>")
  WinPrint.document.write('<link rel="stylesheet" type="text/css" href="/static/TURV/css/tabel_print.css"> ')
  WinPrint.document.write('<link rel="stylesheet" href="/static/TURV/css/style1.css">')




WinPrint.document.write("<input onclick='window.print()' id='print_button' type='button' value='печать'>")

WinPrint.document.write("<style>")

WinPrint.document.write(".fio {width:278px !important; text-align: left;}")
WinPrint.document.write("</style>")



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

function print_toxic(year, month, dep) {
switch (month) {
    case 1:
    month = 'Январь'
    break;

    case 2:
    month = 'Февраль'
    break;

    case 3:
    month = 'Март'
    break;

    case 4:
    month = 'Апрель'
    break;

    case 5:
    month = 'Май'
    break;

    case 6:
    month = 'Июнь'
    break;

    case 7:
    month = 'Июль'
    break;

    case 8:
    month = 'Август'
    break;

    case 9:
    month = 'Сентябрь'
    break;

    case 10:
    month = 'Октябрь'
    break;

    case 11:
      month = 'Ноябрь'
      break;

    case 12:
      month = 'Декабрь'
      break;
  default:

}


    info = navigator.userAgent.split(' ')
    for (var inf of info) {
      if (inf.indexOf('Chrome') >-1) {
        browser = "Chrome"
        rcount = 50
      }
      if (inf.indexOf('Firefox') >-1 ) {
        browser = "Firefox"
        rcount = 45
      }
    }

    var WinPrint = window.open('','','left=50,top=50,width=1500,height=1500,toolbar=0,scrollbars=1,status=0');
    WinPrint.document.write("<!DOCTYPE html>")
    WinPrint.document.write("<style>")
    WinPrint.document.write("td,tr,th {border: 1px solid black; text-align:center; font-size: 15pt !important;}")
    WinPrint.document.write("th {font-size: 13pt !important;}")
    WinPrint.document.write("table {width: 100% !important; font-size: 20pt !important;}")
    WinPrint.document.write(".toxic-hide {display:none !important;}")
    WinPrint.document.write(".thin-itogo {width:81px !important;}")
    WinPrint.document.write("#print_button {height: 50px; background:blue !important; font-size: 10pt;}")
    WinPrint.document.write(".fio {width:366px !important; text-align: left;}")
    WinPrint.document.write("</style>")

    WinPrint.document.write('<link rel="stylesheet" type="text/css" href="/static/TURV/css/tabel_print.css"> ')
    // WinPrint.document.write('<link rel="stylesheet" href="/static/TURV/css/style1.css">')



  WinPrint.document.write("<input onclick='window.print()' id='print_button' type='button' value='печать'>")
  if ($('#tabel-type').text() == 2) {
  WinPrint.document.write("<h1 style='text-align:center; font-size: 25pt;'> Табель учета рабочего времени во вредных условиях труда за " + month + " " + year + " " + dep + "</h1>")
}
  if ($('#tabel-type').text() == 3) {
    WinPrint.document.write("<h1 style='text-align:center; font-size: 25pt;'> Табель совмещения за " + month + " " + year + " " + dep + "</h1>")
  }




    // WinPrint.document.write("<div style='display:block !important;' class='for-print not-screen cover'> " + $(".cover").html() + "</div>")
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


          WinPrint.document.write("<table class='print_table' style='border-collapse: collapse; page-break-after: always; table-layout: fixed !important; width: 100% !important;'> <thead>")
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
