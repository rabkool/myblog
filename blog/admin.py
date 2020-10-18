from django.contrib import admin

# Register your models here.

from .models import Article, Introduce

admin.site.register(Article)
admin.site.register(Introduce)

admin.site.site_header = 'admin'
admin.site.site_title = 'login'
