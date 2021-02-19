from django.shortcuts import render
from django.views.generic import ListView, DetailView
from TopKala_product.models import Product


def product_list(request):
    products = Product.objects.all_products()
    lower_price = Product.objects.lower_price()
    high_price = Product.objects.high_price()

    context = {
        'products': products,
        'lower_price': lower_price,
        'high_price': high_price,
    }

    return render(request, 'product_list.html', context)
