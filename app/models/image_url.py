from django.db import models


class ImageUrl(models.Model):
    url = models.URLField(default='www.example.com', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'imageurl'
        verbose_name_plural = 'imageurls'

    def __str__(self):
        return self.url
