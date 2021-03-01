from django.http import Http404
from django.shortcuts import render
from TopKala_product.models import Product, ProductBrand
from TopKala_category.models import ProductCategory
from .forms import ProductSearch


def product_list(request):
    product_search_form = ProductSearch(request.POST or None)
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
        'product_search_form': product_search_form,
    }

    if product_search_form.is_valid():
        name = product_search_form.cleaned_data.get('name')
        product_search = Product.objects.search(name)
        context['product_search'] = product_search

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
