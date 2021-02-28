from django.http import Http404
from django.shortcuts import render
from TopKala_product.models import Product, ProductBrand
from TopKala_category.models import ProductCategory


def product_list(request):
    products = Product.objects.all_products()
    lower_price = Product.objects.lower_price()
    high_price = Product.objects.high_price()
    categories = ProductCategory.objects.all()
    product_brand = ProductBrand.objects.all()

    context = {
        'products': products,
        'lower_price': lower_price,
        'high_price': high_price,
        'categories': categories,
        'product_brand': product_brand,
    }

    return render(request, 'product_list.html', context)


def product_detail(request, *args, **kwargs):
    pk = kwargs.get('pk')

    product = Product.objects.filter(id=pk).first()

    if product is None or product.active is False:
        raise Http404('محصول مورد نظر یافت نشد')

    product_category = ProductCategory.objects.filter(id=pk).first()
    product_attributes = product.productattributes_set.all()

    context = {
        'object': product,
        'product_category': product_category,
        'product_attributes': product_attributes,
    }

    return render(request, 'single_product.html', context)
