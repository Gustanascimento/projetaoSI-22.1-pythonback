from django.contrib import admin

# Register your models here.
from .models import ImageDetail, ImageUrl

admin.site.register(ImageDetail)
admin.site.register(ImageUrl)
