from django.http import Http404
from django.shortcuts import render

from TopKala_attributes.models import ProductAttributes
from TopKala_product.models import Product
from TopKala_category.models import ProductCategory


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

# class ProductView(DetailView):
#     model = Product
#     template_name = 'single_product.html'
#
#     def get_product_category(self, **kwargs):
#         context = super().get_product_category(**kwargs)
#         print([kwargs])
#         context['product_category'] = ProductCategory.objects.filter(id=Product.objects.id)
#         return context
