from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بنید ها'

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=10)
    rate = models.IntegerField(default=0)
    free = models.BooleanField(default=True)