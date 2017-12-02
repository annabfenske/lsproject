from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django_redis import get_redis_connection
from django.core.cache import cache
from .models import User
from .forms import UserForm

from datetime import datetime
import time
import uuid
import json

redis = get_redis_connection('default')

def index(request):
  return JsonResponse({'placeholder':True})

def swipe(request, netID):

    redis.rpush(':1:swipes_' + netID, json.dumps(swipe))

    reportTime = cache.get('lost_' + netID)
    
    return JsonResponse({'lost':True})

def reportLost(request):
    print(User.objects.all())
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            ID = form.save(commit=False)
            ID.time_lost = datetime.now()
            ID.save()
            cache.set(form.cleaned_data.get('net_id'), ID.time_lost)
    form = UserForm()
    args = {}
    args['form'] = form
    return render(request,'reportLost/index.html', args)
