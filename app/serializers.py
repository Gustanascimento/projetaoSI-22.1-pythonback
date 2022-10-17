from rest_framework import serializers

from app.models.image_detail import ImageDetail
from app.models.image_url import ImageUrl


class ImageUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUrl
        fields = ('id', 'url')


class ImageSerializer(serializers.ModelSerializer):
    image_url = ImageUrlSerializer(many=False)

    created_at = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M:%S', read_only=True
    )

    class Meta:
        model = ImageDetail
        fields = ('id', 'title', 'description', 'image_url', 'created_at')
        read_only_fields = ('image_url',)

    def validate_title(self, title):
        if not title:
            raise serializers.ValidationError(
                'Title is required. Please, try again.'
            )
        return title
