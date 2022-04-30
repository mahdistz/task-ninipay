from django.contrib import admin
from product.models import ProductType1, Category, Brand, ProductType2, ProductType3

# Register your models here.
admin.site.register(ProductType1)
admin.site.register(ProductType2)
admin.site.register(ProductType3)
admin.site.register(Category)
admin.site.register(Brand)
