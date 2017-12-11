from django.shortcuts import render
from django.http import HttpResponse
from .models import lostNYUID
from django.http import JsonResponse, HttpResponse
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt

from .forms import UserForm

from datetime import datetime

def index(request):
  return JsonResponse({'placeholder':True})

def swipe(request, netID):
    if cache.get(netID):
        return JsonResponse({'lost':True})
    return JsonResponse({'lost':False})

@csrf_exempt
def reportLost(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            ID = form.save(commit=False)
            ID.time_lost = datetime.now()
            ID.save()
    form = UserForm()
    args = {}
    args['form'] = form
    return render(request,'reportLost/index.html', args)
