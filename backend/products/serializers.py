from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category Model"""
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    """Serializer for products item"""
    class Meta:
        model = Product
        fields = "__all__"