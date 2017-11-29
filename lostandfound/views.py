from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
import time

# Create your views here.

def swipe(request, netID):
    expiryTime = 36000 # 10 hours
    currentTime = time.time()

    swipe = {
      'netID': netID,
      'time': currentTime
    }
    cache.write(swipe)
    reportTime = cache.get(netID)
    
    if !reportTime:
      return JsonResponse({'lost':False})

    if reportTime < currentTime - expiryTime:
      return JsonResponse({'lost':False})
    
    return JsonResponse({'lost':True})

def readUser(request, netID):
    # Should we check postGres or just redis? Recency of swipes?
    return render(request, 'lostandfound/swipehistory.html')

# def createUser(request, netID):
