from rest_framework import serializers
from .models import Product, Category, Brand


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    subcategory = serializers.StringRelatedField(read_only=True, required=False)

    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()

    class Meta:
        model = Product
        fields = '__all__'
