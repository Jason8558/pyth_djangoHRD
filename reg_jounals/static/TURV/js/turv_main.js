function open_additional_menu(el, additional_menu_panel) {
    // открыть доп меню
    //close_all_forms()
  
    additional_menu_panel = document.getElementById(additional_menu_panel)
  
    coords = el.getBoundingClientRect()
  
    additional_menu_panel.style.display   = 'flex'
    additional_menu_panel.style.position  = 'absolute'
    additional_menu_panel.style.top       = (Number(coords.top) + 40) + 'px'
    additional_menu_panel.style.left      = coords.left + 'px'
    additional_menu_panel.style.height    = '67px' 
  
    additional_menu_panel.addEventListener('mouseleave', (vsp) => {
      //close_all_forms()
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