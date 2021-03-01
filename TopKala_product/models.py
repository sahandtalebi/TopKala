import os

from django.db.models import Q

from TopKala_category.models import ProductCategory
from django.db import models


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_images_path(instance, filename):
    name, ext = get_filename_ext(filename)
    fainal_name = f"{instance.title}{ext}"
    return f"products/{fainal_name}"


class ProductManager(models.Manager):
    def all_products(self):
        return self.filter(active=True)

    def lower_price(self):
        return self.filter(active=True).order_by('price')

    def high_price(self):
        return self.filter(active=True).order_by('-price')

    def search(self, search_result):
        return self.filter(Q(title__iexact=search_result))


class ProductBrand(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField()

    class Meta:
        verbose_name = ' برند'
        verbose_name_plural = 'برند ها'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='موضوع')
    brand = models.ForeignKey(ProductBrand, on_delete=models.DO_NOTHING, verbose_name='برند', blank=True)
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_images_path, null=True, blank=True, verbose_name='تصویر شاخص')
    active = models.BooleanField(default=False, verbose_name='وضعیت')
    category = models.ManyToManyField(ProductCategory, verbose_name='دسته بندی')
    visit = models.IntegerField(default=0)
    special_sale = models.BooleanField(default=False, verbose_name='فروش ویژه')
    objects = ProductManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def absolute_url(self):
        return f"/product/{self.id}/{self.title.replace(' ' , '-')}"


