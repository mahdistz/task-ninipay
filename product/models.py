from django.db import models
from .managers import ProductManager


class CommonInfo(models.Model):
    # Common fields in products
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    count = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    expire_at = models.DateField()

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=50)
    subcategory = models.ForeignKey('self', null=True, blank=True,
                                    related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductType1(CommonInfo):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    objects = ProductManager()

    def __str__(self):
        return self.name


class ProductType2(CommonInfo):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    objects = ProductManager()

    def __str__(self):
        return self.name


class ProductType3(CommonInfo):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    objects = ProductManager()

    def __str__(self):
        return self.name
