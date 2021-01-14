function PrintSelected() {

var checkboxes = $('.for_print')
var rows = $('.t_row')
var printed_rows = 0;

var WinPrint = window.open('','','left=50,top=50,width=800,height=640,toolbar=0,scrollbars=1,status=0');
WinPrint.document.write('<table>');
WinPrint.document.write('<thead class="thead-dark">');
WinPrint.document.write('<tr class="tr-header">');
WinPrint.document.write('<th></th>');
WinPrint.document.write('<th scope="col">Дата приказа</th>');
WinPrint.document.write('<th scope="col">Номер</th>');
WinPrint.document.write('<th scope="col">Сотрудник</th>');
WinPrint.document.write('<th scope="col">Подразделение</th>');
WinPrint.document.write('<th scope="col">Содержание</th>');
WinPrint.document.write('<th scope="col">Ответственный сотрудник</th>');
WinPrint.document.write('</tr>');
WinPrint.document.write('</thead>');

for (var i = 0; i < checkboxes.length; i++) {
  if ($(checkboxes[i]).prop('checked') == true) {
    WinPrint.document.write('<tr>' + $(rows[i]).html() + '</tr>');
  } ;

};
WinPrint.document.write('</table>');
WinPrint.focus();






//
// for (var i = 0; i < row_.length; i++) {
//   WinPrint.document.write('<tr>')
//   WinPrint.document.write(row_[i].innerHTML );
// WinPrint.document.write('</tr>')
// }
//
//
//
// WinPrint.document.write('</table>');
//
//
//
//
// WinPrint.focus();



}
