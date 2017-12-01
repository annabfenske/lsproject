from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import User
from .forms import UserForm
from django.template import RequestContext
from datetime import datetime

def reportLost(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        print('form before:', form)
        print('form after:', form)
        if form.is_valid():
            form.save()
        print('here - 1')
        return render(request,'reportLost/index.html', {form : form})
    else:
        form = UserForm()
    args = {}

    args['form'] = form
    print('here - 2')
    return render(request,'reportLost/index.html', args)
