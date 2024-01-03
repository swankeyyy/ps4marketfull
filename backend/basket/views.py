from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Basket
from .serializers import BasketSerializer
from users.models import User
from products.models import Product


class BasketView(APIView):
    def get(self, request, pk):
        basket = Basket.objects.filter(user__id=pk)
        if basket:
            serializer = BasketSerializer(basket, many=True)
            return Response(serializer.data)
        return Response({'basket': 'null'})

    def post(self, request, pk):
        basket = Basket.objects.create(user_id=pk,
                                       product_id=request.data.get('product_id'),
                                       quantity=request.data.get('product_quantity'))
        basket.save()
        serializer = BasketSerializer(basket)

        return Response(serializer.data)

    def delete(self, request, pk):
        basket = Basket.objects.get(user__id=pk, id=request.data.get('basket_id'))
        basket.delete()
        return Response({'status_del': 'done'})
