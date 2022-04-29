from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def show_products_api(request, brand_id=None, product_id=None):
    pass


def index(request):
    return HttpResponse('hello world!')
