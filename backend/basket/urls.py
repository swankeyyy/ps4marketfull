from . import views
from django.urls import path

urlpatterns = [
    path('basket/<int:pk>', views.BasketView.as_view()),

]


