from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())

# Create your views here.
