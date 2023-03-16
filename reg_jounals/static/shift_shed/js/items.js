$(document).ready( function() {
    $('#id_employer').css('visibility','hidden')  
    $('#id_employer').css('height','-10px')
})

function get_emp_info(id){

    $.getJSON('/shift_shed/getemps/single/' + id,  (data) => {
         console.log(data[0]); 
         $('#id_employer').val(data[0].id) 
         $('#fullname').text(data[0].fullname)
         $('#position').text(data[0].position__name)
         $('#level').text('Разряд/категория: ' + data[0].level)
         $('#payment').text('Ст.опл: ' + data[0].positionOfPayment)
         

        })


}