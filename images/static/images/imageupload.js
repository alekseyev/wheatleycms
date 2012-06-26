$(document).ready(function(){
})

function start_upload(url) {
    $('#form').ajaxSubmit({
        url: url,
        success: finish_upload
    })
    $('#upload-progress').show()
    $('#upload-submit').attr('disabled', 'disabled')
    return false
}

function finish_upload(data, textStatus, jqXHR) {
    $('#upload-form').modal('hide')
    wysihtml_editor.composer.commands.exec('insertImage', { src: data.url })
}
