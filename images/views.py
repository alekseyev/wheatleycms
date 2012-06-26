import json

from django.http import HttpResponse

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
