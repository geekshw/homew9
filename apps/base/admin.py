from django.contrib import admin
from apps.base.models import Settings, Image, About
# Register your models here.
admin.site.register(Settings)
admin.site.register(Image)
admin.site.register(About)
