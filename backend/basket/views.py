from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Basket
from .serializers import BasketSerializer


class BasketView(APIView):
    def get(self, request, pk):
        basket = Basket.objects.filter(user_id=pk)
        if basket:
            serializer = BasketSerializer(basket, many=True)
            return Response({'basket': serializer.data})
        return Response({'basket': 'null'})

    def post(self, request, pk):
        basket = Basket.objects.filter(user_id=pk, product_id=request.data.get('product_id')).first()
        if basket:
            basket.quantity += 1
            basket.save()
        else:
            basket = Basket.objects.create(user_id=pk,
                                           product_id=request.data.get('product_id'),
                                           quantity=request.data.get('product_quantity'))
            basket.save()
        serializer = BasketSerializer(basket)
        # basket = Basket.objects.create(user_id=pk,
        #                                product_id=request.data.get('product_id'),
        #                                quantity=request.data.get('product_quantity'))
        # basket.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        print(request.data)
        basket = Basket.objects.filter(user_id=pk, id=request.data.get('basket_id')).first()
        if basket:

            basket.delete()
            return Response({'status_del': 'done'})
        return Response({'basket': 'корзина не найдена'})
