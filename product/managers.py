from django.db import models
from django.db.models import Q


class ProductManager(models.Manager):
    def get_products(self, string):
        return super().get_queryset().filter(
            Q(brand__name=string, count__gt=10) | Q(category__name=string, count__gt=10))
