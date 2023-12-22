from django.contrib.auth.forms import UserCreationForm
from .models import User
class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = '__all__'