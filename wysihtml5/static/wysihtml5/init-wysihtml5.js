var wysihtml_editor

$(function(){
    wysihtml_editor = $('.wysihtml5-widget').wysihtml5({
        "font-styles": true, 
        "emphasis": true, 
        "lists": true,
        "html": true, 
        "link": true, 
        "image": true,
        parserRules: {
            tags: {
                "b":  {},
                "i":  {},
                "br": {},
                "ol": {},
                "ul": {},
                "li": {},
                "h1": {},
                "h2": {},
                "p": {},
                "blockquote": {},
                "div": {},
                "u": 1,
                "img": {
                    "check_attributes": {
                        "width": "numbers",
                        "alt": "alt",
                        "src": "url",
                        "height": "numbers"
                    }
                },
                "a":  {
                    set_attributes: {
                        target: "_blank",
                        rel:    "nofollow"
                    },
                    check_attributes: {
                        href:   "url" // important to avoid XSS
                    }
                }
            }
        }
    }).data('wysihtml5').editor
})
