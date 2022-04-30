from rest_framework import serializers
from .models import ProductType1, Category, Brand, ProductType2, ProductType3


class CategorySerializer(serializers.ModelSerializer):
    subcategory = serializers.StringRelatedField(read_only=True, required=False)

    class Meta:
        model = Category
        fields = ['name', 'subcategory']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'id']


class ProductType1Serializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()

    class Meta:
        model = ProductType1
        fields = '__all__'


class ProductType2Serializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()

    class Meta:
        model = ProductType2
        fields = '__all__'


class ProductType3Serializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()

    class Meta:
        model = ProductType3
        fields = '__all__'
