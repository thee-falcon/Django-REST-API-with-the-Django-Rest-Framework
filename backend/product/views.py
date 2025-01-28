from django.shortcuts import render
from .models import Product
from rest_framework import generics
from .serializers import ProductSrializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from requests import Response

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all() # and we can change queryset using function: def get_queryset()
    serializer_class = ProductSrializer
    
class ProductListCreatAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSrializer
    
    # handle the json data from the client(POST request)
    def perform_create(self, serializer):
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
 

@api_view(['GET', 'POST'])    
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    
    if method == 'GET':
        # detail view
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSrializer(obj, Many=False).data
            return Response(data)
        # list view
        queryset = Product.objects.all()
        data = ProductSrializer(queryset, Many=True).data
        return Response(data)
