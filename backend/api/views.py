from product.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.serializers import ProductSrializer

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    
    if instance:
        # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price', ''])
        data = ProductSrializer(instance).data
    return Response(data)
