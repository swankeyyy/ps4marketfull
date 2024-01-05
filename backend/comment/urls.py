from . import views
from django.urls import path

urlpatterns = [
    path('<int:pk>', views.CommentView.as_view()),

]


