from rest_framework import serializers

from .models import ImageDetail, ImageUrl


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageDetail
        fields = ['id', 'title', 'description', 'image_url', 'created_at']


class ImageUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUrl
        fields = ['id', 'url', 'created_at']
