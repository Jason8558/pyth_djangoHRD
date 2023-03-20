$(document).ready( function() {
    $('#id_employer').css('visibility','hidden')  
    $('#id_employer').css('height','-10px')
})

function get_emp_info(id, month, year){

    codes = $('.dig_code')

    for (const code of codes) {
       code.value = '' 
    }

    $.getJSON('/shift_shed/getemps/single/' + id,  (data) => {
         console.log(data[0]); 
         $('#id_employer').val(data[0].id) 
         $('#fullname').text(data[0].fullname)
         $('#position').text(data[0].position__name)
         $('#level').text('Разряд/категория: ' + data[0].level)
         $('#payment').text('Ст.опл: ' + data[0].positionOfPayment)

        })
    
    // month = $('#month').val()
    // year = $('#year').val()

    $.getJSON('/shift_shed/getvac/' + id + '/' + year + '/' + month, (data) => {
        console.log(data[0].days);
        for (const day of data[0].days) {
             $('#id_day_'+day).val('ОТ')
           }
        
       
        $('#n_time').text(data[0].norm)

    })
    
   
}

function calculate() {
    fact = 0
    codes = $('.dig_code')
    for (const code of codes) {
        console.log(code.value);
       if (code.value != 'ОТ' && code.value != '') {
        fact = fact + parseInt(code.value, 10)
       } 
    }

    $('#id_fact').val(fact)
}
