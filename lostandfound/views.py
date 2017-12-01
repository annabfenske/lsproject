from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
import time
import uuid

# Create your views here.

def index(request):
  return JsonResponse({"placeholder":True})

def swipe(request, netID):
    expiryTime = 36000 # 10 hours
    currentTime = time.time()

    tempID = uuid.uuid4()
    swipe = {
      'netID': netID,
      'time': currentTime
    }
    cache.set(tempID, swipe)
    reportTime = cache.get(netID)
    
    if not reportTime:
      return JsonResponse({'lost':False})

    if reportTime < currentTime - expiryTime:
      return JsonResponse({'lost':False})
    
    return JsonResponse({'lost':True})

def readUser(request, netID):
    # Should we check postGres or just redis? Recency of swipes?
    return render(request, 'lostandfound/swipehistory.html')

def reportLost(request, netID):
  return JsonResponse({"placeholder":True})

def createUser(request):
  return JsonResponse({"placeholder":True})
