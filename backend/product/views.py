from django.shortcuts import render
from .models import Product
from rest_framework import generics
from .serializers import ProductSrializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all() # and we can change queryset using function: def get_queryset()
    serializer_class = ProductSrializer