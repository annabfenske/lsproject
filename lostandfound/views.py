from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def swipe(request, netID):
    # Check if id is lost
    # cache.get(netID)?
    # cache.write(swipe)
    return JsonResponse({'lost':False})

def readUser(request, netID):
    # Should we check postGres or just redis? Recency of swipes?
    return render(request, 'lostandfound/swipehistory.html')

# def createUser(request, netID):