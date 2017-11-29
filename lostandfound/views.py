from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.template import loader

def reportLost(request):
    template = loader.get_template('reportLost/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
