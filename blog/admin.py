from django.contrib import admin

# Register your models here.

from .models import Article

admin.site.register(Article)
admin.site.site_header = 'admin'
admin.site.site_title = 'login'
