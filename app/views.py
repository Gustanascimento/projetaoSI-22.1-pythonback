from rest_framework import generics

from .models import Image
# from .permissions import isAuthorOrReadOnly
from .serializers import ImageSerializer


# Create your views here.
class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
