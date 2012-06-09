from django.shortcuts import render

from forms import TestForm

def test_form(request):
    return render(request, 'form.html', { 'form': TestForm })
