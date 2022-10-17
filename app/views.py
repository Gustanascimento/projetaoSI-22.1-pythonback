from rest_framework import generics

from app.models.image_detail import ImageDetail
from app.models.image_url import ImageUrl
from app.service.request_duck_duck import DuckDuckSearch

# from .permissions import isAuthorOrReadOnly
from .serializers import ImageSerializer, ImageUrlSerializer


# TODO: remover duplicações a partir de urls inseridas
def check_title_image(title):
    search_title_image = DuckDuckSearch()

    url_image_results = search_title_image.get_results(title)

    if url_image := ImageUrl.objects.filter(url=url_image_results):
        return url_image[0]

    obj = ImageUrl.objects.create(url=url_image_results)
    return obj


# Create your views here.
class ImageList(generics.ListCreateAPIView):
    queryset = ImageDetail.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        url = (
            self.request.data['image_url']['url']
            if 'image_url' in self.request.data
            else self.request.data['image_url.url']
        )

        if url == '':
            image_url = check_title_image(self.request.data['title'])
        else:
            image_url = ImageUrl.objects.create(
                url=self.request.data['image_url.url']
            )

        serializer.save(image_url=image_url)

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageDetail.objects.all()
    serializer_class = ImageSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ImageUrlList(generics.ListCreateAPIView):
    queryset = ImageUrl.objects.all()
    serializer_class = ImageUrlSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
