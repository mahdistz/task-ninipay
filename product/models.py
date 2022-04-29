from django.db import models
from .managers import ProductManager


class CommonInfo(models.Model):
    # Common fields in products
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=50)
    subcategory = models.ForeignKey('self', null=True, blank=True,
                                    related_name='subcategories', on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


product_type = [
    ('1', 'آرایشی بهداشتی'),
    ('2', 'شوینده'),
    ('3', 'خوراکی'),
]


class Product(CommonInfo):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    objects = ProductManager()

    def __str__(self):
        return self.name
