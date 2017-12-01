from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForm
from datetime import datetime
from django.core.cache import cache
from django.views.decorators.cache import cache_page

#@cache_page(60 * 15)
def reportLost(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            #cache.write(form)
            cache.set(form,datetime.now)
    form = UserForm()
    args = {}
    args['form'] = form
    return render(request,'reportLost/index.html', args)
