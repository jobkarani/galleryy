from django.contrib import admin
from .models import Image,Location,Category

# Register your models here.
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image)