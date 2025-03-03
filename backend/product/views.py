from django.shortcuts import render
from requests import get
from .models import Product
from rest_framework import generics, mixins
from .serializers import ProductSrializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all() # and we can change queryset using function: def get_queryset()
    serializer_class = ProductSrializer
    
class ProductListCreatAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSrializer
    
    # handle the json data from the client(POST request)
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

class ProductUpdateCreateView(generics.UpdateAPIView):
    serializer_class = ProductSrializer
    queryset = Product.objects.all()
    lookup_field = 'pk'

class ProductMixinView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = ProductSrializer
    queryset = Product.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# another way to handle crud request in one single function
@api_view(['GET', 'POST'])    
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    
    if method == 'GET':
        # detail view
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSrializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Product.objects.all()
        data = ProductSrializer(queryset, many=True).data
        return Response(data)
    elif method == 'POST':
        # create the item to store the data from the request
        serializer = ProductSrializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
                serializer.save(content=content)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
