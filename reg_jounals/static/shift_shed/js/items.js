$(document).ready( function() {
    year = $('#year').text()
    month = $('#month').text()
   
    $('#id_employer').css('visibility','hidden')  
    $('#id_employer').css('height','-10px')
    $('#id_celeb').val(0)
    $('#id_deviation').val(0)

    if (document.location.href.split('/')[5] == 'upditem' ) {
        get_celeb( $('#year').text(), $('#month').text() )
    }

    draw_days(year, month)
    get_celeb(year, month)
    celebs_higlight(year)
    set_row_numbers()
    set_page_break()

})

function get_emp_info(id, month, year){
    fact = 0
    codes = $('.dig_code')

    for (const code of codes) {
       code.value = '' 
    }
    
    $.getJSON('/shift_shed/getemps/single/' + id,  (data) => {
        
         $('#id_employer').val(data[0].id) 
         $('#fullname').text(data[0].fullname)
         $('#position').text(data[0].position__name)
         $('#level').text('Разряд/категория: ' + data[0].level)
         $('#payment').text('Ст.опл: ' + data[0].positionOfPayment)
         
        })
    
    // month = $('#month').val()
    // year = $('#year').val()

    $.getJSON('/shift_shed/getvac/' + id + '/' + year + '/' + month, (data) => {
        
        for (const day of data[0].days) {
             $('#id_day_'+day).val('ОТ')
           }
        
        $('#id_norma').val(data[0].norm)
        

    })

  
    
   
}

function get_celeb(year,month) {
    $.getJSON('/work_cal/' + year + '/' + month,  (data) => {
        
        for (const day of data[0].days.split(',')) {
            $('#id_day_' + day).css('background', 'blue')
        }
        
        return data

       })
}

function calculate() {
    // if (document.location.href.split('/')[5] != 'additem') {
    // $('#id_norma').val(parseFloat($('#main_norma').text().replace(',','.')))
    // }
    have_vacaton = false
    fact = 0
    celebs = 0
    codes = $('.dig_code')
    empty_time = false
    for (const code of codes) {

        code.value = code.value.toUpperCase()
        
       if (code.value != 'ОТ' && code.value != '' && code.value != 'В') {
        fact = fact + parseInt(code.value, 10)
       } 
       if (code.value == 'ОТ') {
        have_vacaton = true
       }

       if (code.style.backgroundColor == 'blue') {
        if (code.value != '' && code.value != 'В' && code.value != 'ОТ') {
        celebs = celebs + parseInt(code.value)}
        else if (code.value == 'ОТ') {
            code.value = 'В'
        }
       }
        


    }

    $('#id_fact').val(fact)
    $('#id_celeb').val(celebs)

    if (have_vacaton == false) {
        
        if (fact != 0) {
        dev = fact - parseFloat($('#id_norma').val()) - $('#id_celeb').val() 
        $('#id_deviation').val(dev) }
        else {
            $('#id_norma').val(0)
            $('#id_devitation').val(0)
            $('#id_celebs').val(0)
            $('#id_fact').val(0)
        }
    }
   
    else {
 

        if (fact > parseFloat($('#id_norma').val())) {
        
           dev = fact - parseFloat($('#id_norma').val()) - $('#id_celeb').val()
            $('#id_deviation').val(dev)
        }
        else {
            if (fact != 0){
            
            $('#id_norma').val(fact)
            $('#id_fact').val(fact)
            
            $('#id_deviation').val(0)}
            
            else {
                $('#id_norma').val(0)
                $('#id_devitation').val(0)
                $('#id_celebs').val(0)
                $('#id_fact').val(0)
            }
            
           
        }

    }

    

    


    
}

function send_submit() {
    calculate()
    $('#shed-item-form').submit()
    $('#shed-item-form-upd').submit()
    

}

// ОТРИСОВКА ЧИСЕЛ В ЗАВИСИМОСТИ ОТ КОЛ-ВА ДНЕЙ
function draw_days(year, month) {

    days_count = Date.getDaysInMonth(year, month-1)





    let days29 = $('#d29')
    let days30 = $('#d30')
    let days31 = $('#d31')




    switch (days_count) {

    case 28:

    for (var i = 0; i < days29.length; i++) {
        days29[i].style.display = 'None'
    }


    for (var i = 0; i < days30.length; i++) {
        days30[i].style.display = 'None'
    }

    for (var i = 0; i < days31.length; i++) {
        days31[i].style.display = 'None'
    }


    case 29:

        for (var i = 0; i < days30.length; i++) {
        days30[i].style.display = 'None'
        }

        for (var i = 0; i < days31.length; i++) {
        days31[i].style.display = 'None'
        }


    case 30:


        for (var i = 0; i < days31.length; i++) {
        days31[i].style.display = 'None'
        }








    break;
    default:

    }
 }


 function celebs_higlight(year) {
    $.getJSON('/work_cal/' + year, (data) => {

        for (let i = 0; i <= data.length; i++) {
            
            days = data[i].days.split(',')
            table = document.querySelectorAll('#table' + data[i].month + ' tbody tr')

            for (const row of table) {
                for (const day of days) {
                    
                    row.querySelector('#day' + day).style.fontWeight = 'bolder'
               
                }

            }
        }

    })
 }

 function set_row_numbers() {
    
    tables = document.querySelectorAll('.shift-table tbody')

    for (table of tables) {
        rows = table.querySelectorAll('tr')
        console.log(rows.length)

    for (let i = 1; i < rows.length+1; i++) {
      
      rows[i-1].querySelector('.number').innerText = i;
      
    }

    }
 }

 function set_page_break () { 
    block = document.querySelectorAll('.shed-month')[11]

    block.className = 'shed-month shed-month-last'
  }