from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForm
from django.core.cache import cache
from datetime import datetime

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
