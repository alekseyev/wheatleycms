import json

from django.http import HttpResponse
from filetransfers.api import prepare_upload
from django.core.urlresolvers import reverse

from .forms import ImageUploadForm
from .models import Image

def ajax_upload_post(request):
    form = ImageUploadForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        result = { 
            'success': 1, 
            'thumbnail_url': form.instance.thumbnail_url(), 
            'url': form.instance.url(),
            'pk': form.instance.pk, 
        }
    else:
        result = { 'success': 0 }
    return HttpResponse(json.dumps(result), content_type='application/json')

def ajax_list_images(request):
    objects = Image.objects.all()[:10]
    result = [{
        'thumbnail_url': obj.thumbnail_url(), 
        'url': obj.url(),
        'pk': obj.pk, 
    } for obj in objects]
    return HttpResponse(json.dumps(result), content_type='application/json')

def ajax_get_upload_data(request):
    upload_url, upload_data = prepare_upload(
        request, 
        reverse('images.views.ajax_upload_post'))
    return HttpResponse(
        json.dumps({
            'upload_url': upload_url,
            'upload_data': upload_data,
        }), 
        content_type='application/json')
