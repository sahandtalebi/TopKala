from django.shortcuts import render
from django.views.generic import ListView, DetailView

from TopKala_product.models import Product


class ProductList(ListView):
    template_name = 'product_list.html'
    model = Product


class ProductDetail(DetailView):
    pass

