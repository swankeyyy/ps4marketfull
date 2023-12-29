from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Product
from .serializers import CategorySerializer, ProductsAllSerializer, SingleProductSerializer


class AllCategoriesView(APIView):
    """View for List Categories on Frontend (navbar, sidebar)"""

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class AllProductsView(APIView):
    """View for main page"""
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductsAllSerializer(products, many=True)
        return Response(serializer.data)


class SingleProductView(APIView):
    """Detail Product View"""
    def get(self, request, url):
        product = Product.objects.get(url=url)
        serializer = SingleProductSerializer(product)
        return Response(serializer.data)
