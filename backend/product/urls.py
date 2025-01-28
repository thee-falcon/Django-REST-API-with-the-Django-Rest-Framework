from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('',  views.ProductCreatAPIView.as_view()),
]
