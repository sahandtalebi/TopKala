from django.db import models
from TopKala_product.models import Product


class ProductAttributes(models.Model):
    name = models.CharField(max_length=30, verbose_name='نام ویژگی')
    description = models.TextField(verbose_name='توضیح')
    products = models.ManyToManyField(Product)

    class Meta:
        verbose_name = 'ویژگی محصولات'

    def __str__(self):
        return self.name
