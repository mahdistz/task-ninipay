from django.db.models import Q
from rest_framework.decorators import api_view  # GET PUT POST , ..... نوع درخواست
from rest_framework.response import Response  # ارسال پاسخ ها
from .serializers import ProductType1Serializer, ProductType2Serializer, ProductType3Serializer
from .models import ProductType1, ProductType2, ProductType3
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
@api_view(["GET"])
def show_products(request, id=None, brand_id=None):
    if request.method == 'GET':
        if id or brand_id:
            products = ProductType1.objects.filter(Q(id=id) | Q(brand__id=brand_id))
            serializer = ProductType1Serializer(products, many=True)
            return Response(serializer.data)


@csrf_exempt
@api_view(["GET"])
def show_products_type1_count_more_than_10(request, string):
    if request.method == 'GET':
        products = ProductType1.objects.get_products(string=string)
        serializer = ProductType1Serializer(products, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(["GET"])
def show_products_type2_count_more_than_10(request, string):
    if request.method == 'GET':
        products = ProductType2.objects.get_products(string=string)
        serializer = ProductType2Serializer(products, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(["GET"])
def show_products_type3_count_more_than_10(request, string):
    if request.method == 'GET':
        products = ProductType3.objects.get_products(string=string)
        serializer = ProductType3Serializer(products, many=True)
        return Response(serializer.data)

