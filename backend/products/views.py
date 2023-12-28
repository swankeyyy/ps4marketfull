from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer
class AllCategoriesView(APIView):
    """View for List Categories on Frontend (navbar, sidebar)"""

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)