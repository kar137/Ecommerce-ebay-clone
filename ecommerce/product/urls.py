from django.urls import path
from . import views 

urlpatterns = [
    path('product-form', views.ProductView.as_view(), name= "product-form"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name= "product-detail"),
]