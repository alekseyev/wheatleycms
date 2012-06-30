var image_data = {}
var gallery_data = []
var upload_url = ''
var upload_data = {}

$(document).ready(function(){
    update_upload_data()
})

function update_upload_data() {
    $.getJSON(
        '/images/ajax/get_upload_data/',
        function(data, textStatus, jqXHR){
            upload_url = data.upload_url
            upload_data = data.upload_data
            $('#upload-submit').removeAttr('disabled')
        })
}

function start_upload() {
    $('#form').ajaxSubmit({
        url: upload_url,
        success: finish_upload
    })
    $('#upload-progress').show()
    $('#upload-submit').attr('disabled', 'disabled')
}

function finish_upload(data, textStatus, jqXHR) {
    $('#upload-form').modal('hide')
    $('#upload-progress').hide()
    $('#id_image_inner').val('')
    update_upload_data()
    image_data = data
    show_image()
}

function show_image() {
    $('#image-modal-thumbnail').attr('src', image_data.thumbnail_url)
    $('#image-modal').modal('show')
}

function insert_image() {
    wysihtml_editor.composer.commands.exec(
        'insertHTML', 
        '<img src="' + image_data.url + '"></a>'
        )
    $('#image-modal').modal('hide')
}

function insert_thumbnail() {
    wysihtml_editor.composer.commands.exec(
        'insertHTML', 
        '<a href="' + image_data.url + '"><img src="' + image_data.thumbnail_url + '"></a>')
    $('#image-modal').modal('hide')
}

function show_gallery() {
    $.getJSON(
        '/images/ajax/images/', 
        function(data, textStatus, jqXHR){
            gallery_data = data
            var html = ''
            for (var img in data) {
                html += '<li>'
                html += '<a href="#" class="thumbnail" onclick="gallery_click(' + img +  ')">'
                html += '<img src="' + gallery_data[img].thumbnail_url + '">'
                html += '</a></li>'
            }
            $('#gallery-thumbnails').html(html)
            $('#gallery').modal('show')
        })
}

function gallery_click(gallery_index) {
    $('#gallery').modal('hide')
    image_data = gallery_data[gallery_index]
    show_image()
}
