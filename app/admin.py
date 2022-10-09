from django.contrib import admin

# Register your models here.
from app.models.image_detail import ImageDetail
from app.models.image_url import ImageUrl

admin.site.register(ImageDetail)
admin.site.register(ImageUrl)
