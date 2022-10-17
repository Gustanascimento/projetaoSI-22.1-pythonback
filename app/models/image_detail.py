from django.db import models

from app.models.image_url import ImageUrl


class ImageDetail(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    image_url = models.ForeignKey(
        ImageUrl, on_delete=models.CASCADE, null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'image'
        verbose_name_plural = 'images'

    def __str__(self):
        return self.title
