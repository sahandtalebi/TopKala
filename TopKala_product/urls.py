from django.urls import path
from .views import product_list, product_detail


urlpatterns = [
    path('products', product_list),
    path('product/<int:pk>', product_detail),
]