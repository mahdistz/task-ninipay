from django.db import models
from django.db.models import Q


class ProductManager(models.Manager):
    def get_products(self, brand_or_category):
        return super().get_queryset().filter(
            Q(brand__name=brand_or_category, count__gt=10) | Q(category__name=brand_or_category, count__gt=10))
