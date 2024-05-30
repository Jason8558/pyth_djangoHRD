function open_additional_menu(el, additional_menu_panel) {
    // открыть доп меню
    close_all_panels()
  
    additional_menu_panel = document.getElementById(additional_menu_panel)
  
    coords = el.getBoundingClientRect()
  
    additional_menu_panel.style.display   = 'flex'
    additional_menu_panel.style.position  = 'absolute'
    additional_menu_panel.style.top       = (Number(coords.top) + 40) + 'px'
    
    additional_menu_panel.style.height    = 'max-content'
    if (additional_menu_panel.classList.contains('search')) {

    }
    else {
        additional_menu_panel.style.width    = 'max-content'
        additional_menu_panel.style.left      = coords.left + 'px'
    }
     
  
    additional_menu_panel.addEventListener('mouseleave', (vsp) => {
      close_all_panels()
    })
  
    el.onclick = function() {
      
      if (additional_menu_panel.style.display == 'none') {
        additional_menu_panel.style.display = 'flex'}
      else {
        additional_menu_panel.style.display = 'none'
        
      }
  
    }
   
  
   //el.onclick = 'open_additional_menu(this)'
  
  }

function close_all_panels() {
    panels = document.getElementsByClassName('panel')

    for (const panel of panels) {
        panel.style.display = 'none'
    }
}

function set_table_head() {
  original_table_th   = document.querySelectorAll('#tabels-main-table thead th')
  copy_table_th       = document.querySelectorAll('#tabels-main-table-head-copy thead th')

  i = 0

  for (const th of copy_table_th) {
    th.style.width = window.getComputedStyle(original_table_th[i]).width
    i++ 
  }

  document.getElementById('tabels-main-table-head-copy').style.width = window.getComputedStyle(document.getElementById('tabels-main-table')).width
  document.getElementById('tabels-main-table-head-copy').style.display = 'block'
}