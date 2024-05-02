from django.urls import path
from .views import get_info, get_products, detail



urlpatterns = [
    path('', get_info, name='get_info'),
    path('products/<int:pk>', get_products, name='get_products'),
    path('products/detail/<int:pk>', detail, name='detail')
]