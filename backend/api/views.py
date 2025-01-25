from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
def api_home(request, *args, **kwargs):
    
    # print(request.GET) # url query params
    
    body = request.body # byte string of json data
    data = {}
    try:
        data = json.loads(body) # convert the byte string to json string
    except:
        pass
    data["params"] = dict(request.GET)
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type
    return JsonResponse(data)
