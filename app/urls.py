from django.urls import path

from .views import ImageDetail, ImageList, ImageUrlList

urlpatterns = [
    path('images/', ImageList.as_view(), name='image-list-and-create'),
    path(
        'images/<int:pk>/',
        ImageDetail.as_view(),
        name='image-detail-patch-and-destroy',
    ),
    path('images/results/', ImageUrlList.as_view(), name='image-results'),
]
