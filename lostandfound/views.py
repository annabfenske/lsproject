from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
from django_redis import get_redis_connection

import time
import uuid
import json


redis = get_redis_connection('default')

def index(request):
  return JsonResponse({'placeholder':True})

def swipe(request, netID):
    expiryTime = 36000 # 10 hours
    currentTime = time.time()

    swipe = {
      'netID': netID,
      'time': currentTime
    }

    # if request.body.location:
    #   swipe['location'] = request.body.location
    swipe['location'] = 'Bobst'

    redis.rpush(':1:swipes_' + netID, json.dumps(swipe))

    reportTime = cache.get('lost_' + netID)

    if not reportTime:
      return JsonResponse({'lost':False})

    if reportTime < currentTime - expiryTime:
      return JsonResponse({'lost':False})
    
    return JsonResponse({'lost':True})

def readUser(request, netID):
    swipes = redis.lrange(':1:swipes_' + netID, -20, -1)
    swipes = map(json.loads, swipes)
    print swipes
    context = {'headers': ['Time', 'Location'], 
              'keys': ['time', 'location'],
              'swipes': swipes}
    return render(request, 'swipe_history.html', context)

def reportLost(request, netID):
  return JsonResponse({"placeholder":True})

def createUser(request):
  return JsonResponse({"placeholder":True})
