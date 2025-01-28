from django.shortcuts import render
from .models import Product
from rest_framework import generics
from .serializers import ProductSrializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all() # and we can change queryset using function: def get_queryset()
    serializer_class = ProductSrializer
    
class ProductCreatAPIView(generics.CreateAPIView):
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