from rest_framework import serializers
from .models import User


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category Model"""
    class Meta:
        model = User
        fields = '__all__'

