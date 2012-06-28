image_data = {}

$(document).ready(function(){
})

function start_upload(url) {
    $('#form').ajaxSubmit({
        url: url,
        success: finish_upload
    })
    $('#upload-progress').show()
    $('#upload-submit').attr('disabled', 'disabled')
}

function finish_upload(data, textStatus, jqXHR) {
    $('#upload-form').modal('hide')
    $('#upload-progress').hide()
    $('#id_image_inner').val('')
    $('#upload-submit').removeAttr('disabled')
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
