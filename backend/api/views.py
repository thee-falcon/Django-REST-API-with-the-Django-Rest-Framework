from django.shortcuts import render
from django.http import JsonResponse
import json
from product.models import Product
from django.forms.models import model_to_dict

# Create your views here.
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return JsonResponse(data)
