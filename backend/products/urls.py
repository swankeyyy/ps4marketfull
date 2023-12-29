from . import views
from django.urls import path

urlpatterns = [
    path('categories/', views.AllCategoriesView.as_view()),
    path('products/', views.AllProductsView.as_view()),
    path('products/<slug:url>', views.SingleProductView.as_view())
]


