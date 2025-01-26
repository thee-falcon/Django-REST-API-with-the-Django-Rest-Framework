from product.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.serializers import ProductSrializer

@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    
    if request.method == 'GET':
        instance = Product.objects.all().first()
        data = {}

        if instance:
            # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price', ''])
            data = ProductSrializer(instance).data
        return Response(data)
    elif request.method == 'POST':
        serializer = ProductSrializer(data=request.data) # if we want let a client know about the issue.
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response({"invalid": "Not good data"}, status=400) # if we don't want a client know about the issue.
