from django.urls import path
from .views import product_list, ProductView


urlpatterns = [
    path('products', product_list),
    path('product/<int:pk>', ProductView.as_view()),
]