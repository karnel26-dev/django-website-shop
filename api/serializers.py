from rest_framework import serializers
from shop.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
   class Meta:
       model = Category
       fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
   class Meta:
       model = Product
       exclude = ('slug', 'created', 'updated')