from django.contrib import admin

from blog.models import Profile, Category, Blog

# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Blog)