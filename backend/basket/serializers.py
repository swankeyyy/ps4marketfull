from rest_framework import serializers
from .models import Basket


class BasketSerializer(serializers.ModelSerializer):
    """Serializer for Category Model"""
    class Meta:
        model = Basket
        fields = '__all__'

