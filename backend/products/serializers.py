from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category Model"""
    class Meta:
        model = Category
        fields = '__all__'

class ProductsAllSerializer(serializers.ModelSerializer):
    """Serializer for Home page"""

    class Meta:
        model = Product
        fields = ("title", "short_description", "poster", "price", "url")



class SingleProductSerializer(serializers.ModelSerializer):
    """Serializer for products item"""
    categories = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    class Meta:
        model = Product
        fields = "__all__"