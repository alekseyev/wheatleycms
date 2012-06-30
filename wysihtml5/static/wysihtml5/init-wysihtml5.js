var wysihtml_editor

$(function(){
    wysihtml_editor = $('.wysihtml5-widget').wysihtml5({
        "font-styles": true, 
        "emphasis": true, 
        "lists": true,
        "html": true, 
        "link": true, 
        "image": true 
    }).data('wysihtml5').editor
})
