$(document).ready( function() {
    $('#id_employer').css('visibility','hidden')  
    $('#id_employer').css('height','-10px')
    $('#id_celeb').val(0)
    $('#id_deviation').val(0)
})

function get_emp_info(id, month, year){
    fact = 0
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
        
        $('#id_norma').val(data[0].norm)
        

    })

    get_celeb(year, month)
    
   
}

function get_celeb(year,month) {
    $.getJSON('/work_cal/' + year + '/' + month,  (data) => {
        
        for (const day of data[0].days.split(',')) {
            $('#id_day_' + day).css('background', 'blue')
        }
        
       })
}

function calculate() {
    if (document.location.href.split('/')[5] != 'additem') {
    $('#id_norma').val(parseFloat($('#main_norma').text().replace(',','.')))
    }
    have_vacaton = false
    fact = 0
    celebs = 0
    codes = $('.dig_code')
    for (const code of codes) {
        console.log(code.value);
       if (code.value != 'ОТ' && code.value != '') {
        fact = fact + parseInt(code.value, 10)
       } 
       if (code.value == 'ОТ') {
        have_vacaton = true
       }

       if (code.style.backgroundColor == 'blue') {
        if (code.value != '') {
        celebs = celebs + parseInt(code.value)}
       }

    }

    if (have_vacaton == false) {
       console.log($('#n_time').text()) 
        dev = fact - parseFloat($('#id_norma').val()) - $('#id_celeb').val()
        $('#id_deviation').val(dev)
    }
    else {
        $('#id_norma').val(fact)
        $('#id_deviation').val(0)
    }

    console.log(celebs);

    

    $('#id_fact').val(fact)
    $('#id_celeb').val(celebs)
    
}

function send_submit() {
    calculate()
    $('#shed-item-form').submit()
    $('#shed-item-form-upd').submit()
    

}
