from rest_framework import serializers
from .models import Basket
from products.serializers import SingleProductSerializer
from products.models import Product


class BasketProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price',)


class BasketSerializer(serializers.ModelSerializer):
    """Serializer for Category Model"""
    product = BasketProductSerializer()

    class Meta:
        model = Basket
        fields = '__all__'
