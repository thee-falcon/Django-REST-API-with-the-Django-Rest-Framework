from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('',  views.ProductListCreatAPIView.as_view()),
    path('update/<int:pk>/', views.ProductUpdateCreateView.as_view()),
    # path('<int:pk>/', views.product_alt_view),
    # path('',  views.product_alt_view),
]
