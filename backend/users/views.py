from requests import Response
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser
from rest_framework.views import APIView
from .models import User
from .forms import UploadForm


class PhotoUploadView(APIView):
    pass
