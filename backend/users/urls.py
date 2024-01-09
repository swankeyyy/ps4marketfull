from . import views
from django.urls import path

urlpatterns = [
    path('uploadprofile/<int:pk>', views.PhotoUploadView.as_view()),
]


