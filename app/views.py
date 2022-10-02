from requests import Response
from rest_framework import generics, status

from app.service.request_duck_duck import DuckDuckSearch

from .models import ImageDetail, ImageUrl
# from .permissions import isAuthorOrReadOnly
from .serializers import ImageSerializer, ImageUrlSerializer


def check_title_image(title):
    url_results = DuckDuckSearch()
    url_results.get_results(title)

    if url_image := ImageUrl.objects.filter(url=url_results):
        return url_image[0].id
    else:
        obj = ImageUrl.objects.create(url=url_results)
        return obj.id


# Create your views here.
class ImageList(generics.ListCreateAPIView):
    queryset = ImageDetail.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        if url_image := check_title_image(request.data['title']):
            if not request.GET._mutable:
                request.POST._mutable = True

            request.POST['image_url'] = url_image
            return self.create(request, url_image=url_image, *args, **kwargs)

        # return {'reason': 'success'}
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageDetail.objects.all()
    serializer_class = ImageSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ImageUrlList(generics.ListCreateAPIView):
    queryset = ImageUrl.objects.all()
    serializer_class = ImageUrlSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
