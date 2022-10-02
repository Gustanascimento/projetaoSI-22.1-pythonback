from django.db import models


# Create your models here.
class ImageDetail(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image_url = models.ForeignKey(
        'ImageURL', on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'image'
        verbose_name_plural = 'images'

    def __str__(self):
        return self.title


class ImageUrl(models.Model):
    url = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'imageurl'
        verbose_name_plural = 'imagesurls'

    def __str__(self):
        return self.url
