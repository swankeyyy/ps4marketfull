from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


class UploadForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('photo', )