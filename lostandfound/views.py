from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import User
from .forms import UserForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template import RequestContext

def reportLost(request):
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render('reportLost/index.html')
    else:
        form = UserForm()
    args = {}

    args['form'] = form

    return render_to_response('reportLost/index.html', args)
